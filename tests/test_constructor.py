from locators.locators import ConstructorPageLocators


def test_go_to_buns_section(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*ConstructorPageLocators.BUNS_TAB).click()
    buns_tab = driver.find_element(*ConstructorPageLocators.BUNS_TAB)

    assert "current" in buns_tab.get_attribute("class")


def test_go_to_sauces_section(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()
    sauces_tab = driver.find_element(*ConstructorPageLocators.SAUCES_TAB)

    assert "current" in sauces_tab.get_attribute("class")


def test_go_to_fillings_section(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*ConstructorPageLocators.TOPPINGS_TAB).click()
    fillings_tab = driver.find_element(*ConstructorPageLocators.TOPPINGS_TAB)

    assert "current" in fillings_tab.get_attribute("class")
