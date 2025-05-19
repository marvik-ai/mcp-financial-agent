import yfinance as yf
import json

def available_currencies() -> list[str]:
    with open("data/currencies.json", "r") as file:
        currencies = json.load(file)
    return currencies

def fx_rate(from_currency: str, to_currency: str) -> float:
    currencies = available_currencies()
    if from_currency.upper() not in currencies or to_currency.upper() not in currencies:
        raise ValueError(f"Invalid currency code: {from_currency} or {to_currency}")

    ticker = f"{from_currency.upper()}{to_currency.upper()}=X"
    data = yf.Ticker(ticker)
    fx_data = data.history(period="1d")
    if fx_data.empty:
        raise ValueError(f"Could not fetch FX rate for {from_currency} to {to_currency}")
    rate = fx_data['Close'].iloc[-1]
    return rate


def currency_conversion(amount: float, from_currency: str, to_currency: str) -> float:
    rate = fx_rate(from_currency, to_currency)
    converted_amount = amount * rate
    return converted_amount