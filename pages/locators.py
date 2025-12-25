"""
Локаторы для тестов проекта Sprint_5 - Stellar Burgers
"""
from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""
    
    # Шапка
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")  # Кнопка "Конструктор"
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'logo')]")  # Логотип Stellar Burgers
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")  # Кнопка "Личный Кабинет"
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"
    
    # Кнопки входа/регистрации
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной
    
    # Раздел конструктора
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")  # Вкладка "Булки"
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")  # Вкладка "Соусы"
    TOPPINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")  # Вкладка "Начинки"
    
    # Индикаторы активных разделов
    ACTIVE_BUNS_SECTION = (By.XPATH, "//div[contains(@class, 'current')]//span[text()='Булки']")  # Активная вкладка "Булки"
    ACTIVE_SAUCES_SECTION = (By.XPATH, "//div[contains(@class, 'current')]//span[text()='Соусы']")  # Активная вкладка "Соусы"
    ACTIVE_TOPPINGS_SECTION = (By.XPATH, "//div[contains(@class, 'current')]//span[text()='Начинки']")  # Активная вкладка "Начинки"
    
    # Заголовки
    MAIN_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок "Соберите бургер"


class LoginPageLocators:
    """Локаторы страницы входа"""
    
    # Заголовки
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")  # Заголовок "Вход"
    
    # Поля формы
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")  # Поле для ввода email
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")  # Поле для ввода пароля
    
    # Кнопки
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"
    
    # Ссылки
    LOGIN_LINK = (By.LINK_TEXT, "Войти")  # Ссылка "Войти" (используется в формах регистрации и восстановления пароля)


class RegistrationPageLocators:
    """Локаторы страницы регистрации"""
    
    # Заголовки
    REGISTRATION_HEADER = (By.XPATH, "//h2[text()='Регистрация']")  # Заголовок "Регистрация"
    
    # Поля формы
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле "Имя"
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле "Email"
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле "Пароль"
    
    # Кнопки
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    
    # Ошибки
    PASSWORD_ERROR = (By.CLASS_NAME, "input__error")  # Ошибка валидации пароля


class PersonalAccountLocators:
    """Локаторы личного кабинета"""
    
    # Навигация
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")  # Ссылка "Профиль"
    
    # Кнопки
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти' or text()='Выход']")  # Кнопка выхода из аккаунта