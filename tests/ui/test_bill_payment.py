from pages.login_page import LoginPage
from pages.account_overview_page import AccountOverviewPage
from pages.transfer_funds_page import TransferFundsPage
from pages.bill_pay_page import BillPayPage
from pages.logout_page import LogoutPage
from utils.screenshot import take_screenshot


def test_parabank_e2e_flow(driver):

    login = LoginPage(driver)
    login.login("john", "demo")

    overview = AccountOverviewPage(driver)
    assert overview.verify_accounts_loaded()

    bill = BillPayPage(driver)
    bill.open_bill_pay()
    bill.pay_bill()
    take_screenshot(driver, "bill_pay")
    assert "Bill Payment Complete" in bill.payment_success()

    logout = LogoutPage(driver)
    logout.logout()

    assert "index.htm" in driver.current_url