import random
import string
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import REGISTER_URL, LOGIN_URL, BASE_URL
from locators import RegistrationPageLocators, AuthFormLocators, MainPageLocators

WAIT_TIMEOUT = 10


# Генерирует уникальный email вида ekaterinazotova59123@yandex.ru:
# имя + фамилия + номер когорты + 3 случайные цифры
def generate_email():
    name = "ekaterina"
    surname = "zotova"
    cohort = "59"
    digits = "".join(random.choices(string.digits, k=3))
    return f"{name}{surname}{cohort}{digits}@yandex.ru"


# Генерирует случайный пароль из букв и цифр
def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))


# Заполняет поле и дожидается, что значение зафиксировалось в нём.
# clear() на контролируемых React-полях не сбрасывает состояние компонента,
# поэтому очищаем через JS с отправкой события input
def fill_field(driver, locator, value):
    field = WebDriverWait(driver, WAIT_TIMEOUT).until(
        expected_conditions.element_to_be_clickable(locator))
    driver.execute_script(
        "arguments[0].value = '';"
        "arguments[0].dispatchEvent(new Event('input', {bubbles: true}));",
        field)
    field.send_keys(value)


# Собирает текст ошибок, которые форма показывает в момент проверки.
# Без этого повторы происходят вслепую: непонятно, отклонил сервер запрос
# или редирект просто не успел за таймаут
def collect_form_errors(driver):
    elements = driver.find_elements(By.CSS_SELECTOR, "[class*='error']")
    return [e.text for e in elements if e.text.strip()]


# Регистрирует нового пользователя через интерфейс сайта
# и возвращает кортеж (email, password). До пяти попыток: при серии
# регистраций тестовый стенд изредка молча отклоняет запрос, не показывая
# ошибки в интерфейсе (задокументировано в README)
def register_user(driver):
    password = generate_password()
    last_state = ""

    for attempt in range(5):
        # Новый email на каждую попытку: если пользователь успел создаться,
        # повторная регистрация того же адреса гарантированно упадёт
        email = generate_email()

        driver.get(REGISTER_URL)
        fill_field(driver, RegistrationPageLocators.NAME_FIELD, "Екатерина")
        fill_field(driver, RegistrationPageLocators.EMAIL_FIELD, email)
        fill_field(driver, RegistrationPageLocators.PASSWORD_FIELD, password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        try:
            # url_contains вместо url_to_be: переживает query-параметры
            # и trailing slash, на которых строгое сравнение ломается
            WebDriverWait(driver, WAIT_TIMEOUT).until(
                expected_conditions.url_contains("/login"))
            return email, password
        except Exception:
            last_state = (
                f"[попытка {attempt + 1}] URL: {driver.current_url}, "
                f"ошибки на форме: {collect_form_errors(driver)}")
            print(f"\n{last_state}")
            # Небольшая пауза: даём серверу отдышаться перед повтором
            time.sleep(2)

    raise AssertionError(
        f"Регистрация не завершилась за 5 попыток. Последнее состояние: {last_state}")


# Заполняет форму входа и нажимает «Войти»,
# дожидаясь перехода на главную. Если тест уже открыл форму своим
# путём — не перезагружаем её, чтобы не стереть пройденный сценарий
def login_user(driver, email, password):
    if "/login" not in driver.current_url:
        driver.get(LOGIN_URL)

    fill_field(driver, AuthFormLocators.LOGIN_EMAIL_FIELD, email)
    fill_field(driver, AuthFormLocators.LOGIN_PASSWORD_FIELD, password)
    driver.find_element(*AuthFormLocators.LOGIN_BUTTON).click()

    # url_contains вместо строгого url_to_be: главная может открыться
    # с query-параметрами или слэшем на конце
    WebDriverWait(driver, WAIT_TIMEOUT).until(
        expected_conditions.url_contains(BASE_URL))


# Общая проверка: после входа пользователь на главной,
# видна кнопка «Оформить заказ»
def assert_logged_in(driver):
    assert WebDriverWait(driver, WAIT_TIMEOUT).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
    ).is_displayed() and driver.current_url.startswith(BASE_URL), (
        f"Ожидалась главная страница, а открылась: {driver.current_url}")


# Общий шаг: открываем личный кабинет после входа
def open_profile(driver):
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, WAIT_TIMEOUT).until(
        expected_conditions.url_contains(f"{BASE_URL}/account/profile"))
