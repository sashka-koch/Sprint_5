from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


TEST_EMAIL = "aleksandra_kochenkova_44_999@yandex.com"
TEST_PASSWORD = "123456"


from locators.locators import MainPageLocators, LoginPageLocators, ProfilePageLocators


def test_login_from_main_page_button(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*MainPageLocators.LOGIN_BUTTON_HEADER).click()

    WebDriverWait(driver,10).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(TEST_EMAIL)

    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver,10).until(
        EC.visibility_of_element_located(ProfilePageLocators.CONSTRUCTOR_LINK)
    )

    assert driver.find_element(*ProfilePageLocators.CONSTRUCTOR_LINK).is_displayed()


def test_login_from_personal_account_button(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(TEST_EMAIL)

    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ProfilePageLocators.CONSTRUCTOR_LINK)
    )

    assert driver.find_element(*ProfilePageLocators.CONSTRUCTOR_LINK).is_displayed()


from locators.locators import RegistrationPageLocators


def test_login_from_registration_form(driver):
    driver.get("https://stellarburgers.education-services.ru/register")
    driver.find_element(*RegistrationPageLocators.LOGIN_LINK).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(TEST_EMAIL)

    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ProfilePageLocators.CONSTRUCTOR_LINK)
    )

    assert driver.find_element(*ProfilePageLocators.CONSTRUCTOR_LINK).is_displayed()


def test_login_from_password_recovery_form(driver):
    driver.get("https://stellarburgers.education-services.ru/forgot-password")
    driver.find_element(*LoginPageLocators.LOGIN_LINK).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(TEST_EMAIL)

    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ProfilePageLocators.CONSTRUCTOR_LINK)
    )

    assert driver.find_element(*ProfilePageLocators.CONSTRUCTOR_LINK).is_displayed()
