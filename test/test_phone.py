import re
from confest import app
def clear(s):
    """Функция для очистки строки от лишних символов."""
    return re.sub("[() -]", "", s)


def test_contact_info_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
def test_contact_info_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def merge_phones_like_on_home_page(contact):
    phones = [
        contact.homephone,  # НовыйДом
        contact.mobilephone,  # НовыйМобильный
        contact.workphone,  # НовыйРабочий
        contact.secondaryphone  # (если есть)
    ]
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None, phones))))