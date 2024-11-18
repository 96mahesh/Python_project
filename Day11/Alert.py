from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://letcode.in/alert")
driver.find_element(By.ID,"accept").click()
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
alert.accept()

driver.find_element(By.ID,"confirm").click()
confalert = driver.switch_to.alert
confralert_text = confalert.text
print(confralert_text)
alert.dismiss()

driver.find_element(By.ID,"prompt").click()
promptalert = driver.switch_to.alert
promptalert_text = promptalert.text
print(promptalert_text)
promptalert.send_keys("Mahesh")
promptalert.accept()

text_L = driver.find_element(By.ID,"myName")
print(text_L.text)


