from selenium.webdriver.common.by import By

# Класс-помощник для работы с группами
class GroupHelper:
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def open_group_page(self):
        if not (self.driver.current_url.endswith("/group.php") and len(self.driver.find_elements(By.NAME, "new")) > 0):
            self.driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        """Создание группы"""
        self.open_group_page()
        self.app.driver.find_element(By.NAME, "new").click()
        self.app.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.app.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.app.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        self.app.driver.find_element(By.NAME, "submit").click()

    def select_first_group(self):
        """Выбирает первую группу."""
        self.open_group_page()
        self.app.driver.find_element(By.NAME, "selected[]").click()

    def modify(self, group):
        """Модифицирует группу, изменя только переданные поля."""
        self.select_first_group()
        self.app.driver.find_element(By.NAME, "edit").click()

        # Получаем текущие значения полей группы
        current_name = self.app.driver.find_element(By.NAME, "group_name").get_attribute("value")
        current_header = self.app.driver.find_element(By.NAME, "group_header").get_attribute("value")
        current_footer = self.app.driver.find_element(By.NAME, "group_footer").get_attribute("value")

        # Если новое значение передано, используем его, иначе оставляем текущее
        new_name = group.name if group.name is not None else current_name
        new_header = group.header if group.header is not None else current_header
        new_footer = group.footer if group.footer is not None else current_footer

        # Заполняем форму с новыми значениями
        self.fill_group_form(new_name, new_header, new_footer)

        # Сохраняем изменения
        self.app.driver.find_element(By.NAME, "update").click()
        self.return_to_groups_page()

    def fill_group_form(self, name, header, footer):
        """Модифицирует имя группы."""
        self.app.driver.find_element(By.NAME, "group_name").clear()
        self.app.driver.find_element(By.NAME, "group_name").send_keys(name)
        self.app.driver.find_element(By.NAME, "group_header").clear()
        self.app.driver.find_element(By.NAME, "group_header").send_keys(header)
        self.app.driver.find_element(By.NAME, "group_footer").clear()
        self.app.driver.find_element(By.NAME, "group_footer").send_keys(footer)


    def return_to_groups_page(self):
        """Возврат на страницу групп"""
        # Проверяем, открыта ли уже страница групп
        if not (self.driver.current_url.endswith("/group.php") and len(self.driver.find_elements(By.NAME, "new")) > 0):
            self.app.driver.find_element(By.LINK_TEXT, "home").click()

    def delete_first_group(self):
        """Удаляет первую группу."""
        self.open_group_page()
        elements = self.app.driver.find_elements(By.NAME, "selected[]")
        if elements:
            elements[0].click()
            self.app.driver.find_element(By.NAME, "delete").click()
            self.return_to_groups_page()

    def count(self):
        """Возвращает количество групп."""
        self.open_group_page()
        return len(self.app.driver.find_elements(By.NAME, "selected[]"))