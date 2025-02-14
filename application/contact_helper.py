from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
# Класс-помощник для работы с контактами
class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        """Открытие страницы добавления контакта"""
        self.app.driver.find_element(By.LINK_TEXT, "add new").click()

    def create_contact(self, contact):
        """Создание контакта"""
        self.open_contact_page()
        self.app.type(By.NAME, "firstname", contact.firstname)
        self.app.type(By.NAME, "middlename", contact.middlename)
        self.app.type(By.NAME, "lastname", contact.lastname)
        self.app.type(By.NAME, "nickname", contact.nickname)
        self.app.type(By.NAME, "title", contact.title)
        self.app.type(By.NAME, "company", contact.company)
        self.app.type(By.NAME, "address", contact.address)
        self.app.type(By.NAME, "home", contact.home)
        self.app.type(By.NAME, "mobile", contact.mobile)
        self.app.type(By.NAME, "work", contact.work)
        self.app.type(By.NAME, "fax", contact.fax)
        self.app.type(By.NAME, "email", contact.email)
        self.app.type(By.NAME, "email2", contact.email2)
        self.app.type(By.NAME, "email3", contact.email3)
        self.app.type(By.NAME, "homepage", contact.homepage)

        # Выбор даты рождения
        Select(self.app.driver.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        Select(self.app.driver.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        self.app.type(By.NAME, "byear", contact.byear)

        # Выбор даты годовщины
        Select(self.app.driver.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
        Select(self.app.driver.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
        self.app.type(By.NAME, "ayear", contact.ayear)

        # Подтверждение создания контакта
        self.app.driver.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()