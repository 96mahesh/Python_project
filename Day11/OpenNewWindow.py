from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome();
driver.get("https://www.google.com")
print(driver.title);
driver.execute_script("window.open('about:blank', 'new_window')")
driver.switch_to.window("new_window")
driver.get("https://www.facebook.com")
print(driver.title);

driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH,"//textarea[@name='q']").send_keys("Ram")
driver.quit()