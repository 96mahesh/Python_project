import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window();
driver.find_element(By.XPATH,"//textarea[@name='q']").send_keys("Mahesh")
time.sleep(2)
elements = driver.find_elements(By.XPATH,"//div[@class='OBMEnb']//div[@class='wM6W7d']")








