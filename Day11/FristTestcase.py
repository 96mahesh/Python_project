# Example 1
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome();
driver.get("https://admin-demo.nopcommerce.com/login")
ele = driver.find_element(By.NAME, 'Email')
ele.clear()
ele.send_keys("admin@yourstore.com")

pele = driver.find_element(By.NAME,'Password')
pele.clear()
pele.send_keys('admin')

driver.find_element(By.XPATH,"//button[text()='Log in']").click()
act_title = driver.title
print(act_title)
exp_title = 'Dashboard / nopCommerce administration'

if act_title==exp_title:
    print("Test case will pass")
else :
    print("Test case will not pass")

driver.close()


