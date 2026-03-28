from pages.login_page import LoginPage


def test_valid_login(driver):

    login = LoginPage(driver)

    login.login("Masiha", "1234")

    assert "overview" in driver.current_url