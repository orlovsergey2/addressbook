import pytest
from application.application import Application  # Импортируем класс Application
from selenium.webdriver.common.by import By
from confest import app
def test_del_contact(app):
    """Тест для удаления контакта"""
    app.login()
    app.driver.find_element(By.NAME, "selected[]").click()  # Выбор группы
    app.driver.find_element(By.XPATH, "//input[@value='Delete']").click()
    app.contact.open_contact_page()