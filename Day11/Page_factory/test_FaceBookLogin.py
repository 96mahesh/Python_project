import time

from selenium import webdriver

from Day11.Page_factory.Amazon import dropdown
from Day11.Page_factory.facebooklogin import FbLoginpage
from Day11.Page_factory.google import Google


class Test_loginWith_valid_Credintial:
    def test_login_functions(self):
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com")
        fb = FbLoginpage(driver)
        fb.enter_uesrname("78"
                          "24358565")
        fb.enter_password("swapna")
        fb.get_element_text()
        fb.click_on_login()

    def test_amazon_Drop_Down(self):
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.get("https://www.amazon.in")
        time.sleep(3)
        d = dropdown(driver)
        d.dd()
        # d.click_on_mobile()
        time.sleep(3)

    def test_google_serach(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.google.com")
        time.sleep(3)
        g = Google(driver)
        g.enter_elements()
        g.get_suggisted_list()
        # d.click_on_mobile()
        time.sleep(3)



