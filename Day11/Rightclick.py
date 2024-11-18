import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
mobile_L = driver.find_element(By.XPATH,"//a[text()='Mobiles']")
action = ActionChains(driver)
action.context_click(mobile_L).click().perform()
for i in range(1,5):
    time.sleep(2)
    pyautogui.press('down')

pyautogui.press('enter')
time.sleep(5)