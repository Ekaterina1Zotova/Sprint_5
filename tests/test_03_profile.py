from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import BASE_URL, LOGIN_URL
from helpers import login_user, open_profile, WAIT_TIMEOUT
from locators import AuthFormLocators, MainPageLocators, PersonalAccountLocators


class TestProfile:

    def test_transition_to_personal_account(self, driver, registered_user):
        # Переход в личный кабинет по клику на «Личный Кабинет»
        email, password = registered_user

        login_user(driver, email, password)
        open_profile(driver)

        # Открылся личный кабинет: URL страницы профиля
        assert WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.url_to_be(f"{BASE_URL}/account/profile")), (
            f"Ожидался личный кабинет, а открылась: {driver.current_url}")

    def test_transition_from_profile_to_constructor_by_button(self, driver, registered_user):
        # Из личного кабинета в конструктор по кнопке «Конструктор»
        email, password = registered_user

        login_user(driver, email, password)
        open_profile(driver)

        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

        # Снова на главной: виден заголовок «Соберите бургер», URL главной
        assert WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.ASSEMBLE_BURGER_TITLE)
        ).is_displayed() and driver.current_url == f"{BASE_URL}/", (
            f"Ожидалась главная страница, а открылась: {driver.current_url}")

    def test_transition_from_profile_to_constructor_by_logo(self, driver, registered_user):
        # Из личного кабинета в конструктор по логотипу Stellar Burgers
        email, password = registered_user

        login_user(driver, email, password)
        open_profile(driver)

        driver.find_element(*MainPageLocators.LOGO).click()

        assert WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.ASSEMBLE_BURGER_TITLE)
        ).is_displayed() and driver.current_url == f"{BASE_URL}/", (
            f"Ожидалась главная страница, а открылась: {driver.current_url}")

    def test_logout_from_personal_account(self, driver, registered_user):
        # Выход из аккаунта по кнопке «Выход» в личном кабинете
        email, password = registered_user

        login_user(driver, email, password)
        open_profile(driver)

        # Дожидаемся, что кнопка «Выход» кликабельна, и выходим
        WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON))
        driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).click()

        # После выхода снова открывается форма входа
        assert WebDriverWait(driver, WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(AuthFormLocators.LOGIN_EMAIL_FIELD)
        ).is_displayed() and driver.current_url == LOGIN_URL, (
            f"Ожидалась страница входа, а открылась: {driver.current_url}")
