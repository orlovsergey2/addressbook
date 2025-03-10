# test/test_add_contact.py
import pytest
from application.application import Application
from confest import app
from utils.contact_input import load_contact_from_json
from model.contact import Contact
from confest import app
from utils.contact_input import load_contact_from_json
def test_add_contact(app):
    """Тест для добавления контакта."""
    old_contacts = app.contact.get_contact_list()
    print(f"Old contacts before addition: {old_contacts}")

    contact = load_contact_from_json("utils/contact_data.json")  # Загружаем данные и создаем объект группы
    app.contact.create_contact(contact)

    # Обновление идентификатора контакта
    contact.id = str(max(int(c.id) for c in old_contacts) + 1)


    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    print(f"New contacts after addition: {new_contacts}")

    old_contacts.append(contact)
    print(f"Appended old contacts: {old_contacts}")

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.contact.return_to_contact_page()
