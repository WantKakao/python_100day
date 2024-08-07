from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(url='https://secure-retreat-92358.herokuapp.com/')
# article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# article_count.click()
# talk = driver.find_element(By.LINK_TEXT, value="Talk")
# talk.click()
first_name = driver.find_element(By.NAME, value='fName')
last_name = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')

first_name.send_keys("hello")
last_name.send_keys("my friend")
email.send_keys("example@gmail.com")
# email.send_keys(Keys.ENTER)
submit = driver.find_element(By.CSS_SELECTOR, value='form button')
submit.click()

# driver.quit()
