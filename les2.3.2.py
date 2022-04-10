from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID, "input_value")

    x = x_element.text
    y = calc(x)
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





