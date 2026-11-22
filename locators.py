from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка «Войти в аккаунт» на главной
    LOGIN_BUTTON_MAIN = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    # Кнопка «Личный Кабинет» в шапке
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//*[contains(text(), 'Личный Кабинет')]")
    # Кнопка «Конструктор» в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//*[contains(text(), 'Конструктор')]")
    # Логотип Stellar Burgers в шапке
    LOGO = (By.XPATH, ".//*[contains(@class, 'AppHeader_header__logo')]")
    # Кнопка «Оформить заказ» — признак успешного входа
    ORDER_BUTTON = (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")
    # Заголовок «Соберите бургер» на главной
    ASSEMBLE_BURGER_TITLE = (By.XPATH, ".//*[contains(text(), 'Соберите бургер')]")


class RegistrationPageLocators:
    # Поле «Имя» в форме регистрации
    NAME_FIELD = (By.XPATH, ".//*[text()='Имя']/following-sibling::input")
    # Поле «Email» в форме регистрации
    EMAIL_FIELD = (By.XPATH, ".//*[text()='Email']/following-sibling::input")
    # Поле «Пароль» в форме регистрации
    PASSWORD_FIELD = (By.XPATH, ".//*[text()='Пароль']/following-sibling::input")
    # Кнопка «Зарегистрироваться» в форме регистрации
    REGISTER_BUTTON = (By.XPATH, './/*[contains(@class, "button_button_type_primary")]')
    # Ошибка «Некорректный пароль» под полем
    WRONG_PASSWORD_ERROR = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")


class AuthFormLocators:
    # Кнопка «Войти» в форме входа
    LOGIN_BUTTON = (By.XPATH, './/button[contains(@class, "button_button_type_primary")]')
    # Поле «Email» в форме входа
    LOGIN_EMAIL_FIELD = (By.XPATH, ".//*[text()='Email']/following-sibling::input")
    # Поле «Пароль» в форме входа
    LOGIN_PASSWORD_FIELD = (By.XPATH, ".//*[text()='Пароль']/following-sibling::input")
    # Ссылка «Войти» на страницах регистрации и восстановления пароля
    LOGIN_LINK = (By.XPATH, './/*[contains(@class, "Auth_link")]')
    # Заголовок «Вход» — форма входа открыта
    AUTH_HEADING = (By.XPATH, ".//*[text()='Вход']")
    AUTH_ERROR = (By.XPATH, ".//p[contains(@class, 'input__error')]")


class PersonalAccountLocators:
    # Ссылка «Профиль» в меню личного кабинета
    PROFILE_HEADING = (By.XPATH, ".//a[contains(text(), 'Профиль')]")
    # Кнопка «Выйти» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")


class ConstructorLocators:
    # Вкладка «Булки» в разделе «Конструктор»
    BUNS_TAB = (By.XPATH, ".//span[text()='Булки']")
    # Вкладка «Соусы»
    SAUCES_TAB = (By.XPATH, ".//span[text()='Соусы']")
    # Вкладка «Начинки»
    FILLINGS_TAB = (By.XPATH, ".//span[text()='Начинки']")
    # Активная вкладка «Булки»
    BUNS_TAB_ACTIVE = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')][.//span[text()='Булки']]")
    # Активная вкладка «Соусы»
    SAUCES_TAB_ACTIVE = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')][.//span[text()='Соусы']]")
    # Активная вкладка «Начинки»
    FILLINGS_TAB_ACTIVE = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')][.//span[text()='Начинки']]")


class ModalLocators:
    # Оверлей модального окна — перехватывает клики, пока открыт или исчезает
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay')]")