from model.contact import Contact
from confest import app
from utils.contact_input import load_contact_from_json
def test_modify_contact_name(app):
    """Тест для изменения имени контакта."""
    contact = load_contact_from_json("utils/contact_data.json")
    app.contact.modify_contact(contact)