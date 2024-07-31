import requests
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key = os.getenv("api_key")
url = 'https://www.alphavantage.co/query'
parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': api_key
}
today = datetime.datetime.now()
year = today.year
month = today.month
if month < 10:
    month = '0' + str(month)
day = today.day

response = requests.get(url, params=parameters)
response.raise_for_status()

data = response.json()['Time Series (Daily)']

# data_list = [value for (key, value) in data.items()]
# yesterday = float(data_list[0]['4. close'])
# day_before_yesterday = float(data_list[1]['4. close'])

yesterday = float(data[f"{year}-{month}-{day-1}"]['4. close'])
day_before_yesterday = float(data[f"{year}-{month}-{day-2}"]['4. close'])
val = (yesterday - day_before_yesterday) / yesterday
if abs(val) < 0.05:
    api_key2 = os.getenv("api_key2")
    url2 = 'https://newsapi.org/v2/top-headlines'
    parameters2 = {
        'apiKey': api_key2,
        'q': 'Tesla'
    }
    response2 = requests.get(url2, params=parameters2)
    response.raise_for_status()

    news = response2.json()['articles'][:3]
    print(news)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
    op = '▼'
    if val > 0:
        op = '▲'
    formatted_article = [f"{STOCK}: {op}{val*100}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in news]
    from twilio.rest import Client

    account_sid = os.getenv("ACCOUNT_SID")
    auth_token = os.getenv("AUTH_TOKEN")

    client = Client(account_sid, auth_token)
    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_=os.getenv("from_"),
            to=os.getenv("to")
        )

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

