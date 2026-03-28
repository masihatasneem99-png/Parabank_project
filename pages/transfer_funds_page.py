from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class TransferFundsPage:
    transfer_link = (By.LINK_TEXT, "Transfer Funds")
    amount = (By.ID, "amount")
    transfer_btn = (By.CSS_SELECTOR, "input[value='Transfer']")

    fromAccount = (By.XPATH, "//select[@id='fromAccountId']")
    toAccount = (By.XPATH, "//select[@id='toAccountId']")

    success_msg = (By.XPATH, "//h1[text()='Transfer Complete!']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_transfer(self):
        self.wait.until(EC.element_to_be_clickable(self.transfer_link)).click()

    def select_account(self, locator, value):
        element = self.wait.until(EC.presence_of_element_located(locator))
        select = Select(element)

        # wait until options are loaded
        self.wait.until(lambda d: len(select.options) > 1)

        found = False
        for option in select.options:
            if option.text.strip() == value or option.get_attribute("value") == value:
                option.click()
                found = True
                break

        if not found:
            raise Exception(f"Value '{value}' not found in dropdown {locator}")

    def transfer_money(self, amt, from_acc, to_acc):
        # enter amount
        self.wait.until(EC.visibility_of_element_located(self.amount)).send_keys(amt)

        self.select_account(self.fromAccount, from_acc)

        self.select_account(self.toAccount, to_acc)

        # click transfer
        self.wait.until(EC.element_to_be_clickable(self.transfer_btn)).click()

    def transfer_success(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.success_msg)
        ).text