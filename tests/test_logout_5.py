import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import (
    MainPageLocators, 
    LoginPageLocators, 
    PersonalAccountLocators,
    TestData
)


def test_logout_from_account(driver, login):
    driver.get(TestData.LOGIN_URL)
    
    login(driver)
    
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(PersonalAccountLocators.PROFILE_LINK)
    )
    
    logout_button = driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON)
    logout_button.click()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginPageLocators.LOGIN_HEADER)
    )
    
    driver.quit()