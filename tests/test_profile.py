TEST_EMAIL = "aleksandra_kochenkova_44_999@yandex.com"
TEST_PASSWORD = "123456"


from locators.locators import (
    MainPageLocators,
    LoginPageLocators,
    ProfilePageLocators,
    ConstructorPageLocators
)


def login(driver):
    driver.get("https://stellarburgers.education-services.ru/login")
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()


def test_go_to_personal_account(driver):
    login(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    assert driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).is_displayed()


def test_go_from_personal_account_to_constructor_by_button(driver):
    login(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*ProfilePageLocators.CONSTRUCTOR_LINK).click()

    assert driver.find_element(*ConstructorPageLocators.BUNS_TAB).is_displayed()


def test_go_from_personal_account_to_constructor_by_logo(driver):
    login(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*MainPageLocators.LOGO).click()

    assert driver.find_element(*ConstructorPageLocators.BUNS_TAB).is_displayed()


def test_logout_from_personal_account(driver):
    login(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()

    assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()
