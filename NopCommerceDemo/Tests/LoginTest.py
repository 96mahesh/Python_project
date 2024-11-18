from selenium import webdriver

from NopCommerceDemo.Pages.LoginPage import Login_nopCommerce



def test_loginTest_nopCommerce():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    login = Login_nopCommerce(driver)
    login.openUrl("https://admin-demo.nopcommerce.com/login")
    login.enter_username("admin@yourstore.com")
    login.enter_password("admin")
    login.clickOn_login()