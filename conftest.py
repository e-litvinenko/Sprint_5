import pytest
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

@pytest.fixture
def random_email():
    return f"test_user_37_{random.randint(100, 999)}@yandex.ru"

@pytest.fixture
def login():
    def _login(driver):
        from pages.locators import TestData, LoginPageLocators, MainPageLocators
        
        wait = WebDriverWait(driver, 10)
        
        email_field = wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        email_field.send_keys(TestData.TEST_EMAIL)
        
        password_field = wait.until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT))
        password_field.send_keys(TestData.TEST_PASSWORD)
        
        login_button = wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_SUBMIT_BUTTON))
        login_button.click()
        
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
    
    return _login