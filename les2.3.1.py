from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    time.sleep(1)

    x_element = browser.find_element(By.ID, "input_value")

    x = x_element.text
    print(x)
    y = calc(x)
    print(y)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)


    button = browser.find_element_by_tag_name("button")
    button.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)

    # Проверяем, что смогли зарегистрироваться

finally:
    time.sleep(2)
    browser.quit()





