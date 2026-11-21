import random
import string

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import REGISTER_URL, LOGIN_URL
from locators import RegistrationPageLocators, AuthFormLocators

WAIT_TIMEOUT = 10


# Генерирует уникальный email вида ekaterinazotova59123@yandex.ru:
# имя + фамилия + номер когорты + 3 случайные цифры
def generate_email():
    name = "ekaterina"
    surname = "zotova"
    cohort = "59"
    digits = "".join(random.choices(string.digits, k=3))
    return f"{name}{surname}{cohort}{digits}@yandex.ru"


# Генерирует случайный пароль из 6–10 символов (буквы + цифры)
def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))


# Регистрирует нового пользователя через интерфейс сайта
# и возвращает кортеж (email, password). Браузер остаётся на форме входа.
def register_user(driver):
    email = generate_email()
    password = generate_password()

    driver.get(REGISTER_URL)

    driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys("Екатерина")
    driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    # Ждём, пока откроется форма входа — значит, регистрация прошла
    WebDriverWait(driver, WAIT_TIMEOUT).until(
        expected_conditions.visibility_of_element_located(AuthFormLocators.LOGIN_EMAIL_FIELD)
    )
    return email, password


# Открывает форму входа, заполняет её и нажимает «Войти»
def login_user(driver, email, password):
    driver.get(LOGIN_URL)

    driver.find_element(*AuthFormLocators.LOGIN_EMAIL_FIELD).send_keys(email)
    driver.find_element(*AuthFormLocators.LOGIN_PASSWORD_FIELD).send_keys(password)
    driver.find_element(*AuthFormLocators.LOGIN_BUTTON).click()
