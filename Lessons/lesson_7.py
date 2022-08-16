def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y=calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    optional_robot = browser.find_element(By.ID,"robotCheckbox")
    optional_robot.click()
    optional_robot_best = browser.find_element(By.ID, "robotsRule")
    optional_robot_best.click()
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла