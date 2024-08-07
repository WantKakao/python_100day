# 2단계 지원까지 맛보기 후 종료하는 프로그램
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3987831632&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

time.sleep(1)
login = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
login.click()

id = driver.find_element(By.NAME, value='session_key')
pw = driver.find_element(By.NAME, value='session_password')
id.send_keys('YOUR_LINKEDIN_ID')
pw.send_keys('YOUR_LINKEDIN_PASSWORD')
pw.send_keys(Keys.ENTER)
# 보안인증 직접 해야할 수 있음
time.sleep(30)


def apply_company():
    apply = driver.find_element(By.CLASS_NAME, value='jobs-apply-button')
    apply.click()
    time.sleep(1)

    phone = driver.find_element(By.CLASS_NAME, value='artdeco-text-input--input')
    phone.send_keys('12341234')
    next1 = driver.find_element(By.CSS_SELECTOR, value='form button')
    next1.send_keys(Keys.ENTER)
    next2 = driver.find_elements(By.CSS_SELECTOR, value='form footer button')[1]
    next2.send_keys(Keys.ENTER)

    close_button = driver.find_element(By.CSS_SELECTOR, value='#artdeco-modal-outlet button')
    close_button.click()
    delete_button = driver.find_element(By.CLASS_NAME, value='artdeco-button--secondary')
    delete_button.click()


jobs = driver.find_elements(By.CLASS_NAME, value='job-card-container')
# scroll down 하지 않으면 len = 7
# print(len(jobs))
for j in range(len(jobs)):
    jobs[j].click()

    apply_company()
    time.sleep(2)
