# AppDynamicsJob.py
import pytest
from application import Application, Contact, Group  # Импортируем класс Application
from confest import app
# Тест, который добавляет контакт и группу
def test_add_contact_and_group(app):
    """Тест для добавления контакта и группы"""
    # Авторизация
    app.login()

    # Добавление контакта
    contact = Contact(
        firstname="Sergey",
        middlename="Sergeevich",
        lastname="Orlov",
        nickname="ORLOV_Sergey",
        title=u"ВУЗ",
        company=u"СиБАДИ",
        address=u"Печальная область, тоскливый район, проспект разочарования, дом 13",
        home="1",
        mobile="88005553535",
        work=u"бездельник",
        fax=u"не имеется",
        email=u"выавып",
        email2=u"ываввы",
        email3=u"ыавыа",
        homepage=u"выаыв",
        bday="12",
        bmonth="August",
        byear="2005",
        aday="12",
        amonth="August",
        ayear="2005"
    )
    app.contact.create_contact(contact)

    # Добавление группы
    app.group.open_group_page()
    group = Group(name="Test Group", header="Header", footer="Footer")
    app.group.create_group(group)
    app.group.return_to_groups_page()