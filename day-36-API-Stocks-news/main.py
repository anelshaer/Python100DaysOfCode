import os
import requests
from itertools import islice
from datetime import datetime, timedelta
from twilio.rest import Client


STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"
STOCK_CHANGE_PERCENTILE = 10

STOCK_API_URL = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ["STOCK_API_KEY"]
STOKE_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

NEWS_API_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ['NEWS_API_KEY']
date_before_3days = datetime.today().date() - timedelta(days=7) 
NEWS_PARAMETERS = {
    "qInTitle": COMPANY_NAME,
    "from": date_before_3days,
    "pageSize": 3,
    "apiKey": NEWS_API_KEY,
}

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
my_phone_number = os.environ['MY_PHONE']
twilio_number = os.environ['TWILIO_NUMBER']


def get_stock_changes():
    response = requests.get(url=STOCK_API_URL, params=STOKE_PARAMETERS)
    response.raise_for_status()
    stock_last_100 = response.json()['Time Series (Daily)']
    last_2_day_keys = list(islice(stock_last_100, 2))    
    stock_yesterday_closing_price = float(stock_last_100[last_2_day_keys[0]]['4. close'])
    stock_day_before_closing_price = float(stock_last_100[last_2_day_keys[1]]['4. close'])
    last_2_days_stock_percentile = round((stock_yesterday_closing_price - stock_day_before_closing_price) * 100 / stock_yesterday_closing_price, 2)
    print(f"{STOCK}: {last_2_days_stock_percentile}%")

    if last_2_days_stock_percentile >= STOCK_CHANGE_PERCENTILE:    
        send_sms(f"{STOCK}: 🔺{last_2_days_stock_percentile}%")
        get_news_headlines()
    elif last_2_days_stock_percentile <= -STOCK_CHANGE_PERCENTILE:
        send_sms(f"{STOCK}:  🔻{abs(last_2_days_stock_percentile)}%")
        get_news_headlines()


def get_news_headlines():
    response = requests.get(url=NEWS_API_URL, params=NEWS_PARAMETERS)
    response.raise_for_status()
    articles = response.json()['articles']    
    for article in articles:
        print((f"Title: {article['title']}\nBrief: {article['description']}"))
        send_sms(f"Title: {article['title']}\nBrief: {article['description']}")


def send_sms(sms_body):
    client = Client(account_sid, auth_token)
    client.api.account.messages.create(
        to=my_phone_number,
        from_=twilio_number,
        body=sms_body
    )



get_stock_changes()
