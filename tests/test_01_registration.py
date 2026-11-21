from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import REGISTER_URL
from helpers import generate_email, generate_password
from locators import RegistrationPageLocators, AuthFormLocators


def test_successful_registration(driver):
    driver.get(REGISTER_URL)

    # Заполняем форму: имя не пустое, email сгенерирован, пароль — 8 символов
    driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys("Екатерина")
    driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(generate_email())
    driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(generate_password())

    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    # После успешной регистрации открывается форма входа — ждём заголовок «Вход»
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(AuthFormLocators.AUTH_HEADING))
    assert driver.find_element(*AuthFormLocators.AUTH_HEADING).is_displayed()



def test_registration_with_wrong_password(driver):
    driver.get(REGISTER_URL)

    # Заполняем форму с коротким паролем: 5 символов — меньше минимума в 6
    driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys("Екатерина")
    driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(generate_email())
    driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys("12345")

    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    # Появляется ошибка «Некорректный пароль»
    error = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(RegistrationPageLocators.WRONG_PASSWORD_ERROR))
   
    assert error.is_displayed()
