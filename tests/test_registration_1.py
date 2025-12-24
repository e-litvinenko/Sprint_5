import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import RegistrationPageLocators, LoginPageLocators, TestData  # ← Добавить TestData

class TestRegistration:
    
    def test_successful_registration(self, driver, random_email):
        """1.1. Успешная регистрация - используем фикстуру random_email"""
        driver.get(TestData.REGISTER_URL)  # ← Исправить хардкод
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.REGISTRATION_HEADER)
        )
        
        # Заполняем форму с данными из фикстур
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Екатерина")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(random_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("123456")
        
        # Регистрируемся
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        # Проверяем успешность
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        
        login_header = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_HEADER)
        )
        assert login_header.is_displayed()
        driver.quit()
    
    def test_registration_invalid_password(self, driver, random_email):
        """1.2. Ошибка для некорректного пароля"""
        driver.get(TestData.REGISTER_URL)  # ← Исправить хардкод
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.REGISTRATION_HEADER)
        )
        
        # Используем random_email из фикстуры
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Екатерина")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(random_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("12345")  # короткий пароль
        
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        # Проверяем ошибку
        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR)
        )
        assert error.is_displayed()
        driver.quit()