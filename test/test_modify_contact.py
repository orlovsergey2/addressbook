from model.contact import Contact
from confest import app
from utils.contact_input import load_contact_from_json
from random import randrange


def test_modify_contact_name(app):
    """Тест для изменения имени контакта."""
    if app.contact.count() == 0:
        contact = Contact(firstname="Иван", lastname="Иванов")
        app.contact.create_contact(contact)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    new_contact = Contact(
        firstname="Новое Имя",
        middlename="Новый Отчество",
        lastname="Новая Фамилия",
        nickname="Новое Прозвище",
        title="Новый Титул",
        company="Новая Компания",
        address="Новый Адрес",
        home="Новый Дом",
        mobile="Новый Мобильный",
        work="Новый Рабочий",
        fax="Новый Факс",
        email="Новый Электронный",
        email2="Новый Электронный2",
        email3="Новый Электронный3",
        homepage="Новый ГлавнаяСтраница",
        bday="12",
        bmonth="August",
        byear="2005",
        aday="12",
        amonth="August",
        ayear="2005",
        id=old_contacts[index].id
    )
    app.contact.modify_contact(new_contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.group.get_group_list()
    old_contacts[index] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)