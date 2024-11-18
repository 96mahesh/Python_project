import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)

#maximize browser
driver.maximize_window()
driver.delete_all_cookies()
#launch browser
driver.get("https://playwright.dev/java/docs/intro")
time.sleep(3)
lnk_java = driver.find_element(By.XPATH,"//ul[@class='dropdown__menu']//preceding-sibling::a")

# Create an ActionChains object
actions = ActionChains(driver)
# Move the mouse cursor to the element
actions.move_to_element(lnk_java).perform()

#creating a empty list
string_list =[]
dd_options = driver.find_elements(By.XPATH,"//ul[@class='dropdown__menu']//li//a")
for option in dd_options:
    print(option.text) #adding text values to list
    string_list.append(option.text)
print(string_list)

for i in range(0,len(string_list)):
    time.sleep(1)
    lnk_java = driver.find_element(By.XPATH, "//ul[@class='dropdown__menu']//preceding-sibling::a")
    actions.move_to_element(lnk_java).perform()
    time.sleep(1)
    dd_option = driver.find_element(By.XPATH, "//ul[@class='dropdown__menu']//li//a[text()='"+string_list[i]+"']")
    dd_option.click()
    time.sleep(3)
    # i=i+1
    #i+=1