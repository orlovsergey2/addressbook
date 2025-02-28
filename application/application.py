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

