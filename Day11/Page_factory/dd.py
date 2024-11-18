from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from seleniumpagefactory.Pagefactory import PageFactory
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class ExamplePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    # Define locators using PageFactory
    locators = {
        "dropdown": ('XPATH', "//select[@id='searchDropdownBox']")
    }

    # Method to select an option from the dropdown
    def select_dropdown_option(self, visible_text):
        # Using the PageFactory locator for the dropdown
        # dropdown_element = WebDriverWait(self.driver, 15).until(
        #     EC.visibility_of_element_located(self.locators['dropdown'])
        # )
        dropdown_element = self.dropdown
        print(type(dropdown_element))
        select = Select(dropdown_element)
        select.select_by_visible_text(visible_text)

# Usage Example
if __name__ == "__main__":
    driver = webdriver.Chrome()  # Initialize WebDriver
    driver.get("https://www.amazon.in")  # Navigate to the webpage

    # Instantiate the Page Object
    example_page = ExamplePage(driver)

    # Use the method defined in the Page Object to interact with the dropdown
    example_page.select_dropdown_option("Books")

    driver.quit()  # Close the browser
