# Navidata

Navidata is an open-source platform for intuitive data exploration and analysis, leveraging the power of large language models (LLMs). It offers a seamless natural language interface to interact with databases, automatically generating and executing SQL queries based on user input. Navidata also provides visualizations and summarizations of data, making it accessible to both technical users and non-technical professionals.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [System Components](#system-components)
- [Use Cases](#use-cases)
- [References](#references)

---

## Features

- **Natural Language Querying**: Easily query databases with natural language inputs, supported by advanced semantic parsing.
- **Automatic SQL Generation**: Translate natural language queries into SQL commands; preview and edit commands as needed.
- **Data Visualization**: Generate interactive visualizations automatically, enhancing data understanding and analysis.
- **Flexible Integrations**: Connect with multiple data sources, including relational databases and CSV files.
- **Human-in-the-Loop**: Provides options for manual SQL editing and query refinement, ensuring accuracy and control.
- **Plug-and-Play**: Simple setup with no need for additional training data; ready for diverse data exploration scenarios.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/navidata/navidata.git
    ```
2. **Install Dependencies**:
    ```bash
    cd navidata
    pip install -r requirements.txt
    ```
3. **Environment Configuration**:
   Configure the API keys for LLMs (e.g., OpenAI Codex) and database credentials in `.env` or directly in `config.py`.

4. **Run the Application**:
   ```bash
   python app.py
   ```

## Usage

1. Launch the application and connect to your preferred data source.
2. Use the natural language interface to input queries. Navidata generates SQL commands automatically.
3. Edit and review the SQL commands if necessary.
4. View data summarizations and visualizations generated in response to your query.

## System Components

- **Data Query Module**: Translates natural language queries into SQL, allowing users to fine-tune the queries.
- **Summarization and Visualization Module**: Summarizes data in natural language and generates visualizations using Vega for easy interpretation.
- **Pre-trained Models**: Utilizes large language models (e.g., OpenAI Codex, GPT-3) for SQL generation, data summarization, and visualization code creation.

## Use Cases

### 1. Business Intelligence
Navidata can connect to live business databases, providing rapid insights and visual summaries for non-technical professionals.

### 2. Sports Analytics
Integrate real-time sports data for up-to-date insights on player performance, team rankings, and more.

### 3. Open-Source Event Analysis
With OSS Insight Data Explorer, Navidata can analyze data from open-source repositories, providing summaries and trends over time.

## References

For further details, please refer to the original paper:  
Xu, C., McAuley, J., & Wang, P. (2023). *Mirror: A Natural Language Interface for Data Querying, Summarization, and Visualization*. In Companion Proceedings of the ACM Web Conference 2023. [https://doi.org/10.1145/3543873.3587309](https://doi.org/10.1145/3543873.3587309)
