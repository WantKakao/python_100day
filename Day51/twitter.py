from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url='https://www.speedtest.net/')
        time.sleep(5)
        agree = self.driver.find_element(By.ID, value='onetrust-accept-btn-handler')
        agree.click()
        go = self.driver.find_element(By.CSS_SELECTOR, value='.start-button a')
        go.click()
        time.sleep(70)
        self.down = self.driver.find_element(By.CLASS_NAME, value='download-speed').text
        self.up = self.driver.find_element(By.CLASS_NAME, value='upload-speed').text

    def find_by_name(self, val, key):
        ID = self.driver.find_element(By.NAME, value=val)
        ID.send_keys(key)
        ID.send_keys(Keys.ENTER)

    def tweet_at_provider(self):
        self.driver.get(url='https://x.com/i/flow/login')
        time.sleep(5)
        self.find_by_name('text', 'YOUR_TWITTER_ID')
        time.sleep(1)
        self.find_by_name('text', 'YOUR_TWITTER_NAME')
        time.sleep(1)
        self.find_by_name('password', 'YOUR_TWITTER_PASSWORD')
        time.sleep(5)
        textarea = self.driver.find_element(By.CSS_SELECTOR, value='.DraftEditor-editorContainer span')
        textarea.send_keys(f'My Internet Speed is {self.down} for downloading, {self.up} for uploading.')
