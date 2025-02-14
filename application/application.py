from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from .contact_helper import ContactHelper
from .group_helper import GroupHelper
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

