from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (Chrome in this case)
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode if you don't need a GUI
# service = Service('/path/to/chromedriver')  # Update this path to your chromedriver executable
# driver = webdriver.Chrome(service=service, options=chrome_options)

driver = webdriver.Chrome()

# Navigate to Facebook's login page
driver.get("https://www.facebook.com/")

# Define input data with double quotes
username = '"7842358565"'
password = 'your_password_with_"quotes"'

# Locate the username and password fields
username_field = WebDriverWait(driver, 10).until(

    EC.presence_of_element_located((By.ID, "email"))
)
password_field = driver.find_element(By.ID, "pass")

# Send the input data
username_field.send_keys(username)
password_field.send_keys(password)

# Submit the login form
password_field.send_keys(Keys.RETURN)  # This simulates pressing the Enter key

# Optionally, wait for some time to observe the result
WebDriverWait(driver, 10).until(
    EC.title_contains("Facebook")
)

# Close the browser
driver.quit()
