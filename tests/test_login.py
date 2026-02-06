from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    MainPageLocators,
    LoginPageLocators,
    ProfilePageLocators
)
from data.test_data import TEST_EMAIL, TEST_PASSWORD


def test_login_from_main_page_button(open_main_page):
    driver = open_main_page

    driver.find_element(*MainPageLocators.LOGIN_BUTTON_HEADER).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(TEST_EMAIL)

    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ProfilePageLocators.CONSTRUCTOR_LINK)
    ).is_displayed()


def test_login_from_personal_account_button(open_main_page):
    driver = open_main_page

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(TEST_EMAIL)

    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ProfilePageLocators.CONSTRUCTOR_LINK)
    ).is_displayed()


def test_login_from_registration_form(open_register_page):
    driver = open_register_page

    driver.find_element(*LoginPageLocators.LOGIN_LINK).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(TEST_EMAIL)

    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ProfilePageLocators.CONSTRUCTOR_LINK)
    ).is_displayed()


def test_login_from_forgot_password_form(open_forgot_password_page):
    driver = open_forgot_password_page

    driver.find_element(*LoginPageLocators.LOGIN_LINK).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(TEST_EMAIL)

    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ProfilePageLocators.CONSTRUCTOR_LINK)
    ).is_displayed()
