from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import BASE_URL, LOGIN_URL
from helpers import login_user
from locators import AuthFormLocators, MainPageLocators, PersonalAccountLocators

WAIT_TIMEOUT = 10


# Общий шаг: открываем личный кабинет после входа
def open_profile(driver):
    WebDriverWait(driver, WAIT_TIMEOUT).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    )
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, WAIT_TIMEOUT).until(
        expected_conditions.visibility_of_element_located(PersonalAccountLocators.PROFILE_HEADING))


def test_transition_to_personal_account(driver, registered_user):
    # Переход в личный кабинет по клику на «Личный Кабинет»
    email, password = registered_user

    login_user(driver, email, password)
    open_profile(driver)

    assert driver.current_url == f"{BASE_URL}/account/profile", (
        f"Ожидался личный кабинет, а открылась: {driver.current_url}")


def test_transition_from_profile_to_constructor_by_button(driver, registered_user):
    # Из личного кабинета в конструктор по кнопке «Конструктор»
    email, password = registered_user

    login_user(driver, email, password)
    open_profile(driver)

    driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

    # Снова на главной — виден заголовок «Соберите бургер»
    WebDriverWait(driver, WAIT_TIMEOUT).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.ASSEMBLE_BURGER_TITLE))
    assert driver.current_url == f"{BASE_URL}/", (
        f"Ожидалась главная страница, а открылась: {driver.current_url}")


def test_transition_from_profile_to_constructor_by_logo(driver, registered_user):
    # Из личного кабинета в конструктор по логотипу Stellar Burgers
    email, password = registered_user

    login_user(driver, email, password)
    open_profile(driver)

    driver.find_element(*MainPageLocators.LOGO).click()

    WebDriverWait(driver, WAIT_TIMEOUT).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.ASSEMBLE_BURGER_TITLE))
    assert driver.current_url == f"{BASE_URL}/", (
        f"Ожидалась главная страница, а открылась: {driver.current_url}")


def test_logout_from_personal_account(driver, registered_user):
    # Выход из аккаунта по кнопке «Выход» в личном кабинете
    email, password = registered_user

    login_user(driver, email, password)
    open_profile(driver)

    driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).click()

    # После выхода снова открывается форма входа
    WebDriverWait(driver, WAIT_TIMEOUT).until(
        expected_conditions.visibility_of_element_located(AuthFormLocators.LOGIN_EMAIL_FIELD))
    assert driver.current_url == LOGIN_URL, (
        f"Ожидалась страница входа, а открылась: {driver.current_url}")
