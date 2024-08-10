from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(url='https://www.instagram.com/accounts/login/')
        time.sleep(3)
        insta_id = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        insta_pw = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        insta_id.send_keys('YOUR_INSTA_ID')
        insta_pw.send_keys('YOUR_INSTA_PASSWORD')
        insta_pw.send_keys(Keys.ENTER)
        time.sleep(5)
        self.click_by_class('x1i10hfl')
        self.click_by_class('_a9_1')

    def click_by_class(self, val):
        target = self.driver.find_element(By.CLASS_NAME, value=val)
        print(target.text)
        target.click()
        time.sleep(3)

    def find_followers(self):
        self.driver.get(url='https://www.instagram.com/1min_cook/')
        time.sleep(3)
        followers = self.driver.find_element(By.XPATH, "//a[text()='팔로워 ']")
        followers.click()
        # 자바스크립트를 사용해 스크롤 다운
        time.sleep(3)
        modal = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for _ in range(5):  # 여러 번 스크롤하기 위해 반복
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)  # 잠시 대기하여 콘텐츠가 로드되도록 함

    def follow(self):
        people = self.driver.find_elements(By.CSS_SELECTOR, "button._acan._acap._acas._aj1-._ap30")
        for p in people:
            try:
                p.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel.click()
