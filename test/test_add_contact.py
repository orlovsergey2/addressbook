import pytest
from application.application import Application
from confest import app
from model.contact import Contact
from selenium.webdriver.support.ui import Select
import random
import string

# Функция для генерации случайных строк
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# Функция для генерации случайных чисел
def random_number(min_value, max_value):
    return str(random.randint(min_value, max_value))

# Функция для генерации случайных дат
def random_date():
    day = random_number(1, 28)  # Ограничиваем до 28, чтобы избежать проблем с февралем
    month = random.choice(["January", "February", "March", "April", "May", "June",
                          "July", "August", "September", "October", "November", "December"])
    year = random_number(1900, 2023)
    return day, month, year

# Тестовые данные для контактов
testdata_contacts = [
    Contact(firstname="", lastname="", address="", homephone="", email="",
            bday="", bmonth="", byear="", aday="", amonth="", ayear="")
] + [
    Contact(
        firstname=random_string("firstname", 10),
        lastname=random_string("lastname", 10),
        address=random_string("address", 20),
        homephone=random_string("homephone", 10),
        email=random_string("email", 15),
        bday=random_date()[0],  # Случайный день
        bmonth=random_date()[1],  # Случайный месяц
        byear=random_date()[2],  # Случайный год
        aday=random_date()[0],  # Случайный день
        amonth=random_date()[1],  # Случайный месяц
        ayear=random_date()[2]  # Случайный год
    )
    for i in range(5)  # 5 контактов со случайными данными
]

def normalize_contact_data(contact):
    """Нормализация данных контакта (удаление лишних пробелов и специальных символов)."""
    if contact.firstname is not None:
        contact.firstname = " ".join(contact.firstname.split()).strip()
    if contact.lastname is not None:
        contact.lastname = " ".join(contact.lastname.split()).strip()
    if contact.address is not None:
        contact.address = " ".join(contact.address.split()).strip()
    if contact.homephone is not None:
        contact.homephone = " ".join(contact.homephone.split()).strip()
    if contact.email is not None:
        contact.email = " ".join(contact.email.split()).strip()
    return contact

@pytest.mark.parametrize("contact", testdata_contacts, ids=[repr(x) for x in testdata_contacts])
def test_add_contact(app, contact):
    """Тест для добавления контакта."""
    old_contacts = app.contact.get_contact_list()
    print(f"Old contacts before addition: {old_contacts}")

    # Создание контакта
    app.contact.create_contact(contact)

    # Обновление идентификатора контакта
    contact.id = str(max(int(c.id) for c in old_contacts) + 1)

    # Проверка, что количество контактов увеличилось на 1
    new_count = app.contact.count()
    print(f"New count: {new_count}")
    assert len(old_contacts) + 1 == new_count

    # Получение нового списка контактов
    new_contacts = app.contact.get_contact_list()
    print(f"New contacts after addition: {new_contacts}")

    # Добавление созданного контакта в старый список
    old_contacts.append(contact)
    print(f"Appended old contacts: {old_contacts}")

    # Нормализация данных перед сравнением
    old_contacts = [normalize_contact_data(c) for c in old_contacts]
    new_contacts = [normalize_contact_data(c) for c in new_contacts]

    # Проверка, что списки контактов совпадают
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    # Возврат на страницу контактов
    app.contact.return_to_contact_page()