import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome();
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.implicitly_wait(10)
ele = driver.find_element(By.XPATH,"//h3[text()='Widgets']")
time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView();",ele)
time.sleep(2)
ele.screenshot("screenShot.png")
time.sleep(2)
print(ele.screenshot_as_png)
print(ele.screenshot_as_base64)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//h3[text()='Widgets']""")))
