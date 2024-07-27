from dotenv import load_dotenv
import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import base64
from openai import ChatCompletion
import time


def init_database(user:str,password:str,host:str,port:str,database:str)->SQLDatabase:
    db_uri=f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"

    conn = mysql.connector.connect(
        host=host,
        port=int(port),
        user=user,
        password="Ishikarathore@76",
        database=database
    )
    return conn, SQLDatabase.from_uri(db_uri)


     

def get_sql_chain(db):
     template = """You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
            Based on the table schema below, write a SQL query that would answer the user's question. Take the conversation history into account to maintain context and continuity.

            <SCHEMA>{schema}</SCHEMA>

            Conversation History: {chat_history}

            STRICTLY FOLLOW 1: Write only the SQL query and nothing else. Do not wrap the SQL query in any other text, not even backticks.
            STRICTLY FOLLOW 2: Not use '\' in SQL query.

            For example:
            Question: Which 3 artists have the most tracks?
            SQL Query: SELECT ArtistId, COUNT(*) as track_count FROM Track GROUP BY ArtistId ORDER BY track_count DESC LIMIT 3;
            Question: Name 10 artists
            SQL Query: SELECT Name FROM Artist LIMIT 10;

            Your turn:

            Question: {user_query}
            SQL Query:
            """
     
     prompt = ChatPromptTemplate.from_template(template)
    #  llm = ChatOpenAI(model="gpt-4-turbo")
     llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0)

     def get_schema(_):
         return db.get_table_info()
     
     return(
         RunnablePassthrough.assign(schema=get_schema)
         | prompt
         | llm
         | StrOutputParser()
     )




def get_response(user_query,database_response):
    # sql_chain = get_sql_chain(db)
    
    template = """You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
        Based on the user's question, and the SQL response, write a natural language response that clearly answers the user's question and ensures user satisfaction.

        User Question: {user_query}
        SQL Response: {database_response}
        """
    
    prompt = ChatPromptTemplate.from_template(template)
    # llm = ChatOpenAI(model="gpt-4-turbo")
    llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0)
    
    chain = (
        # RunnablePassthrough.assign(query=sql_chain).assign(
        # schema=lambda _: db.get_table_info(),
        # response=lambda vars: db.run(vars["query"]),
        # )
        prompt
        | llm
        | StrOutputParser()
    )
    
    return chain.invoke({
        "user_query": user_query,
        "database_response":database_response
    })





def get_response_for_graph(html_table, user_query):
    template = """Given the tabular data provided below and the user's query, generate Python code to create an informative graph that accurately represents the data.

        <TABULAR_DATA>
        {html_table}
        </TABULAR_DATA>

        User Query: {user_query}

        Ensure the generated code is executable and produces a clear, informative visualization using matplotlib or seaborn. The graph should be relevant to the query and the data structure.

        STRICTLY FOLLOW these guidelines:
        1. Do not include "```python" in the code, as this causes an error.
        2. Provide only the executable code without any extra text before or after the code.
        3. Do not include any print statements in the code, as they cause errors.
        4. Please use different colors every time for the graph.

        Example:
        User Query: Show the distribution of values in column 'age'.
        Code:
        import matplotlib.pyplot as plt
        import pandas as pd
        from io import StringIO

        df = pd.read_csv(StringIO(data))
        plt.hist(df['age'])
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.title('Age Distribution')
        plt.show()
        """

    
    prompt = ChatPromptTemplate.from_template(template)
    # llm = ChatOpenAI(model="gpt-4-turbo")
    llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0)
    
    return(
         prompt
         | llm
         | StrOutputParser()
     )





if "chat_history" not in st.session_state:
    st.session_state.chat_history =  [
        AIMessage(content="Hello! I'm a SQL assistant. Ask me anything about your database.")
    ]
    
if "history" not in st.session_state:
    st.session_state.history =  [
        AIMessage(content="Hello! I'm a SQL assistant. Ask me anything about your database.")
    ]

load_dotenv()

st.set_page_config(page_title="IntelliQuery",page_icon=":speech_balloon:")

st.title("Get Instant Data Insights")


if 'connected' not in st.session_state:
    st.session_state.connected = False

with st.sidebar:
    st.subheader("Settings")
    st.write("AI-Driven Chat Interface Uses LLM for Instant Insights and Visualizations from Internal Client Databases")

    with st.expander("Database Connection Settings"):
        st.text_input("Host", value="localhost", key="Host")
        st.text_input("Port", value="3306", key="Port")
        st.text_input("User", value="root", key="User")
        st.text_input("Password", type="password", value="Ishikarathore%4076", key="Password")
        st.text_input("Database", value="Chinook", key="Database")

    if st.button("Connect"):
        with st.spinner("Connecting to database..."):
            conn, db = init_database(
                st.session_state["User"], 
                st.session_state["Password"],
                st.session_state["Host"],
                st.session_state["Port"],
                st.session_state["Database"]
            )
            st.session_state.db = db
            st.session_state.conn = conn
            st.session_state.connected = True
            st.success("Connected to database!")


    if st.session_state.connected:
        try:
            cursor = st.session_state.conn.cursor()
            cursor.execute("SHOW TABLES")
            tables = [table[0] for table in cursor.fetchall()]

            # Dropdown for table selection
            selected_table = st.selectbox("Select a table to view schema:", tables)

            if selected_table:
                cursor.execute(f"DESCRIBE {selected_table}")
                schema = cursor.fetchall()

                st.markdown(f"### Table: {selected_table}")
                st.markdown("#### Schema:")
                for column in schema:
                    st.markdown(f"- **{column[0]}**: {column[1]}")
        except Exception as e:
            st.error(f"Error fetching schema: {e}")


                
for message in st.session_state.history:
    if isinstance(message,AIMessage):
        with st.chat_message("AI"):
            # st.markdown(message.content, unsafe_allow_html=True)

            content = message.content
            # Check if the message contains graph code
            if "```python" in content:
                # Extract graph code and other content
                parts = content.split("```python")
                text_part = parts[0].strip()  # Text before the code block
                code_part = parts[1].split("```")[0].strip()  # Code block
                
                # Display other content
                if text_part:
                    st.markdown(text_part, unsafe_allow_html=True)
                
                # Execute and display graph code
                try:
                    exec(code_part)
                    st.pyplot(plt)
                except Exception as e:
                    st.error(f"An error occurred while executing the graph code: {e}")
            else:
                # Render any other text content
                st.markdown(content, unsafe_allow_html=True)
    elif isinstance(message,HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)


user_query = st.chat_input("Type a message...")

if user_query is not None and user_query.strip()!="":
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    st.session_state.history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        
        sql_chain = get_sql_chain(st.session_state.db)
        sql_query=sql_chain.invoke({
            "chat_history": st.session_state.chat_history,
            "user_query":user_query    
        })
        database_response = pd.read_sql_query(sql_query,st.session_state.conn)
        NLP_response = get_response(user_query,database_response)

        html_table = database_response.to_html(index=False, classes='table table-striped')
        graph_code = get_response_for_graph(html_table,user_query)

        graph_code=graph_code.invoke({
            "user_query": user_query,
            "html_table": html_table
        })
        st.markdown(f"**SQL Query:**\n{sql_query}\n")
        st.markdown(f"**Response:**\n{NLP_response}\n")
        st.markdown(f"**Response in Table format:**\n{html_table}\n", unsafe_allow_html=True)
        st.markdown("\n\n**Response in Graph format:**\n")
        try:
            exec(graph_code)
            st.pyplot(plt)
        except Exception as e:
            st.error(f"An error occurred while executing the graph code: {e}")

    st.session_state.chat_history.append(AIMessage(content=f"**SQL Query:**\n{sql_query}\n\n"))

    st.session_state.history.append(AIMessage(content=f"**SQL Query:**\n{sql_query}\n\n**Response:**\n{NLP_response}\n\n**Response in Table format:**\n{html_table}\n\n**Response in Graph format:**\n```python\n{graph_code}\n```"))
    
    
