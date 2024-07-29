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
#         msg="Subject:Hello\n\nThis is body of my email"
#     )


import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2000, month=1, day=1, hour=1)
print(date_of_birth)

with open("quotes.txt") as quote:
    q = quote.readlines()
    random_quote = random.choice(q)
print(random_quote)