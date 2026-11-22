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


# Фикстура пользователя: один аккаунт на весь прогон. Регистрируем его
# через отдельный короткоживущий браузер — за прогон создаётся один
# пользователь вместо десяти, и стенд не упирается в лимит запросов.
# Браузер каждого теста всё равно открывается заново, изоляция сохраняется
@pytest.fixture(scope="session")
def registered_user():
    reg_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        return register_user(reg_driver)
    finally:
        reg_driver.quit()
