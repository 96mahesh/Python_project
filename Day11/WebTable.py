from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/web-table-element.php")
rows = driver.find_elements(By.XPATH,"//table[@class='dataTable']//tbody//tr")
for loc in rows:
    rowsdata = loc.text
    #print(rowsdata)
print(len(rows))

col = driver.find_elements(By.XPATH,"//table[@class='dataTable']//thead//tr/th")
value = "Group"
column = 0
for i in range(0,len(col)):
    if(col[i].text.__eq__(value)):
        column=i

print(column)

singlecol = driver.find_elements(By.XPATH,"//table[@class='dataTable']//tbody//td")
for i in range(column,len(singlecol),5):
   coldata = singlecol[i].text
   print(coldata)

driver.close()