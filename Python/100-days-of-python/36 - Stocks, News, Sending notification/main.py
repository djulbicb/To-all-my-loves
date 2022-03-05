import requests

# News
# https://newsapi.org/docs/client-libraries/python

# Stocks
# ===============================================================
import pandas as pd
import requests
import datetime as dt
STOCK_API_KEY = "###"
NEWS_API_KEY = "###"
STOCK_NAME = "Tesla"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_params={
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data=response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_closing_price=float(data_list[0]["4. close"])
day_before_closing_price=float(data_list[1]["4. close"])
print(yesterday_closing_price, day_before_closing_price)

diff_closing_price=abs(yesterday_closing_price - day_before_closing_price)
diff_percent=(diff_closing_price / yesterday_closing_price) * 100
print(diff_closing_price, diff_percent)

# News
# ===============================================================
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key=NEWS_API_KEY)
all_articles = newsapi.get_everything(qintitle='Tesla',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2022-02-01',
                                      to='2022-02-10',
                                      language='en',
                                      sort_by='relevancy')
top_articles = all_articles["articles"][:1]
formatted_news = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in top_articles]
print(top_articles)

# Send email
# ===============================================================
# SMTP - Simple mail transfer protocol
import smtplib

USERNAME = "###"
PASSWORD = "###"

# za svakog providera drugaciji email server
with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
    connection.set_debuglevel(0)
    connection.starttls() # da se pokrene tls security
    connection.login(user=USERNAME, password=PASSWORD)
    # subject:Za naslov
    connection.sendmail(from_addr=USERNAME,
                        to_addrs="###",
                        msg="fSubject:Hello\n\nHello Hello\n\n{formatted_news}")
    connection.close()
