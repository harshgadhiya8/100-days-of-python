import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api = "OJMKBE0IYPEAMGX5"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_PARAMETERS ={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    'apikey': stock_api
}

response = requests.get(STOCK_ENDPOINT,params=STOCK_PARAMETERS)
stock_data = response.json()["Time Series (Daily)"]
data = [value for (key,value) in stock_data.items()]
y_closing = data[0]['4. close']
print(y_closing)
day_before_yday_closing = data[1]['4. close']
print(day_before_yday_closing)