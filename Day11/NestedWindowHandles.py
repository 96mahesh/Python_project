import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://letcode.in/windows")
driver.find_element(By.ID,"multi").click()
time.sleep(2)
allwin = driver.window_handles
for win in allwin:
    if win != (driver.current_window_handle):
        driver.switch_to.window(win)
        urls = driver.current_url;
        print(urls)
        if urls.__eq__("https://letcode.in/dropdowns"):
            driver.maximize_window()
            dropdown = driver.find_element(By.ID,"fruits")
            select = Select(dropdown)
            select.select_by_index(5)
            time.sleep(2)
           # driver.close()
        else :
            time.sleep(2)
            driver.find_element(By.Id,"accept").click()
            alert = driver.switch_to.alert
            alert_text = alert.text
            print("Alert text:", alert_text)
            alert.accept()




