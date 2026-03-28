import pytest
from core.driver_factory import get_driver
from config.env import BASE_URL
from utils.screenshot import take_screenshot


@pytest.fixture
def driver(request):

    driver = get_driver()
    driver.get(BASE_URL)

    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        take_screenshot(driver, request.node.name)

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)