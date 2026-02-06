from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import RegistrationPageLocators, ProfilePageLocators
from data.test_data import TEST_EMAIL, TEST_PASSWORD, INVALID_PASSWORD


def test_successful_registration(open_register_page):
    driver = open_register_page

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
    ).send_keys("Aleksandra")

    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ProfilePageLocators.CONSTRUCTOR_LINK)
    ).is_displayed()


def test_registration_with_invalid_password(open_register_page):
    driver = open_register_page

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
    ).send_keys("Aleksandra")

    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(
        "invalid_" + TEST_EMAIL
    )
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(
        INVALID_PASSWORD
    )
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    error_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            RegistrationPageLocators.PASSWORD_ERROR
        )
    )

    assert "пароль" in error_element.text.lower() or "минимум" in error_element.text.lower()
