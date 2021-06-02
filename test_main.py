import os
import time

import allure
from selenium import webdriver

@allure.title("First test")
def test_01():
    driver = webdriver.Firefox()
    # driver.get("https://stepik.org/lesson/25969/step/12")
    try:
        driver.get(os.environ["URL_ENV"])
    except KeyError:
        driver.get("https://www.google.com/")
    time.sleep(7)
    textarea = driver.find_element_by_css_selector(".textarea")
    textarea.send_keys("get()")
    time.sleep(5)
    submit_button = driver.find_element_by_css_selector(".submit-submission")
    submit_button.click()
    time.sleep(5)
    driver.quit()

#