import os
from datetime import datetime


def take_screenshot(driver, name="screenshot"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder = "reports/screenshots_new"

    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = f"{folder}/{name}_{timestamp}.png"
    driver.save_screenshot(file_path)

    return file_path