import yfinance as yf
import requests
from dotenv import load_dotenv
import os

ALPHA_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
# Interest Rate (yfinance)
def get_interest_rate():
    try:
        data = yf.ticker("^TNX")
        hist = yf.history(period = "1d") # Period -> just the sepcified time data
        return round(hist["Close"].iloc[-1],2)
    except:
        return None
    
# Currency (yfinance)
def get_currency_strength():
    try:
        data = yf.ticker("USDINR=X")
        hist = yf.histroy(period= "1d")
        return round(hist["Close"].iloc[-1],2)
    except:
        return None
    
# Inflation(Alpha_Vantage)
def get_inflation():
    try:
        url = f"https://www.alphavantage.co/query?function-INFLATION&apikey={ALPHA_API_KEY}"
        res = requests.get(url).json()

        latest = res["data"][0]
        return float(latest["value"])
    except:
        return None
    
# GDP (World Bank)
def get_gdp_growth():
    try:
        url = "https://api.worldbank.org/v2/country/US/indicator/NY.GDP.MKTP.KD.ZG?format=json"
        res = requests.get(url).json()

        for entry in res[1]:  # res[0] is metadata 
            if entry["value"] is not None: # res[1] is a list of dict's with each dict describing each year
                return round(entry["value"],2) # res is list with res[0] -> dict and res[1] -> list of dict
    except:
        return None
    
# Unemployment (World Bank)
def get_unemployment():
    try:
        url = "https://api.worldbank.org/v2/country/US/indicator/SL.UEM.TOTL.ZS?format=json"
        res = requests.get(url).json()

        for entry in res[1]:
            if entry["value"] is not None:
                return round(entry["value"],2)
    except:
        return None
    
# Master Function
def load_macro_data():
    data = {
        "inflation": get_inflation(),
        "interest_rate": get_interest_rate(),
        "gdp_growth": get_gdp_growth(),
        "unemployment": get_unemployment(),
        "currency_strength": get_currency_strength()
    }

    # fallback if any fail
    for key, value in data.items():
        if value is None:
            data[key] = get_fallback_value(key)

    return data

# FallBacks
def get_fallback_value(indicator):
    fallback = {
        "inflation": 5.0,
        "interest_rate": 4.5,
        "gdp_growth": 2.0,
        "unemployment": 4.0,
        "currency_strength": 80.0,
    }
    return fallback[indicator]