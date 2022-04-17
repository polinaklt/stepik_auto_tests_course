import math
from selenium import webdriver
import time

driver = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver.get("http://suninjuly.github.io/alert_accept.html")

iwantjorney_button = driver.find_element_by_css_selector(".btn.btn-primary")
iwantjorney_button.click()

confirm = driver.switch_to.alert
confirm.accept()

x_element = driver.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)

textarea = driver.find_element_by_css_selector("#answer")
textarea.send_keys(y)

submit_button = driver.find_element_by_css_selector(".btn.btn-primary")
submit_button.click()
time.sleep(30)

driver.quit()
