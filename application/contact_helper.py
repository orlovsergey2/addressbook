from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# Класс-помощник для работы с контактами
class ContactHelper:
    def __init__(self, app):
        self.app = app
        driver = self.app.driver

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

    def modify_contact(self, contact):
        """Модифицирует контакт, изменяя только переданные поля."""

        # Выбираем первый контакт для редактирования
        self.app.driver.find_element(By.NAME, "selected[]").click()
        self.app.driver.find_element(By.XPATH, "//img[@alt='Edit']").click()

        # Получаем текущие значения полей контакта
        current_data = {
            "firstname": self.app.driver.find_element(By.NAME, "firstname").get_attribute("value"),
            "middlename": self.app.driver.find_element(By.NAME, "middlename").get_attribute("value"),
            "lastname": self.app.driver.find_element(By.NAME, "lastname").get_attribute("value"),
            "nickname": self.app.driver.find_element(By.NAME, "nickname").get_attribute("value"),
            "title": self.app.driver.find_element(By.NAME, "title").get_attribute("value"),
            "company": self.app.driver.find_element(By.NAME, "company").get_attribute("value"),
            "address": self.app.driver.find_element(By.NAME, "address").get_attribute("value"),
            "home": self.app.driver.find_element(By.NAME, "home").get_attribute("value"),
            "mobile": self.app.driver.find_element(By.NAME, "mobile").get_attribute("value"),
            "work": self.app.driver.find_element(By.NAME, "work").get_attribute("value"),
            "fax": self.app.driver.find_element(By.NAME, "fax").get_attribute("value"),
            "email": self.app.driver.find_element(By.NAME, "email").get_attribute("value"),
            "email2": self.app.driver.find_element(By.NAME, "email2").get_attribute("value"),
            "email3": self.app.driver.find_element(By.NAME, "email3").get_attribute("value"),
            "homepage": self.app.driver.find_element(By.NAME, "homepage").get_attribute("value"),
            "bday": Select(self.app.driver.find_element(By.NAME, "bday")).first_selected_option.text,
            "bmonth": Select(self.app.driver.find_element(By.NAME, "bmonth")).first_selected_option.text,
            "byear": self.app.driver.find_element(By.NAME, "byear").get_attribute("value"),
            "aday": Select(self.app.driver.find_element(By.NAME, "aday")).first_selected_option.text,
            "amonth": Select(self.app.driver.find_element(By.NAME, "amonth")).first_selected_option.text,
            "ayear": self.app.driver.find_element(By.NAME, "ayear").get_attribute("value"),
        }

        # Если новое значение передано, используем его, иначе оставляем текущее
        new_data = {}
        for field in current_data:
            new_data[field] = getattr(contact, field) if getattr(contact, field) is not None else current_data[field]

        # Заполняем форму с новыми значениями
        self.fill_contact_form(**new_data)

        # Сохраняем изменения
        self.app.driver.find_element(By.NAME, "update").click()

    def fill_contact_form(self, **fields):
        """Заполняет форму контакта."""
        for field, value in fields.items():
            if field in ["bday", "bmonth", "aday", "amonth"]:
                # Для выпадающих списков используем Select
                select = Select(self.app.driver.find_element(By.NAME, field))
                select.select_by_visible_text(value)
            else:
                # Для обычных полей ввода
                element = self.app.driver.find_element(By.NAME, field)
                element.clear()
                element.send_keys(value)

    def return_to_contact_page(self):
        """Возврат на страницу контактов"""
        self.app.driver.find_element(By.LINK_TEXT, "home").click()