import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('nomer', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, nomer):
    link = f"https://stepik.org/lesson/{nomer}/step/1/"
    browser.get(link)
  #  answer == 0
    answer = math.log(int(time.time() + 39.5))
    finder = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "ember-text-area")))
    finder.send_keys(str(answer))
    button = browser.find_element(By.CLASS_NAME, "submit-submission")
    button.click()
    time.sleep(3)
    hint = browser.find_element(By.CLASS_NAME, "smart-hints__feedback")

    assert hint.text == "Correct!"
    time.sleep(2)