from pages.login_page import LoginPage
from utils.screenshot import take_screenshot


def test_valid_login(driver):

    login = LoginPage(driver)
    take_screenshot(driver, "login_page")

    login.login("john", "demo")

    take_screenshot(driver, "login")
    assert "overview" in driver.current_url