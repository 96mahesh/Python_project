import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://letcode.in/dropdowns")

dropdown = driver.find_element(By.ID,"superheros")
select = Select(dropdown)
alloption = select.options
text_List = []
for opt in alloption:
    text_List.append(opt.text)
print(text_List)
print(len(text_List))

time.sleep(2)
for selopt in text_List:
    if selopt.__eq__("Batman") or selopt.__eq__("Black Panther"):
        select.select_by_visible_text(selopt)

selectd_options = select.all_selected_options;
select_text = []
for e in selectd_options:
    allselectopt = e.text
    select_text.append(allselectopt)
print(select_text)
print(len(select_text))

print("Non selectd Options")
nonselectOpt = []
for opt in alloption:
    if(not(opt.is_selected())):
        nonselectOpt.append(opt.text)

print(nonselectOpt)
print(len(nonselectOpt))