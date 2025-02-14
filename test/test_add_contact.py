# test/test_add_contact.py
import pytest
from application.application import Application
from confest import app
from model.contact import Contact
def test_add_contact(app):
    """Тест для добавления контакта"""
    app.login()
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