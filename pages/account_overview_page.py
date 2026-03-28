from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountOverviewPage:

    account_table = (By.ID, "accountTable")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_accounts_loaded(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.account_table)
        ).is_displayed()