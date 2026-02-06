from locators import (
    MainPageLocators,
    ProfilePageLocators,
    ConstructorPageLocators,
    LoginPageLocators
)
from data.helpers import login


def test_go_to_personal_account(open_main_page):
    driver = open_main_page

    login(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    assert driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).is_displayed()


def test_go_from_personal_account_to_constructor_by_button(open_main_page):
    driver = open_main_page

    login(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*ProfilePageLocators.CONSTRUCTOR_LINK).click()

    assert driver.find_element(*ConstructorPageLocators.BUNS_TAB).is_displayed()


def test_go_from_personal_account_to_constructor_by_logo(open_main_page):
    driver = open_main_page

    login(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*MainPageLocators.LOGO).click()

    assert driver.find_element(*ConstructorPageLocators.BUNS_TAB).is_displayed()


def test_logout_from_personal_account(open_main_page):
    driver = open_main_page

    login(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()

    assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()
