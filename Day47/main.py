import lxml
import requests
from bs4 import BeautifulSoup
import smtplib

url = 'AMAZON_PRODUCT_URL'

headers = {
    'User-Agent': "YOUR_USER_AGENT",
    'Accept-Language': 'YOUR_ACCEPT_LANGUAGE'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

title = soup.find(id="productTitle").get_text().strip()
price_ = soup.select_one('#corePriceDisplay_desktop_feature_div div')
price = float(price_.getText().split()[0][1:])
buy_price = 20

if price < buy_price:
    message = f'{title} is now {price}'
    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )