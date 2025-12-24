import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators, LoginPageLocators, TestData


def test_click_personal_account_button(driver):
    driver.get(TestData.MAIN_URL)
    
    personal_account_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    )
    personal_account_link.click()
    
    WebDriverWait(driver, 10).until(EC.url_to_be(TestData.LOGIN_URL))
    
    login_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginPageLocators.LOGIN_HEADER)
    )
    
    assert login_header.is_displayed()
    driver.quit()