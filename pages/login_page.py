from selenium.webdriver.common.by import By


class LoginPage:

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_btn = (By.CSS_SELECTOR, "input[value='Log In']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()