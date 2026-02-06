import pytest
from selenium import webdriver
from data.urls import Urls

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def open_main_page(driver):
    driver.get(Urls.MAIN_PAGE)
    return driver

@pytest.fixture
def open_login_page(driver):
    driver.get(Urls.LOGIN)
    return driver


@pytest.fixture
def open_register_page(driver):
    driver.get(Urls.REGISTER)
    return driver


@pytest.fixture
def open_forgot_password_page(driver):
    driver.get(Urls.FORGOT_PASSWORD)
    return driver


@pytest.fixture
def open_profile_page(driver):
    driver.get(Urls.PROFILE)
    return driver