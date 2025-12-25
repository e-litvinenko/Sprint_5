import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators, LoginPageLocators
from pages.urls import URLs


class TestLogin:
    
    def test_login_from_main_page_button(self, driver, login):
        driver.get(URLs.MAIN_URL)
        
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        
        login(driver)
        
        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_login_from_personal_account_button(self, driver, login):
        driver.get(URLs.MAIN_URL)
        
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        
        login(driver)
        
        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_login_from_registration_form(self, driver, login):
        driver.get(URLs.REGISTER_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        
        login(driver)
        
        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_login_from_password_recovery_form(self, driver, login):
        driver.get(URLs.FORGOT_PASSWORD_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        
        login(driver)
        
        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()