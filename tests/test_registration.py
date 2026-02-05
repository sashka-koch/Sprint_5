from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators import RegistrationPageLocators, ProfilePageLocators

TEST_EMAIL = "aleksandra_kochenkova_44_999@yandex.com"
TEST_PASSWORD = "Test12345"       
INVALID_PASSWORD = "123"          


def test_successful_registration(driver):
    driver.get("https://stellarburgers.education-services.ru/register")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
    ).send_keys("Aleksandra")

    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ProfilePageLocators.CONSTRUCTOR_LINK)
    )

    assert driver.find_element(*ProfilePageLocators.CONSTRUCTOR_LINK).is_displayed()


def test_registration_with_invalid_password(driver):
    driver.get("https://stellarburgers.education-services.ru/register")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
    ).send_keys("Aleksandra")

    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys("invalid_" + TEST_EMAIL)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(INVALID_PASSWORD)
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    error_element= WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[@class='input__error text_type_main-default']"))
)

    assert "пароль" in error_element.text.lower() or "минимум" in error_element.text.lower()