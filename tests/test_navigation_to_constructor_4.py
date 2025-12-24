import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import (
    MainPageLocators, 
    PersonalAccountLocators, 
    LoginPageLocators,
    TestData
)

def test_navigation_from_account_to_constructor(driver, login):  # ← Добавить login в параметры
    """4. Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers"""
    
    # 1. Переходим на страницу логина
    driver.get(TestData.LOGIN_URL)
    
    # 2. Логинимся с помощью фикстуры (вместо прямого кода)
    login(driver)  # ← Всего одна строка вместо 8!
    
    # 3. Переходим в личный кабинет
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    
    # Ждём загрузки личного кабинета
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(PersonalAccountLocators.PROFILE_LINK)
    )
    
    # 4. ПРОВЕРКА 1: Переход по клику на «Конструктор»
    driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
    
    # Проверяем, что вернулись на главную
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPageLocators.MAIN_HEADER)
    )
    
    # 5. Снова переходим в личный кабинет для второй проверки
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(PersonalAccountLocators.PROFILE_LINK)
    )
    
    # 6. ПРОВЕРКА 2: Переход по клику на логотип Stellar Burgers
    driver.find_element(*MainPageLocators.LOGO_BUTTON).click()
    
    # Проверяем, что снова на главной
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPageLocators.MAIN_HEADER)
    )
    
    driver.quit()