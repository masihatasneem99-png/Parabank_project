from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BillPayPage:

    billpay_link = (By.LINK_TEXT, "Bill Pay")
    payee_name = (By.NAME, "payee.name")
    address = (By.NAME, "payee.address.street")
    city = (By.NAME, "payee.address.city")
    state = (By.NAME, "payee.address.state")
    zip = (By.NAME, "payee.address.zipCode")
    phone = (By.NAME, "payee.phoneNumber")
    account = (By.NAME, "payee.accountNumber")
    verify_account = (By.NAME, "verifyAccount")
    amount = (By.NAME, "amount")
    send_payment = (By.CSS_SELECTOR, "input[value='Send Payment']")
    success = (By.CSS_SELECTOR, "#billpayResult .title")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_bill_pay(self):
        self.wait.until(EC.element_to_be_clickable(self.billpay_link)).click()

    def pay_bill(self):

        self.wait.until(EC.visibility_of_element_located(self.payee_name)).send_keys("Electricity Board")

        self.driver.find_element(*self.address).send_keys("nlg road")
        self.driver.find_element(*self.city).send_keys("Hyderabad")
        self.driver.find_element(*self.state).send_keys("MA")
        self.driver.find_element(*self.zip).send_keys("508001")
        self.driver.find_element(*self.phone).send_keys("1234567890")

        self.driver.find_element(*self.account).send_keys("987654")
        self.driver.find_element(*self.verify_account).send_keys("987654")

        self.driver.find_element(*self.amount).send_keys("45")

        self.driver.find_element(*self.send_payment).click()

    def payment_success(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.success)
        ).text