from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from model.contact import Contact
# Класс-помощник для работы с контактами
class ContactHelper:
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver
        self.contact_cache = None

    def open_contact_page(self):
        """Открытие страницы добавления контакта"""
        if not (self.driver.current_url.endswith("/addressbook/") and len(self.driver.find_elements(By.LINK_TEXT, "Edit / add address book entry")) > 0):
            self.app.driver.find_element(By.LINK_TEXT, "add new").click()

    def select_contact_by_index(self, index):
        """Выбирает контакт по указанному индексу."""
        self.open_contact_page()  # Открываем страницу контактов
        elements = self.app.driver.find_elements(By.NAME, "selected[]")
        if elements and 0 <= index < len(elements):  # Проверяем, что индекс в допустимых пределах
            elements[index].click()  # Выбираем контакт по индексу
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
        self.invalidate_cache()

    def modify_contact(self, index, contact):
        """Модифицирует контакт по индексу."""
        elements = self.app.driver.find_elements(By.NAME, "selected[]")

        elements[index].click()  # Выбираем контакт по индексу

        # Ожидаем, пока кнопка редактирования станет доступной
        edit_button = WebDriverWait(self.app.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='Edit']"))
        )
        edit_button.click()

        # Заполняем форму с новыми значениями
        self.fill_contact_form(
            firstname=contact.firstname,
            middlename=contact.middlename,
            lastname=contact.lastname,
            nickname=contact.nickname,
            title=contact.title,
            company=contact.company,
            address=contact.address,
            home=contact.home,
            mobile=contact.mobile,
            work=contact.work,
            fax=contact.fax,
            email=contact.email,
            email2=contact.email2,
            email3=contact.email3,
            homepage=contact.homepage,
            bday=contact.bday,
            bmonth=contact.bmonth,
            byear=contact.byear,
            aday=contact.aday,
            amonth=contact.amonth,
            ayear=contact.ayear
        )

        # Сохраняем изменения
        self.app.driver.find_element(By.NAME, "update").click()
        self.return_to_contact_page()
        self.invalidate_cache()

    def fill_contact_form(self, **fields):
        """Заполняет форму контакта."""
        for field, value in fields.items():
            if value is None:
                continue  # Пропускаем поля со значением None
            if field in ["bday", "bmonth", "aday", "amonth"]:
                # Для выпадающих списков используем Select
                select = Select(self.app.driver.find_element(By.NAME, field))
                select.select_by_visible_text(value)
            else:
                # Для обычных полей ввода
                element = self.app.driver.find_element(By.NAME, field)
                element.clear()
                element.send_keys(value)

    def delete_first_contact(self):
        """Удаляет первый контакт."""
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        """Удаляет контакт по указанному индексу."""
        self.return_to_contact_page()  # Открываем страницу контактов
        elements = self.app.driver.find_elements(By.NAME, "selected[]")
        if elements and 0 <= index < len(elements):  # Проверяем, что индекс в допустимых пределах
            elements[index].click()  # Выбираем контакт по индексу
            self.app.driver.find_element(By.XPATH, "//input[@value='Delete']").click()  # Удаляем контакт
            self.return_to_contact_page()  # Возвращаемся на страницу контактов
        self.invalidate_cache()

    def return_to_contact_page(self):
        """Возвращается на страницу с контактами."""
        if not (self.driver.current_url.endswith("/addressbook/") and len(self.driver.find_elements(By.LINK_TEXT, "Last name")) > 0):
            self.driver.find_element(By.LINK_TEXT, "home").click()

    def count(self):
        """Возвращает количество контактов."""
        self.return_to_contact_page()
        return len(self.app.driver.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        """Возвращает список контактов с использованием кэширования."""
        if self.contact_cache is None:  # Если кэш пуст, загружаем данные
            self.contact_cache = []
            # Логика загрузки списка контактов
            for row in self.app.driver.find_elements(By.NAME, "entry"):
                cells = row.find_elements(By.TAG_NAME, "td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element(By.NAME, "selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)  # Возвращаем копию кэша

    def invalidate_cache(self):
        """Сбрасывает кэш списка контактов."""
        self.contact_cache = None


