import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

answer = math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('nomer', ["236895", "236896"])
def test_guest_should_see_login_link(browser, nomer):
    link = f"https://stepik.org/lesson/{nomer}/step/1/"
    browser.get(link)
    finder = browser.find_element(By.CLASS_NAME, "ember-text-area")
    finder.send_keys(answer)
    time.sleep(5)