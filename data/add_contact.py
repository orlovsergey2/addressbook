import random
import string
from model.contact import Contact
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
