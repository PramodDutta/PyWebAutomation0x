# Page Locators
# Page Actions
# Webdriver - Init
# Custom Functions
# No Assertion here ( They are not Test cases)
# Page Class

from selenium.webdriver.common.by import By


class LoginPage():

    # Webdriver - Init
    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    username = (By.ID, "login-username")
    password = (By.NAME, "password")
    submit_button = (By.XPATH, "//button[@id='js-login-btn']")
    error_message = (By.CSS_SELECTOR, "#js-notification-box-msg")

    # forgot pass, start a free trial,..... We skip as of now - u

    # Return a Webelement ->  username
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    # Page Actions
    def login_to_vwo(self, user, pwd):
        self.get_username().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()
        # get username and send keys - email
        # get password and send keys - email
        # click the submit button and navigate to dashboard Page

