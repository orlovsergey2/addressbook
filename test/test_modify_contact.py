from model.contact import Contact
from confest import app
from utils.contact_input import load_contact_from_json
from random import randrange


def test_modify_contact_name(app):
    """Тест для изменения имени контакта."""
    # Если контактов нет, создаем новый
    if app.contact.count() == 0:
        contact = load_contact_from_json("utils/contact_data.json")
        app.contact.create_contact(contact)

    # Загружаем старый список контактов
    old_contacts = app.contact.get_contact_list()

    # Выбираем случайный индекс для модификации
    index = randrange(len(old_contacts))

    # Создаем новый контакт с обновленными данными
    contact = Contact(
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
        id=old_contacts[index].id  # Сохраняем id контакта для модификации
    )

    # Модифицируем контакт
    app.contact.modify_contact(index, contact)

    # Проверяем, что количество контактов не изменилось
    assert len(old_contacts) == app.contact.count()

    # Загружаем новый список контактов
    new_contacts = app.contact.get_contact_list()

    # Находим измененный контакт в новом списке по id
    modified_contact = None
    for new_contact in new_contacts:
        if new_contact.id == contact.id:
            modified_contact = new_contact
            break

    # Обновляем старый список контактов
    old_contacts[index] = modified_contact

    # Сравниваем списки контактов
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
