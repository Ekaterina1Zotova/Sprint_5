from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import BASE_URL, REGISTER_URL, FORGOT_PASSWORD_URL
from helpers import login_user
from locators import AuthFormLocators, MainPageLocators

WAIT_TIMEOUT = 10


# Общая проверка: после входа пользователь на главной, видна кнопка «Оформить заказ»
def assert_logged_in(driver):
    WebDriverWait(driver, WAIT_TIMEOUT).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
    assert driver.current_url == f"{BASE_URL}/", (
        f"Ожидалась главная страница, а открылась: {driver.current_url}")


def test_login_by_main_page_button(driver, registered_user):
    # Вход по кнопке «Войти в аккаунт» на главной
    email, password = registered_user

    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()

    # Ждём форму входа и логинимся данными зарегистрированного пользователя
    WebDriverWait(driver, WAIT_TIMEOUT).until(
        expected_conditions.visibility_of_element_located(AuthFormLocators.LOGIN_EMAIL_FIELD))
    login_user(driver, email, password)

    assert_logged_in(driver)


def test_login_via_personal_account_button(driver, registered_user):
    # Вход через кнопку «Личный Кабинет» в шапке
    email, password = registered_user

    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    # Неавторизованного пользователя сайт сам приводит на форму входа
    WebDriverWait(driver, WAIT_TIMEOUT).until(
        expected_conditions.visibility_of_element_located(AuthFormLocators.LOGIN_EMAIL_FIELD))
    login_user(driver, email, password)

    assert_logged_in(driver)


def test_login_via_registration_form_link(driver, registered_user):
    # Вход через кнопку «Войти» в форме регистрации
    email, password = registered_user

    driver.get(REGISTER_URL)
    driver.find_element(*AuthFormLocators.LOGIN_LINK).click()

    WebDriverWait(driver, WAIT_TIMEOUT).until(
        expected_conditions.visibility_of_element_located(AuthFormLocators.LOGIN_EMAIL_FIELD))
    login_user(driver, email, password)

    assert_logged_in(driver)


def test_login_via_forgot_password_page_link(driver, registered_user):
    # Вход через кнопку «Войти» в форме восстановления пароля
    email, password = registered_user

    driver.get(FORGOT_PASSWORD_URL)
    driver.find_element(*AuthFormLocators.LOGIN_LINK).click()

    WebDriverWait(driver, WAIT_TIMEOUT).until(
        expected_conditions.visibility_of_element_located(AuthFormLocators.LOGIN_EMAIL_FIELD))
    login_user(driver, email, password)

    assert_logged_in(driver)
