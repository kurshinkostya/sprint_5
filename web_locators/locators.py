from selenium.webdriver.common.by import By

    
class MainPage:
    # кнопки хедера
    mn_profile_button = (By.XPATH, ".//p[text()='Личный Кабинет']")
    mn_auth = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    mn_order_button = (By.XPATH, ".//button[text()='Оформить заказ']")
    mn_constructor_button = (By.XPATH, ".//p[text()='Конструктор']")
    mn_logo = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")

    # разделы конструктора
    mn_sauces_button = (By.XPATH, ".//span[text()='Соусы']/parent::*")
    mn_h_sauces = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']")

    mn_ban_button = (By.XPATH, ".//span[text()='Булки']/parent::*")
    mn_h_ban = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']")

    mn_filling_button = (By.XPATH, ".//span[text()='Начинки']/parent::*")
    mn_h_filling = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']")

    # общие элементы конструктора
    mn_h1_constructor = (By.XPATH, ".//h1[text()='Соберите бургер']")
    mn_ingredient_list = (By.XPATH, ".//section[contains(@class,'BurgerIngredients_ingredients__menuContainer')]")
    mn_ingredient_card = (By.XPATH, ".//div[contains(@class, 'BurgerIngredient_ingredient__')]")
    mn_basket_constructor = (By.XPATH, ".//section[contains(@class,'BurgerConstructor_basket__')]")


class AuthLogin:
    al_login_text = (By.XPATH, ".//h2[text()='Вход']")
    al_login_button_any_forms = (By.XPATH, ".//button[text()='Войти']")
    
    # ссылка "Войти"
    al_login_text_with_href = (By.XPATH, ".//a[text()='Войти']")  
    al_login_button = (By.CLASS_NAME, "Auth_link__1fOlj")
    al_email_field = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    al_password_field = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    al_element_with_login_text = (By.XPATH, ".//*[text() = 'Вход']")
    al_register_href = (By.XPATH, ".//a[text()='Зарегистрироваться']")
    al_restore_password_href = (By.XPATH, ".//a[text()='Восстановить пароль']")


class AuthRegistre:
    ar_register_text = (By.XPATH, ".//h2[text()='Регистрация']")
    ar_name_field = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")
    ar_email_field = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    ar_password_field = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    ar_register_button = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    ar_error_message = (By.XPATH, ".//p[contains(@class, 'input__error')]")
    ar_error_message_2 = (By.XPATH, ".//div[@class='Auth_login__3hAey']/p[@class='input__error text_type_main-default']")
    ar_login_button = (By.CLASS_NAME, "Auth_link__1fOlj")


class AuthPassword:
    ap_restore_text = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    ap_email_field = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text']")
    ap_restore_button = (By.XPATH, ".//button[text()='Восстановить']")
    ap_login_text_with_href = (By.XPATH, ".//a[text()='Войти']")


class LKProfile:
    lk_profile_header = (By.XPATH, ".//h2[text()='Профиль']")
    lk_logout_button = (By.XPATH, ".//button[text()='Выход']")
    lk_info_message = (By.XPATH, ".//p[contains(text(),'персональные данные')]")
    lk_history_shop_button = (By.XPATH, ".//li[@class='Account_listItem__35dAP']/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")
    lk_history_tab_active = (By.XPATH, ".//a[contains(@class, 'Account_link__') and contains(@class, 'active')]")
    lk_orders_list = (By.XPATH, ".//ul[contains(@class,'OrderHistory_list__')]")