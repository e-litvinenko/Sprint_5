import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators, TestData


class TestConstructor:
    
    def test_go_to_buns_section(self, driver):
        """6.1. Переход к разделу «Булки»"""
        driver.get(TestData.MAIN_URL)
        
        driver.find_element(*MainPageLocators.SAUCES_SECTION).click()
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(MainPageLocators.ACTIVE_SAUCES_SECTION)
        )
        
        driver.find_element(*MainPageLocators.BUNS_SECTION).click()
        buns_tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(MainPageLocators.ACTIVE_BUNS_SECTION)
        )
        assert buns_tab.is_displayed()
        driver.quit()
    
    def test_go_to_sauces_section(self, driver):
        """6.2. Переход к разделу «Соусы»"""
        driver.get(TestData.MAIN_URL)
        
        driver.find_element(*MainPageLocators.SAUCES_SECTION).click()
        sauces_tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(MainPageLocators.ACTIVE_SAUCES_SECTION)
        )
        assert sauces_tab.is_displayed()
        driver.quit()
    
    def test_go_to_toppings_section(self, driver):
        """6.3. Переход к разделу «Начинки»"""
        driver.get(TestData.MAIN_URL)
        
        driver.find_element(*MainPageLocators.TOPPINGS_SECTION).click()
        toppings_tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(MainPageLocators.ACTIVE_TOPPINGS_SECTION)
        )
        assert toppings_tab.is_displayed()
        driver.quit()