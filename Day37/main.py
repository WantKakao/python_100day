import os
import requests
from datetime import datetime

USERNAME = 'minsoo12'
TOKEN = os.getenv(TOKEN)
GRAPH_ID = 'graph1'

pixela_endpoint = "https://pixe.la/v1/users"

user_parmas = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(pixela_endpoint, json=user_parmas)
# print(response)
# print(response.json())
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    'id': GRAPH_ID,
    'name': 'My Coding Time',
    'unit': 'hr',
    'type': 'int',
    'color': 'sora'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# print(response)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
ymd = today.strftime("%Y%m%d")

pixel_params = {
    'date': ymd,
    'quantity': input("How many hours did you coding today? "),
}

response = requests.post(pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

# response = requests.put(f"{pixel_endpoint}/{ymd}", json={'quantity': '3'}, headers=headers)
# print(response.text)

# response = requests.delete(f"{pixel_endpoint}/{ymd}", headers=headers)
# print(response.text)
