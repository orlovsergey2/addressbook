# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# Фикстура для инициализации и завершения работы драйвера
@pytest.fixture(scope="function")
def driver():
    # Инициализация драйвера
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()  # Очистка куки
    yield driver
    # Завершение работы драйвера
    driver.quit()

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

# Вспомогательные функции
def login(driver):
    """Авторизация"""
    base_url = "http://localhost/addressbook/addressbook/"
    driver.get(base_url)  # Открываем главную страницу
    type(driver, By.NAME, "user", "admin")
    type(driver, By.NAME, "pass", "secret")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()

    # Проверка успешной авторизации
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))

def logout(driver):
    """Выход из системы"""
    driver.find_element(By.LINK_TEXT, "Logout").click()

def type(driver, locator_type, locator, text):
    """Вспомогательный метод для ввода текста"""
    if text is not None:
        driver.find_element(locator_type, locator).clear()
        driver.find_element(locator_type, locator).send_keys(text)

# Тест для добавления группы
def test_add_group(driver):
    login(driver)
    open_group_page(driver)
    create_group(driver)
    return_to_groups_page(driver)
    logout(driver)

def return_to_groups_page(driver):
    driver.find_element(By.LINK_TEXT, "groups").click()

def create_group(driver):
    # Инициализация создания группы
    driver.find_element(By.NAME, "new").click()

    # Заполнение формы группы
    driver.find_element(By.NAME, "group_name").clear()
    driver.find_element(By.NAME, "group_name").send_keys("adad")

    driver.find_element(By.NAME, "group_header").clear()
    driver.find_element(By.NAME, "group_header").send_keys("adada")

    driver.find_element(By.NAME, "group_footer").clear()
    driver.find_element(By.NAME, "group_footer").send_keys("adada")

    # Подтверждение создания группы
    driver.find_element(By.NAME, "submit").click()

def open_group_page(driver):
    base_url = "http://localhost/addressbook/addressbook/"
    driver.get(base_url + "group.php")  # Открываем group.php

# Тест для добавления контакта
def test_add_contact(driver):
    # Инициализация тестовых данных для контакта
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

    # Выполнение теста
    login(driver)
    open_contact_page(driver)
    create_contact(driver, contact)
    logout(driver)

def open_contact_page(driver):
    """Открытие страницы добавления контакта"""
    driver.find_element(By.LINK_TEXT, "add new").click()

def create_contact(driver, contact):
    """Создание контакта"""
    # Заполнение формы контакта
    type(driver, By.NAME, "firstname", contact.firstname)
    type(driver, By.NAME, "middlename", contact.middlename)
    type(driver, By.NAME, "lastname", contact.lastname)
    type(driver, By.NAME, "nickname", contact.nickname)
    type(driver, By.NAME, "title", contact.title)
    type(driver, By.NAME, "company", contact.company)
    type(driver, By.NAME, "address", contact.address)
    type(driver, By.NAME, "home", contact.home)
    type(driver, By.NAME, "mobile", contact.mobile)
    type(driver, By.NAME, "work", contact.work)
    type(driver, By.NAME, "fax", contact.fax)
    type(driver, By.NAME, "email", contact.email)
    type(driver, By.NAME, "email2", contact.email2)
    type(driver, By.NAME, "email3", contact.email3)
    type(driver, By.NAME, "homepage", contact.homepage)

    # Выбор даты рождения
    Select(driver.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
    Select(driver.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
    type(driver, By.NAME, "byear", contact.byear)

    # Выбор даты годовщины
    Select(driver.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
    Select(driver.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
    type(driver, By.NAME, "ayear", contact.ayear)

    # Подтверждение создания контакта
    driver.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()