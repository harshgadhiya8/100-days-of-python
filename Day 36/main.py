import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api = "stored it in notes"
news_api = "stored it in notes"

account_sid = "stored it in notes"
auth_token = "stored it in notes"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_PARAMETERS ={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey": stock_api
}
NEWS_PARAMETERS ={
    "apikey": news_api,
    "q" : COMPANY_NAME,

}
response = requests.get(STOCK_ENDPOINT,params=STOCK_PARAMETERS)
stock_data = response.json()["Time Series (Daily)"]
data = [value for (key,value) in stock_data.items()]
y_closing = data[0]['4. close']
day_before_yday_closing = data[1]['4. close']
difference = (float(y_closing) - float(day_before_yday_closing))
up_down = None
if difference > 0:
    up_down = "🔺"
if difference > 0:
    up_down = "🔻"
diff_percent = round((difference/float(y_closing)) * 100)
if abs(diff_percent) > 0:
    response = requests.get(NEWS_ENDPOINT,params=NEWS_PARAMETERS)
    articles = response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    client = Client(account_sid,auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_= "**********",
            to="***********"
        )
        print(message.status)
