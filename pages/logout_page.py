from selenium.webdriver.common.by import By


class LogoutPage:

    logout_link = (By.LINK_TEXT, "Log Out")

    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.find_element(*self.logout_link).click()