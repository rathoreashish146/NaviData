# NaviData: Natural Language Database Explorer

A modern data exploration platform that lets you query and analyze data using natural language. Built with GPT-4, this tool transforms plain English questions into SQL queries and generates insightful visualizations.

## ✨ Key Features

- **Natural Language to SQL**: Ask questions in plain English, get SQL queries
- **Interactive Visualizations**: Auto-generates relevant charts and graphs
- **Data Summarization**: Get natural language summaries of query results
- **Query Verification**: Review and edit generated SQL before execution
- **Multi-DB Support**: Works with popular SQL databases and CSV files

## 🚀 Getting Started

```bash
# Install dependencies
npm install

# Configure environment variables
cp .env.example .env
# Add your GPT-4 API key to .env

# Start the application
npm start
```

## 🔧 Configuration

```env
OPENAI_API_KEY=your_api_key_here
DATABASE_URL=your_database_connection_string
PORT=3000
```

## 💡 Usage Example

Simply type your question:
```
"What were our top 5 selling products last month?"
```

NaviData will:
1. Generate appropriate SQL
2. Execute the query
3. Create visualizations
4. Provide a natural language summary

## 🛠️ Built With

- Frontend: React + Tailwind CSS
- Backend: Node.js + Express
- LLM: GPT-4 API
- Visualization: D3.js/Vega
- Database: SQL/SQLite support

## 🔒 Security Features

- Read-only database connections
- Input validation and sanitization
- Rate limiting for API calls

## 📦 Project Structure

```
navidata/
├── client/          # React frontend
├── server/          # Node.js backend
├── config/          # Configuration files
└── utils/           # Helper functions
```

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request

## 📄 License

MIT License - feel free to use for personal or commercial projects.

## 🙏 Acknowledgments

Based on the research paper "Mirror: A Natural Language Interface for Data Querying, Summarization, and Visualization" (WWW '23) by Canwen Xu, Julian McAuley, and Penghan Wang.
