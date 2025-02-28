from .contact_helper import ContactHelper
from .group_helper import GroupHelper
from .session import SessionHelper
from selenium import webdriver
# Класс-менеджер
class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://localhost/addressbook/addressbook/"
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.session = SessionHelper(self)
        self.verificationErrors = []

    def is_valid(self, expected_url=None):
        """Проверяет, что драйвер активен и текущий URL соответствует ожидаемому."""
        try:
            current_url = self.driver.current_url
            if expected_url is None:
                expected_url = self.base_url
            if not current_url.startswith(expected_url):
                self.driver.get(expected_url)  # Переходим на ожидаемый URL, если текущий URL не совпадает
            return True
        except Exception as e:
            print(f"Ошибка при проверке валидности сессии: {e}")
            return False
    def open_home_page(self):
        """Открытие домашней страницы"""
        self.driver.get(self.base_url)

    def tearDown(self):
        """Завершение теста"""
        self.driver.quit()

    def type(self, locator_type, locator, text):
        """Вспомогательный метод для ввода текста"""
        if text is not None:
            self.driver.find_element(locator_type, locator).clear()
            self.driver.find_element(locator_type, locator).send_keys(text)

