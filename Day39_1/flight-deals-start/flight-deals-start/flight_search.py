import os
import requests
from dotenv import load_dotenv
# from datetime import datetime, timedelta
# from flight_data import find_cheapest_flight
# from notification_manager import NotificationManager

load_dotenv()

TOKEN_ENDPOINT = os.getenv("TOKEN_ENDPOINT")
AIRPORT_ENDPOINT = os.getenv("AIRPORT_ENDPOINT")
FLIGHT_ENDPOINT = os.getenv("FLIGHT_ENDPOINT")


class FlightSearch:

    def __init__(self):
        self._api_key = os.getenv("API_KEY")
        self._api_secret = os.getenv("API_SECRET")
        self._token = self._get_new_token()

    def get_destination_code(self, city_name):
        headers = {'Authorization': f"Bearer {self._token}"}
        params = {
            'keyword': city_name,
            'max': 1,
            'include': 'AIRPORTS'
        }
        response = requests.get(url=AIRPORT_ENDPOINT, headers=headers, params=params)
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        return code

    def _get_new_token(self):
        data = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(url=TOKEN_ENDPOINT, data=data, headers=headers)
        return response.json()['access_token']

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()

# LON 에서 PAR 로 가는 최저가 비행기 찾기
# flight_search = FlightSearch()
# flight_search.get_destination_code('paris')
# tomorrow = datetime.now() + timedelta(days=1)
# six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
# flights = flight_search.check_flights("LON", "PAR", tomorrow, six_month_from_today)
# cheapest_flight = find_cheapest_flight(flights)
# print(f"paris: £{cheapest_flight.price}")
# if cheapest_flight.price != "N/A" and cheapest_flight.price < 5000:
#     notification_manager = NotificationManager()
#     print(f"Lower price flight found to paris!")
#     notification_manager.send_sms(
#         message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
#                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
#                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
#     )