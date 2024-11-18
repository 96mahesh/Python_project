import time

from selenium.webdriver.common.by import By


class Login_nopCommerce():

    def __init__(self,driver):
        self.driver = driver
        self.user_name = (By.XPATH,"//input[@name='Email']")
        self.user_pass = (By.XPATH,"//input[@name='Password']")
        self.login = (By.XPATH,"//button[text()='Log in']")

    def openUrl(self,url):
        self.driver.get(url)

    def enter_username(self,email):
        time.sleep(2)
        self.driver.find_element(*self.user_name).clear()
        self.driver.find_element(*self.user_name).send_keys(email)

    def enter_password(self,password):
        time.sleep(2)
        self.driver.find_element(*self.user_pass).clear()
        self.driver.find_element(*self.user_pass).send_keys(password)

    def clickOn_login(self):
        time.sleep(2)
        self.driver.find_element(* self.login).click()





