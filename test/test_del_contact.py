import pytest
from model.contact import Contact
from confest import app
from utils.contact_input import load_contact_from_json
def test_del_contact(app):
    if app.contact.count() == 0:
        contact = load_contact_from_json("utils/contact_data.json")
        app.contact.create_contact(contact)
    app.contact.delete_first_contact()
