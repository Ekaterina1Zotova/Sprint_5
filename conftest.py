import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from helpers import register_user


# Фикстура браузера: создаёт Chrome для одного теста
# и закрывает его после завершения — так каждый тест автономен
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


# Фикстура пользователя: регистрирует нового пользователя через интерфейс
# и возвращает (email, password) — тесты входа и кабинета используют их для логина
@pytest.fixture
def registered_user(driver):
    return register_user(driver)
