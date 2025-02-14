import pytest
from selenium import webdriver
from application.application import Application
# Фикстура для инициализации и завершения работы драйвера
@pytest.fixture(scope="session")
def app():
    # Инициализация драйвера
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()  # Очистка куки

    # Инициализация Application
    app = Application(driver)

    # Передача объекта в тест
    yield app

    # Завершение работы драйвера после всех тестов
    app.tearDown()