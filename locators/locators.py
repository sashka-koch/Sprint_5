from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON_HEADER = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGO = (By.CSS_SELECTOR, "a[href='/']")


class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class ProfilePageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")


class ConstructorPageLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    TOPPINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
