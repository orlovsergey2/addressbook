from model.contact import Contact
from confest import app

def test_modify_contact_name(app):
    """Тест для изменения имени контакта."""

    new_contact = Contact(
        firstname="NewFirstName",
        middlename="NewMiddleName",
        lastname="NewLastName",
        nickname="NewNickname",
        title="NewTitle",
        company="NewCompany",
        address="NewAddress",
        home="NewHomePhone",
        mobile="88005553535",
        work="бездельник",
        fax="не имеется",
        email="newemail@example.com",
        email2="newemail2@example.com",
        email3="newemail3@example.com",
        homepage="newhomepage.com",
        bday="18",
        bmonth="September",
        byear="2004",
        aday="14",
        amonth="February",
        ayear="2001"
    )

    # Модифицируем контакт
    app.contact.modify_contact(new_contact)
