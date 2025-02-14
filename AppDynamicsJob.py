# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

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

# Класс-менеджер
class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://localhost/addressbook/addressbook/"
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.verificationErrors = []

    def login(self):
        """Авторизация"""
        self.driver.get(self.base_url)  # Открываем главную страницу
        self.type(By.NAME, "user", "admin")
        self.type(By.NAME, "pass", "secret")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()

        # Проверка успешной авторизации
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))

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

# Класс-помощник для работы с группами
class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        """Открытие страницы групп"""
        self.app.driver.get("http://localhost/addressbook/addressbook/group.php")

    def create_group(self, group):
        """Создание группы"""
        self.open_group_page()
        self.app.driver.find_element(By.NAME, "new").click()
        self.app.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.app.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.app.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        self.app.driver.find_element(By.NAME, "submit").click()

    def return_to_groups_page(self):
        """Возврат на страницу групп"""
        self.app.driver.find_element(By.LINK_TEXT, "groups").click()

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

# Вспомогательный класс для хранения свойств группы
class Group:
    def __init__(self, name=None, header=None, footer=None):
        self.name = name
        self.header = header
        self.footer = footer

# Вспомогательный класс для хранения свойств контакта
class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None,
                 homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear

# Тест, который добавляет контакт и группу
def test_add_contact_and_group(app):
    """Тест для добавления контакта и группы"""
    # Авторизация
    app.login()

    # Добавление контакта
    contact = Contact(
        firstname="Sergey",
        middlename="Sergeevich",
        lastname="Orlov",
        nickname="ORLOV_Sergey",
        title=u"ВУЗ",
        company=u"СиБАДИ",
        address=u"Печальная область, тоскливый район, проспект разочарования, дом 13",
        home="1",
        mobile="88005553535",
        work=u"бездельник",
        fax=u"не имеется",
        email=u"выавып",
        email2=u"ываввы",
        email3=u"ыавыа",
        homepage=u"выаыв",
        bday="12",
        bmonth="August",
        byear="2005",
        aday="12",
        amonth="August",
        ayear="2005"
    )
    app.contact.create_contact(contact)

    # Добавление группы
    app.group.open_group_page()
    group = Group(name="Test Group", header="Header", footer="Footer")
    app.group.create_group(group)
    app.group.return_to_groups_page()