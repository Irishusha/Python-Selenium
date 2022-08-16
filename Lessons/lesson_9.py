
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time



link = " http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)



    num1 = browser.find_element(By.ID, "num1")
    x = num1.text
    num2 = browser.find_element(By.ID, "num2")
    y = num2.text
    sum =int(x)+int(y)
    sum1=str(sum)
    print(sum1)
   # select = browser.find_element(By.CLASS_NAME, "custom-select").click()
    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(sum1)
    #select.select_by_visible_text('10')

    button = browser.find_element(By.CLASS_NAME, "btn-default")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла