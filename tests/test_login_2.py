import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators, LoginPageLocators, TestData


class TestLogin:
    
    def test_login_from_main_page_button(self, driver, login):
        """2.1. Вход по кнопке «Войти в аккаунт» на главной"""
        driver.get(TestData.MAIN_URL)
        
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        
        login(driver)
        
        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
        
        driver.quit()  # Просто в конце теста
    
    def test_login_from_personal_account_button(self, driver, login):
        """2.2. Вход через кнопку «Личный кабинет»"""
        driver.get(TestData.MAIN_URL)
        
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        
        login(driver)
        
        assert WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
        
        driver.quit()
    
    def test_login_from_registration_form(self, driver, login):
        """2.3. Вход через кнопку в форме регистрации"""
        driver.get(TestData.REGISTER_URL)
        
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
        
        driver.quit()
    
    def test_login_from_password_recovery_form(self, driver, login):
        """2.4. Вход через кнопку в форме восстановления пароля"""
        driver.get(TestData.FORGOT_PASSWORD_URL)
        
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
        
        driver.quit()