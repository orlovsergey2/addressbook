# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest


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
                 homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, group=None):
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
        self.group = group


class TestAddGroupAndContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost/addressbook/addressbook/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.delete_all_cookies()  # Очистка куки

    def test_add_group_and_contact(self):
        driver = self.driver

        # Инициализация тестовых данных для группы
        group = Group(name="Test Group", header="Header", footer="Footer")

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
            ayear="2005",
            group="Test Group"  # Группа, к которой будет привязан контакт
        )

        # Выполнение теста
        self.open_home_page(driver)
        self.login(driver)
        self.open_group_page(driver)
        self.create_group(driver, group)
        self.return_to_groups_page(driver)
        self.open_contact_page(driver)
        self.create_contact(driver, contact)
        self.logout(driver)

    def logout(self, driver):
        """Выход из системы"""
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self, driver):
        """Возврат на страницу групп"""
        driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, driver, group):
        """Создание группы"""
        # Инициализация создания группы
        driver.find_element(By.NAME, "new").click()

        # Заполнение формы группы
        self.type(driver, By.NAME, "group_name", group.name)
        self.type(driver, By.NAME, "group_header", group.header)
        self.type(driver, By.NAME, "group_footer", group.footer)

        # Подтверждение создания группы
        driver.find_element(By.NAME, "submit").click()

    def open_contact_page(self, driver):
        """Открытие страницы добавления контакта"""
        driver.find_element(By.LINK_TEXT, "add new").click()

    def create_contact(self, driver, contact):
        """Создание контакта"""
        # Заполнение формы контакта
        self.type(driver, By.NAME, "firstname", contact.firstname)
        self.type(driver, By.NAME, "middlename", contact.middlename)
        self.type(driver, By.NAME, "lastname", contact.lastname)
        self.type(driver, By.NAME, "nickname", contact.nickname)
        self.type(driver, By.NAME, "title", contact.title)
        self.type(driver, By.NAME, "company", contact.company)
        self.type(driver, By.NAME, "address", contact.address)
        self.type(driver, By.NAME, "home", contact.home)
        self.type(driver, By.NAME, "mobile", contact.mobile)
        self.type(driver, By.NAME, "work", contact.work)
        self.type(driver, By.NAME, "fax", contact.fax)
        self.type(driver, By.NAME, "email", contact.email)
        self.type(driver, By.NAME, "email2", contact.email2)
        self.type(driver, By.NAME, "email3", contact.email3)
        self.type(driver, By.NAME, "homepage", contact.homepage)

        # Выбор даты рождения
        Select(driver.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        Select(driver.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        self.type(driver, By.NAME, "byear", contact.byear)

        # Выбор даты годовщины
        Select(driver.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
        Select(driver.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
        self.type(driver, By.NAME, "ayear", contact.ayear)

        # Выбор группы
        Select(driver.find_element(By.NAME, "new_group")).select_by_visible_text(contact.group)

        # Подтверждение создания контакта
        driver.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()

    def type(self, driver, locator_type, locator, text):
        """Вспомогательный метод для ввода текста"""
        if text is not None:
            driver.find_element(locator_type, locator).clear()
            driver.find_element(locator_type, locator).send_keys(text)

    def open_group_page(self, driver):
        """Открытие страницы групп"""
        driver.get(self.base_url + "group.php")

    def login(self, driver):
        """Авторизация"""
        driver.get(self.base_url)  # Открываем главную страницу
        self.type(driver, By.NAME, "user", "admin")
        self.type(driver, By.NAME, "pass", "secret")
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

        # Проверка успешной авторизации
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))

    def open_home_page(self, driver):
        """Открытие домашней страницы"""
        driver.get(self.base_url)

    def tearDown(self):
        """Завершение теста"""
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()