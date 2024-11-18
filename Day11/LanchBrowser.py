from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)
highlight_script = """
    var element = arguments[0];
    var original_style = element.getAttribute('style');
    element.setAttribute('style', original_style + '; background: yellow; border: 2px solid red;');
    setTimeout(function(){
        element.setAttribute('style', original_style);
    }, 2000);
"""
email_field = driver.find_element(By.XPATH,"//input[@name='email']")
pass_field = driver.find_element(By.XPATH,"//input[@name='pass']")
login_btn = driver.find_element(By.XPATH,"//button[@type='submit']")
driver.execute_script(highlight_script,email_field)
email_field.send_keys('7842358565')
driver.execute_script(highlight_script,pass_field)
pass_field.send_keys('swapna')
driver.execute_script(highlight_script,login_btn)
login_btn.click()
#print(driver.current_url())
driver.close()


