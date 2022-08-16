from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    element_x = browser.find_element(By.ID, "input_value")
    x = element_x.text
    print(x)
    print(calc(x))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))
    button2 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
