import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(30)

url = driver.current_url;
print(url)
el = driver.find_element(By.XPATH,"//textarea[@name='q']")
# el.send_keys("Mahesh",Keys.ARROW_DOWN,Keys.ENTER)
el.send_keys("Mahesh")
time.sleep(3)
for i in range(0,5):
    time.sleep(2)
    el.send_keys(Keys.ARROW_DOWN)
el.send_keys(Keys.ENTER)
