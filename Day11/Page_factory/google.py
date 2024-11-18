import time

from bs4 import PageElement
from selenium.webdriver.support.select import Select
from seleniumpagefactory import PageFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Google(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)


    locators = {
        'google_search': ('XPATH', "//textarea[@name='q']"),
        'suggested_list': ('XPATH', "//div[@class='wM6W7d']"),
        'suggested_list2': ('CLASS', 'wM6W7d')
    }

    def enter_elements(self):
        # data = self.login.get_text()
        # print(data)
        self.google_search.set_text("selenium")

    def get_suggisted_list(self):
        dd = self.suggested_list2
        dd.get_all_list_item()
        for ele in dd:
            data = ele.text
            print(data)
