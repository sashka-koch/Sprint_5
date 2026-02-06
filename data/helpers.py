from locators import LoginPageLocators
from data.urls import Urls
from data.test_data import TEST_EMAIL, TEST_PASSWORD


def login(driver):
    driver.get(Urls.LOGIN)
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()