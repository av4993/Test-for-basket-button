import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_language_user(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button1 = len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket"))
    
    assert button1 > 0, "Кнопка 'Добавить в корзину' не найдена"
    
