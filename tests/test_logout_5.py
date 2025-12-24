import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import (
    MainPageLocators, 
    LoginPageLocators, 
    PersonalAccountLocators,
    TestData  # Важно: добавить импорт TestData
)


def test_logout_from_account(driver, login):
    """5. Проверь выход по кнопке «Выйти» в личном кабинете"""
    
    # 1. Переходим на страницу входа (чтобы фикстура login работала корректно)
    driver.get(TestData.LOGIN_URL)
    
    # 2. Логинимся с помощью фикстуры (передаем driver как аргумент)
    login(driver)
    
    # 3. Переходим в личный кабинет
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    
    # Ждём загрузки личного кабинета
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(PersonalAccountLocators.PROFILE_LINK)
    )
    
    # 4. Находим и нажимаем кнопку выхода
    logout_button = driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON)
    logout_button.click()
    
    # 5. Проверяем, что произошёл выход - видим форму входа
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginPageLocators.LOGIN_HEADER)
    )
    
    driver.quit()