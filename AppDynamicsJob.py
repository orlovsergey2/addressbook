# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import unittest


# Вспомогательный класс для хранения свойств группы
class Group:
    def __init__(self, name=None, header=None, footer=None):
        self.name = name
        self.header = header
        self.footer = footer


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost/addressbook/addressbook/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.delete_all_cookies()  # Очистка куки

    def test_add_group(self):
        driver = self.driver

        # Инициализация тестовых данных
        group = Group(name="Test Group", header="Header", footer="Footer")

        # Выполнение теста
        self.open_home_page(driver)
        self.login(driver)
        self.open_group_page(driver)
        self.create_group(driver, group)
        self.return_to_groups_page(driver)
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