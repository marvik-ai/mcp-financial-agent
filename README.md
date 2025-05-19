# MCP-FX: Financial Agent and FX Calculator

## Overview

MCP-FX is a financial assistant project that leverages advanced AI models and tools to provide currency exchange rate calculations, currency conversion, and interactive chat-based assistance. The project integrates multiple components, including a server for FX calculations and various agent implementations for user interaction.

## Features

- **Currency Exchange Rate Calculation**: Fetches real-time FX rates using Yahoo Finance.
- **Currency Conversion**: Converts amounts between currencies using the latest FX rates.
- **Interactive Chat Agents**: Provides a console-based chat interface for user interaction.
- **Multi-Agent Support**: Includes implementations using LangGraph, Google ADK, and Agent SDK.

## Project Structure

```
.
├── data/
│   └── currencies.json          # List of supported currencies
├── src/
│   ├── financial_agent/
│   │   ├── mcp_servers.py       # MCP clients extension
│   │   ├── chat.py              # Console chat utilities
│   │   └── agent.py/            # Agent SDK implementation
│   └── server/
│       ├── app.py               # FX Calculator server
│       └── fx_calculator.py     # FX calculation logic
├── requirements.txt             # Python dependencies
├── Makefile                     # Commands for running the project
├── .env                         # Environment variables
└── template.env                 # Template for environment variables
```

## Prerequisites

- Python 3.10 or higher
- [OpenAI API Key](https://platform.openai.com/signup/)
- [Yahoo Finance API](https://finance.yahoo.com/)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mcp-fx
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

Copy `template.env` to `.env`:
  ```bash
  cp template.env .env
  ```
Add your OpenAI API key to `.env`.

## Usage

### Start the FX Calculator Server

Run the following command to start the server:
```bash
make start-server
```

The server will be available at `http://localhost:9000`.

### Run the Agent


```bash
make start-agent-sdk-example
```


### Interact with the Agent

Once an agent is running, you can interact with it via the console. Type your queries, and the agent will respond. To exit, type `exit`.

## Supported Currencies

The project supports the following currencies:
- USD: United States Dollar
- EUR: Euro
- GBP: British Pound Sterling
- JPY: Japanese Yen
- CHF: Swiss Franc
- CAD: Canadian Dollar
- AUD: Australian Dollar
- NZD: New Zealand Dollar
- CNY: Chinese Yuan

## Database Setup

### Start PostgreSQL Database

To start the PostgreSQL database, run the following command:
```bash
docker-compose up -d postgres
```

This will start the database service in a Docker container. The database will be accessible at `localhost:5432` with the credentials specified in the `.env` file.

### Connect to the Database

You can connect to the database using any PostgreSQL client with the following details:
- **Host**: `localhost`
- **Port**: `5432`
- **Database**: `financial_db`
- **User**: `admin`
- **Password**: `adminpassword`

### Stop the Database

To stop the database service, run:
```bash
docker-compose down
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.