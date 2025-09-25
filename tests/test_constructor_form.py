import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_locators.locators import *


class TestStellarBurgersConstructorForm:

    @pytest.mark.parametrize("menu_button, header_locator, expected_text", [
        (MainPage.mn_sauces_button, MainPage.mn_h_sauces, "Соусы"),
        (MainPage.mn_filling_button, MainPage.mn_h_filling, "Начинки"),
        (MainPage.mn_ban_button, MainPage.mn_h_ban, "Булки"),
    ])
    def test_constructor_sections(self, login, menu_button, header_locator, expected_text):
        """Проверка разделов конструктора"""
        driver = login
        driver.find_element(*MainPage.mn_constructor_button).click()
        tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(menu_button)
        )
        if "tab_tab_type_current" not in tab.get_attribute("class"):
            tab.click()
        header = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(header_locator)
        )
        assert header.text == expected_text