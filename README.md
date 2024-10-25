# Mirror: A Natural Language Interface for Data Exploration and Analysis

Welcome to **Mirror**, an open-source platform designed to simplify data querying, summarization, and visualization by leveraging large language models (LLMs). Mirror offers a natural language interface for database interaction, making data exploration accessible to both technical and non-technical users. 

## Overview

**Mirror** is a versatile tool that enables users to interact with data through an intuitive natural language interface. Users can enter queries in plain language, which are then converted into SQL commands by a pretrained language model. The platform also offers visualizations for easier data interpretation, along with options to preview and refine generated SQL commands to suit specific needs.

## Key Features

- **Natural Language Querying**: Query your databases using everyday language.
- **Automated SQL Generation**: Translates queries into executable SQL statements.
- **Editable SQL Preview**: View and adjust SQL commands before execution.
- **Data Visualization**: Automatically generates visualizations for query results.
- **Human-in-the-Loop**: Allows users to edit and refine SQL for greater control and accuracy.
- **Plug-and-Play Design**: Easily adaptable to various databases without training on additional datasets.

## System Requirements

- **Backend**: Node.js (for database connectivity and API handling)
- **Databases Supported**: Major relational databases, along with CSV files (handled by SQLite)
- **APIs**: Codex API for SQL generation, GPT-3 for summarization, Vega for visualizations

## Getting Started

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/mirror-data/mirror.git
   ```
2. **Install Dependencies**
   ```bash
   cd mirror
   npm install
   ```
3. **Configure Environment Variables**
   Update your `.env` file with the API keys required for OpenAI Codex and GPT-3.

4. **Run the Server**
   ```bash
   npm start
   ```

### Usage

1. **Initialize Database Connection**: Connect to your database or CSV file through the Mirror interface.
2. **Input Queries**: Type in your query in natural language.
3. **SQL Generation & Editing**: Mirror will auto-generate SQL based on your query, with options for manual editing.
4. **Visualization**: Automatically generated visuals can be customized and exported for reporting.

## Components and Workflow

1. **Data Query**: Mirror constructs prompts with metadata and queries, which Codex then converts to SQL. Users may preview and edit these SQL commands as needed.
2. **Summarization**: Mirror uses GPT-3 to generate natural language summaries, helping users quickly understand data results.
3. **Visualization**: Automatically generates visuals (e.g., bar charts, line graphs) using Vega to make data insights more accessible.

## Example Use Cases

1. **Sports Data Question-Answering**: Mirror can connect to real-time sports databases, enabling fans to ask questions and receive current statistics and updates.
2. **OSS Insight**: Integration with open-source event analysis to monitor software development trends.

## Contributing

We welcome contributions! If you're interested in improving Mirror, please refer to the `CONTRIBUTING.md` for guidelines.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

For more information, visit our [GitHub repository](https://github.com/mirror-data/mirror).
