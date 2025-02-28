# test/test_add_contact.py
import pytest
from application.application import Application
from confest import app
from utils.contact_input import load_contact_from_json
def test_add_contact(app):
    """Тест для добавления контакта."""

    # Загружаем данные контакта из JSON-файла
    contact = load_contact_from_json("utils/contact_data.json")
    # Создаем контакт в приложении
    app.contact.create_contact(contact)