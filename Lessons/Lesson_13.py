from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.XPATH , "//input[@name='firstname']")
    input1.send_keys("Irisha")
    input2 = browser.find_element(By.XPATH , "//input[@name='lastname']")
    input2.send_keys("Testing")
    input3 = browser.find_element(By.XPATH , "//input[@name='email']")
    input3.send_keys("Irisha@mail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    input4 = browser.find_element(By.ID, "file")
    input4.send_keys(file_path)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
