import pytest
from selenium import webdriver
from application.application import Application

@pytest.fixture(scope="session")
def app(request):
    # Инициализация драйвера
    driver = webdriver.Firefox()  # Или другой браузер
    driver.implicitly_wait(10)
    driver.delete_all_cookies()  # Очистка куки

    # Инициализация Application
    fixture = Application(driver)

    # Авторизация перед началом тестов
    fixture.session.login(username="admin", password="secret")

    # Финализатор для завершения работы
    def fin():
        fixture.session.ensure_logout()  # Выход из системы
        fixture.driver.quit()  # Закрытие браузера

    # Регистрация финализатора
    request.addfinalizer(fin)

    # Передача объекта в тест
    return fixture