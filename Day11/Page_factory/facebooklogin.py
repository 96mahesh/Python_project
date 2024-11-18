from seleniumpagefactory import PageFactory


class FbLoginpage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'username': ('ID', "email"),
        'password': ('ID', "pass"),
        'login': ('XPATH', "//button[text()='Log in']")
    }

    def enter_uesrname(self, user):
        self.username.set_text(user)


    def enter_password(self, password):
        self.password.set_text(password)

    def get_element_text(self):
        data = self.login.get_text()
        print(data)

    def click_on_login(self):
        self.login.click()


