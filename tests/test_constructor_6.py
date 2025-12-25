import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators
from pages.urls import URLs


class TestConstructor:
    
    @pytest.mark.parametrize("section, active_locator, need_initial_click", [
        (MainPageLocators.BUNS_SECTION, MainPageLocators.ACTIVE_BUNS_SECTION, True),
        (MainPageLocators.SAUCES_SECTION, MainPageLocators.ACTIVE_SAUCES_SECTION, False),
        (MainPageLocators.TOPPINGS_SECTION, MainPageLocators.ACTIVE_TOPPINGS_SECTION, False)
    ])
    def test_go_to_section(self, driver, section, active_locator, need_initial_click):
        driver.get(URLs.MAIN_URL)
        
        if need_initial_click:
            driver.find_element(*MainPageLocators.SAUCES_SECTION).click()
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(MainPageLocators.ACTIVE_SAUCES_SECTION)
            )
        
        driver.find_element(*section).click()
        active_tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(active_locator)
        )
        assert active_tab.is_displayed()