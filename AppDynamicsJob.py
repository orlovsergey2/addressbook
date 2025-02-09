# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import unittest

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
        self.open_home_page(driver)
        self.login(driver)
        self.open_group_page(driver)  # Исправлено название метода
        self.create_group(driver)
        self.return_to_groups_page(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self, driver):
        driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, driver):
        # init group creation
        driver.find_element(By.NAME, "new").click()

        # fill group form
        driver.find_element(By.NAME, "group_name").clear()
        driver.find_element(By.NAME, "group_name").send_keys("adad")

        driver.find_element(By.NAME, "group_header").clear()
        driver.find_element(By.NAME, "group_header").send_keys("adada")

        driver.find_element(By.NAME, "group_footer").clear()
        driver.find_element(By.NAME, "group_footer").send_keys("adada")

        # submit group creation
        driver.find_element(By.NAME, "submit").click()

    def open_group_page(self, driver):  # Исправлено название метода
         driver.get(self.base_url + "group.php") # Открываем group.php

    def login(self, driver):
        driver.get(self.base_url)  # Открываем главную страницу
        driver.find_element(By.NAME, "user").clear()
        driver.find_element(By.NAME, "user").send_keys("admin")

        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys("secret")

        driver.find_element(By.XPATH, "//input[@value='Login']").click()
        #Проверяем, что появились элементы после логина
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))

    def open_home_page(self, driver):
         pass # Удаляем, больше не нужен

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
