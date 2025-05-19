from fastmcp import FastMCP
from server.fx_calculator import available_currencies, fx_rate, currency_conversion

# Create a server instance
mcp = FastMCP(
    name="FXCalculatorServer",
)


@mcp.resource("config://currencies")
def get_available_currencies() -> list[str]:
    """
    Fetches all the available currencies, their tickers and names.
    """
    return available_currencies()

@mcp.tool()
def get_fx_rate(from_currency: str, to_currency: str) -> float:
    """
    Fetches the current FX rate from Yahoo Finance from the from_currency to the to_currency. 
    Currencies need to be provided as tickers, as can be found in the get_available_currencies() source.
    """
    return fx_rate(from_currency, to_currency)

@mcp.tool()
def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Converts a given amount from one currency to another using the latest FX rate.
    Currencies need to be provided as tickers, as can be found in the get_available_currencies() source.
    """
    return currency_conversion(amount, from_currency, to_currency)

if __name__ == "__main__":
    mcp.run()
