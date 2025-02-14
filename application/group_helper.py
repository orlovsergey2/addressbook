from selenium.webdriver.common.by import By

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