from selenium.webdriver.common.by import By


class MainPage:
    mn_profile_button = (By.XPATH, ".//p[text()='Личный Кабинет']")
    mn_auth = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    mn_order_button = (By.XPATH, ".//button[text()='Оформить заказ']")
    mn_constructor_button = (By.XPATH, ".//p[text()='Конструктор']")
    mn_logo = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")

    mn_sauces_button = (By.XPATH, ".//span[text()='Соусы']/parent::*")
    mn_h_sauces = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']"

    mn_ban_button = (By.XPATH, ".//span[text()='Булки']/parent::*")
    mn_h_ban = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']"

    mn_filling_button = (By.XPATH, ".//span[text()='Начинки']/parent::*")
    mn_h_filling = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']"


class AuthLogin:
    al_login_text = (By.XPATH