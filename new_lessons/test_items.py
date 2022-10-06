import time

from selenium.webdriver.common.by import By


def test_button_buy_is_displayed(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(2)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").is_displayed(), "This button is not on this page"



