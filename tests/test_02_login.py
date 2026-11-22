from data import BASE_URL, REGISTER_URL, FORGOT_PASSWORD_URL
from helpers import login_user, assert_logged_in
from locators import AuthFormLocators, MainPageLocators


class TestLogin:

    def test_login_by_main_page_button(self, driver, registered_user):
        # Вход по кнопке «Войти в аккаунт» на главной
        email, password = registered_user

        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
        login_user(driver, email, password)

        assert_logged_in(driver)

    def test_login_via_personal_account_button(self, driver, registered_user):
        # Вход через кнопку «Личный Кабинет» в шапке
        email, password = registered_user

        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        login_user(driver, email, password)

        assert_logged_in(driver)

    def test_login_via_registration_form_link(self, driver, registered_user):
        # Вход через кнопку «Войти» в форме регистрации
        email, password = registered_user

        driver.get(REGISTER_URL)
        driver.find_element(*AuthFormLocators.LOGIN_LINK).click()
        login_user(driver, email, password)

        assert_logged_in(driver)

    def test_login_via_forgot_password_page_link(self, driver, registered_user):
        # Вход через кнопку «Войти» в форме восстановления пароля
        email, password = registered_user

        driver.get(FORGOT_PASSWORD_URL)
        driver.find_element(*AuthFormLocators.LOGIN_LINK).click()
        login_user(driver, email, password)

        assert_logged_in(driver)
