
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome();
driver.get("https://www.amazon.in")

driver.maximize_window()
driver.implicitly_wait(10)
dropdown = driver.find_element(By.ID,"searchDropdownBox")

select = Select(dropdown)
alloptions = select.options
for value in alloptions:
    allvalues = value.text
    print(allvalues)
select.select_by_index(3)

time.sleep(2)
select.select_by_value("search-alias=baby")
time.sleep(2)
select.select_by_visible_text("Home & Kitchen")
driver.close()

