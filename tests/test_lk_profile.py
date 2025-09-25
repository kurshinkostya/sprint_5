from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_locators.locators import MainPage, LKProfile, AuthLogin
from data.urls import Urls
from data.data import ProfileData, ConstructorData, AuthData


class TestStellarBurgersProfileForm:

    def test_click_profile_button_open_profile_form(self, login):
        """Открыть личный кабинет"""
        driver = login
        driver.find_element(*MainPage.mn_profile_button).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(LKProfile.lk_info_message)
        )
        profile = driver.find_element(*LKProfile.lk_history_shop_button)
        assert driver.current_url == Urls.url_profile
        assert profile.text == ProfileData.history_orders_text

    def test_click_constructor_button_show_constructor_form(self, login):
        """Переход из личного кабинета в конструктор при нажатии кнопки 'Конструктор'"""
        driver = login
        driver.find_element(*MainPage.mn_profile_button).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(LKProfile.lk_info_message)
        )
        driver.find_element(*MainPage.mn_constructor_button).click()
        h1_tag = driver.find_element(*MainPage.mn_h1_constructor)
        assert h1_tag.text == ConstructorData.h1_text

    def test_click_logo_button_show_constructor_form(self, login):
        """Переход из личного кабинета в конструктор при нажатии на лого"""
        driver = login
        driver.find_element(*MainPage.mn_profile_button).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(LKProfile.lk_info_message)
        )
        driver.find_element(*MainPage.mn_logo).click()
        h1_tag = driver.find_element(*MainPage.mn_h1_constructor)
        assert h1_tag.text == ConstructorData.h1_text

    def test_click_logout_button_in_lk_open_login_form(self, login):
        """Выйти из аккаунта"""
        driver = login
        driver.find_element(*MainPage.mn_profile_button).click()
        WebDriverWait(driver, 8).until(
            EC.presence_of_element_located(LKProfile.lk_info_message)
        )
        driver.find_element(*LKProfile.lk_logout_button).click()
        WebDriverWait(driver, 8).until(
            EC.presence_of_element_located(AuthLogin.al_login_button_any_forms)
        )
        login_button = driver.find_element(*AuthLogin.al_element_with_login_text)
        assert driver.current_url == Urls.url_login
        assert login_button.text == AuthData.login_button_text