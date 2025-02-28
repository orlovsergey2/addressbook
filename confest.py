import pytest
from selenium import webdriver
from application.application import Application

@pytest.fixture(scope="session")
def app():
    # Инициализация драйвера
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()  # Очистка куки

    # Инициализация Application
    app = Application(driver)

    # Авторизация перед началом тестов
    app.session.login(username="admin", password="secret")

    # Передача объекта в тест
    yield app

    # Выход из системы после завершения всех тестов
    app.session.logout()

    # Завершение работы драйвера после всех тестов
    app.tearDown()