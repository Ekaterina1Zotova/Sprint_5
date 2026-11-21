from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import BASE_URL
from locators import ConstructorLocators



def test_switch_to_buns_section(driver):
    # Переход к разделу «Булки»
    driver.get(BASE_URL)

    # Дожидаемся, что вкладка видима и кликабельна
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(ConstructorLocators.BUNS_TAB))

    tab = driver.find_element(*ConstructorLocators.BUNS_TAB)
    # Клик через JS: событие уходит напрямую элементу, мимо перекрывающего слоя
    driver.execute_script("arguments[0].click();", tab)

    active = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(ConstructorLocators.BUNS_TAB_ACTIVE))
    assert active.is_displayed(), "Вкладка «Булки» не стала активной"


def test_switch_to_sauces_section(driver):
    # Переход к разделу «Соусы»
    driver.get(BASE_URL)
    driver.find_element(*ConstructorLocators.SAUCES_TAB).click()

    active = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(ConstructorLocators.SAUCES_TAB_ACTIVE))
    assert active.is_displayed(), "Вкладка «Соусы» не стала активной"


def test_switch_to_fillings_section(driver):
    # Переход к разделу «Начинки»
    driver.get(BASE_URL)
    driver.find_element(*ConstructorLocators.FILLINGS_TAB).click()

    active = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(ConstructorLocators.FILLINGS_TAB_ACTIVE))
    assert active.is_displayed(), "Вкладка «Начинки» не стала активной"
