from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)
    button = browser.find_element(By.ID, 'book')
    price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    button.click()
    element_x = browser.find_element(By.ID, "input_value")
    x = element_x.text
    print(x)
    print(calc(x))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))
    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
