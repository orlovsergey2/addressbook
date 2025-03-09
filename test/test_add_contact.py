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
    contact = load_contact_from_json("utils/contact_data.json")
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)

    # Сравниваем списки, не учитывая порядок
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
