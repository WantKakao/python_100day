import requests
from datetime import datetime
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        print('above')
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if sunset <= time_now.hour <= sunrise:
        print('night')
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        # import smtplib
        #
        # my_email = "hou38304@gmail.com"
        # password = "hou1234."
        #
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     # securing connection to email server
        #     connection.starttls()
        #     connection.login(user=my_email, password=password)
        #     connection.sendmail(
        #         from_addr=my_email,
        #         to_addrs="hou38305@gmail.com",
        #         msg="Subject:Look up\n\nThe ISS is above on your head"
        #     )
        print('Look up in the sky')
