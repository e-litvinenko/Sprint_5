import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import (
    MainPageLocators, 
    PersonalAccountLocators, 
    LoginPageLocators
)
from pages.urls import URLs

class TestNavigationToConstructor:
    
    def test_navigation_from_account_to_constructor(self, driver, login):
        driver.get(URLs.LOGIN_URL)
        
        login(driver)
        
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(PersonalAccountLocators.PROFILE_LINK)
        )
        
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.MAIN_HEADER)
        )
        
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(PersonalAccountLocators.PROFILE_LINK)
        )
        
        driver.find_element(*MainPageLocators.LOGO_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.MAIN_HEADER)
        )