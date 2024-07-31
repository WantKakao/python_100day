import os
import requests
from twilio.rest import Client

api_key = os.getenv("API_KEY")
END_POINT = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
# 위도와 경도
params = {
    'lat': 37.5802,
    'lon': 126.9228,
    'appid': api_key
}

# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}")

# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
response = requests.get(END_POINT, params=params)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for i in range(5):
    weather = weather_data['list'][i]['weather'][0]
    if weather['id'] < 700:
        will_rain = True

if will_rain:
    print('bring umbrellas')
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It won't be rain today! Feel free to go outside!",
        from_=os.getenv("from_"),
        to=os.getenv("to")
    )
    print(message.status)
