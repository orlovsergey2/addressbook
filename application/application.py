from .contact_helper import ContactHelper
from .group_helper import GroupHelper
from .session import SessionHelper
from selenium import webdriver
from selenium.webdriver.common.by import By
# Класс-менеджер
class Application:
    def __init__(self):
        self.By = By
        self.driver = webdriver.Firefox()
        self.base_url = "http://localhost/addressbook/addressbook/"
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.session = SessionHelper(self)
        self.verificationErrors = []

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False
    def open_home_page(self):
        """Открытие домашней страницы"""
        self.driver.get(self.base_url)

    def tear_down(self):
        """Завершение теста"""
        self.driver.quit()


    def type(self, locator_type, locator, text):
        """Вспомогательный метод для ввода текста"""
        if text is not None:
            self.driver.find_element(locator_type, locator).clear()
            self.driver.find_element(locator_type, locator).send_keys(text)

