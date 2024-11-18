import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
mouse_move = driver.find_element(By.XPATH,"//span[text()='Account & Lists']")
action = ActionChains(driver)
action.move_to_element(mouse_move).perform()
time.sleep(2)
driver.find_element(By.XPATH,"//span[text()='Discover Your Style']").click()
