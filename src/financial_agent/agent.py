import asyncio
import os
import textwrap

import dotenv
from agents import Agent
from agents.model_settings import ModelSettings

from financial_agent.chat import console_chat
from financial_agent.mcp_servers import ExtendedMCPServerSse, ExtendedMCPServerStdio

dotenv.load_dotenv()

async def main():

    db = os.getenv("POSTGRES_DB")
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")

    connection_string = f"postgresql://localhost/{db}?user={user}&password={password}"
    local_server = ExtendedMCPServerStdio(
        name="Postgres Server",
        params={
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-postgres",
                f"{connection_string}",
            ],
        },
    )

    remote_server = ExtendedMCPServerSse(
        name="SSE Python Server",
        params={
            "url": "http://127.0.0.1:9000/sse",
        })

    async with local_server, remote_server:
        schema = await local_server.get_resource("postgres://localhost/last_quarter_subsidiary_financials/schema")
        currencies = await remote_server.get_resource("config://currencies")
        prompt = textwrap.dedent(
            f"""You are a financial analysis agent responsible for retrieving and 
            analyzing financial and operational data for Wayne Industries from a PostgreSQL database.
            Use the available tools to complete your tasks efficiently and accurately"
            The database schema is as follows:
            {schema}
            The supported currencies for conversion are:
            {currencies}"""
        )
        agent = Agent(
            name="Assistant",
            instructions=prompt,
            model="gpt-4.1-2025-04-14",
            mcp_servers=[local_server, remote_server],
            model_settings=ModelSettings(tool_choice="auto"),
        )
        await console_chat(agent)

if __name__ == "__main__":
    asyncio.run(main())