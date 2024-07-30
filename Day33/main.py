import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]['latitude']
#
# iss_position = (longitude, latitude)
#
# print(iss_position)


parameters = {
    'lat': 36.7201600,
    'lng': -4.4203400,
    'formatted': 0
}

# response = requests.get(url="https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400")
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise)
print(sunset)
