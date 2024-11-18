from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.execute_script("window.open('https://www.example.com', 'new_window')")
time.sleep(2)
window_handles = driver.window_handles
for handle in window_handles:
    if handle != driver.current_window_handle:
        driver.switch_to.window(handle)
        break
print(driver.current_url)  # Print the URL of the new window
driver.close()
driver.switch_to.window(window_handles[0])
print(driver.current_url)
driver.quit()
