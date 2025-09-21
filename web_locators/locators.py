from selenium.webdriver.common.by import By


class MainPage:
    # кнопка "Личный кабинет"
    mp_profile_button = (By. XPATH, ".//p[text()='Личный кабинет']")
    
    # кнопка "Войти в аккаунт"
    mp_auth = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    
    # кнопка "Оформить заказ"
    mp_order_button = (By.XPATH, ".//button[text()='Оформить заказ']")
    
    # кнопка "Конструктор"
    mp_constructor_button = (By.XPATH, ".//p[text()='Конструктор']")
    
    # логотип
    mp_logo = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")
    
    # кнопка "Соусы"
    mp_sauces_button = (By.XPATH, ".//span[text()='Соусы']/parent::*")
    
    # заголовок "Соусы"
    mp_h_sauces = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']"
    
    # кнопка "Булки"
    mp_ban_button = (By.XPATH, ".//span[text()='Булки']/parent::*")
    
    # заголовок "Булки"
    mp_h_ban = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']"
    
    # кнопка "Начинки"
    mp_filling_button = (By.XPATH, ".//span[text()='Начинки']/parent::*")
    
    # заголовок "Начинки"
    mp_h_filling = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']"



class AuthLogin:
    # заголовок "Вход"
    al_login_text = (By.XPATH, ".//h2[text()='Вход']")
    
    # кнопка "Войти"
    al_login_button_any_forms = (By.XPATH, ".//button[text()='Войти']")
    
    # надпись "Войти" с ссылкой
    al_login_text_with_href = (By.XPATH, ".//a[text()='Войти']")   
    
    # ссылка "Зарегистрироваться"
    al_login_button = (By.CLASS_NAME, "Auth_link__1fOlj")
    
    # поле "email"
    al_email_field = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    
    # поле "password"
    al_password_field = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    
    al_element_with_login_text = (By.XPATH, ".//*[text() = 'Вход']")


class AuthRegistre:
    # поле "Имя"
    ar_name_field = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")
    
    # поле "Логин"
    ar_email_field = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    
    # поле "Пароль"
    ar_password_field = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    
    # кнопка "Зарегистрироваться"
    ar_register_button = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    
    # сообщение об ошибке
    ar_error_message = (By.XPATH, ".//p[contains(@class, 'input__error')]")
    
    # сообщение об ошибке
    ar_error_message_2 = (By.XPATH, ".//div[@class='Auth_login__3hAey']/p[@class='input__error text_type_main-default']")
    
    # ссылка "Зарегистрироваться"
    ar_login_button = (By.CLASS_NAME, "Auth_link__1fOlj")

#
class AuthPassword:
    # текст "Войти"
    ap_login_text_with_href = (By.XPATH, ".//a[text()='Войти']")


class LKProfile:
    # кнопка "Профиль"
    lk_logout_button = (By.XPATH, ".//button[text()='Выход']")
    
    # кнопка "История заказов"
    lk_info_message = (By.XPATH, ".//p[contains(text(),'персональные данные')]")
    
    # кнопка "Выходы"
    lk_history_shop_button = (By.XPATH, ".//li[@class='Account_listItem__35dAP']/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")