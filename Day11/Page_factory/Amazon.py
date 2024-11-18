import time

from bs4 import PageElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from seleniumpagefactory import PageFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class dropdown(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators={
        'dropdown_value': ('XPATH', "//select[@id='searchDropdownBox']"),
        'mobile': ('XPATH', "//a[text()='Mobiles']")
    }

    def dd(self):
        # wait = WebDriverWait(self.driver, 10)
        # drop = wait.until(EC
        # .visibility_of(self.dropdownvalue))
        dropdown = self.driver.find_element(By.XPATH,"//select[@id='searchDropdownBox']")
        select = Select(dropdown)
        time.sleep(3)
        select.select_by_index(3)

    def click_on_mobile(self):
        self.mobile.click()