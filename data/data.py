import random


class PersonData:
    user_name = 'kostya'
    login = 'kostya_k_30_666@ya.ru'
    password = '315920'
    
# тестовые данные и ожидаемые ответы

class ProfileData:
    history_orders_text = "История заказов"

class ConstructorData:
    h1_text = "Соберите бургер"

class AuthData:
    login_button_text = "Вход"

# функция генератора логина
class ValidData:
    user_name = 'Test test'
    login = f"Test_test{random.randint(10, 999)}@ya.ru"
    password = f"{random.randint(100, 999)}{random.randint(100, 999)}"
