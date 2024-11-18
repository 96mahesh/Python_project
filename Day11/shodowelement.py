from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def expand_shadow_element(element):
  shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root

driver.get("chrome://settings")
root1 = driver.find_element(By.TAG_NAME, 'settings-ui');
shadow_root1 = expand_shadow_element(root1)

root2 = shadow_root1.find_element(By.CSS_SELECTOR, '[page-name="Settings"]')
shadow_root2 = expand_shadow_element(root2)

root3 = shadow_root2.find_element(By.ID, 'search')
shadow_root3 = expand_shadow_element(root3)

search_button = shadow_root3.find_element(By.ID, "searchTerm")
search_button.click()

text_area = shadow_root3.find_element(By.ID, 'searchInput')
text_area.send_keys("content settings")

root0 = shadow_root1.find_element, (By.ID, 'main')
shadow_root0_s = expand_shadow_element(root0)


root1_p = shadow_root0_s.find_element(By.CSS_SELECTOR, 'settings-basic-page')
shadow_root1_p = expand_shadow_element(root1_p)


root1_s = shadow_root1_p.find_element(By.CSS_SELECTOR, 'settings-privacy-page')
shadow_root1_s = expand_shadow_element(root1_s)

content_settings_div = shadow_root1_s.find_element(By.CSS_SELECTOR, '#site-settings-subpage-trigger')
content_settings = content_settings_div.find_element(By.CSS_SELECTOR, "button")
content_settings.click()