import os, requests, json
from datetime import datetime

APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')
SHEET_ENDPOINT = os.getenv('SHEET_ENDPOINT')
AUTHORIZATION = os.getenv('AUTHORIZATION')

url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
}

body = {
    'query': input("What exercise did you do? ")
}

response = requests.post(url, headers=headers, data=json.dumps(body))
data = response.json()['exercises']

now = datetime.now()
date = now.strftime('%d/%m/%Y')
time = now.strftime("%H:%M:%S")


sheety_headers = {
    'Content-Type': 'application/json',
    'Authorization': AUTHORIZATION
}

for i in range(len(data)):
    sheety_body = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': data[i]['name'].title(),
            'duration': data[i]['duration_min'],
            'calories': data[i]['nf_calories']
        }
    }

    response = requests.post(SHEET_ENDPOINT, headers=sheety_headers, data=json.dumps(sheety_body))
    print(response.text)
    print(response)

# run 4km cycle 3km swim 5km