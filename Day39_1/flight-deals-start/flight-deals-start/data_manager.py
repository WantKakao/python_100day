import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")


class DataManager:

    def __init__(self):
        self._user = os.getenv("SHEETY_USRERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        print(response.json())
        self.destination_data = response.json()['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            body = {'price': {'iataCode': city['iataCode']}}
            response = requests.put(f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=body, auth=self._authorization)
            print(response.json())
