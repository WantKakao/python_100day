from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# chrome_driver_path = YOUR CHROME DRIVER PATH
# driver = webdriver.Chrome(chrome_driver_path)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(url='https://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, value='cookie')

items = driver.find_elements(By.CSS_SELECTOR, value='#store div')
names = []
for i in range(len(items)-1):
    name = items[i].get_attribute('id')
    names.append(name)
names = names[::-1]


def buy():
    prices = []
    P = driver.find_elements(By.CSS_SELECTOR, value='#store b')
    for i in range(len(names)):
        price = P[i].text.split(' - ')[1].split('\n')[0]
        int_price = int(price.replace(',', ''))
        prices.append(int_price)
    prices.sort(reverse=True)

    money = driver.find_element(By.ID, value='money')
    money = int(money.text)
    for idx in range(len(prices)):
        if prices[idx] <= money:
            item = driver.find_element(By.ID, value=f'{names[idx]}')
            item.click()
            break


timeout = time.time() + 5
five_min = time.time() + 60  # finish time (sec)

while True:
    cookie.click()

    if time.time() > timeout:
        buy()
        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, value="cps").text
        print(cookie_per_s)
        break

# driver.quit()
