import pytest
from model.contact import Contact
from confest import app
from utils.contact_input import load_contact_from_json
from random import randrange
def test_del_contact(app):
    if app.contact.count() == 0:
        contact = load_contact_from_json("utils/contact_data.json")
        app.contact.create_contact(contact)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts