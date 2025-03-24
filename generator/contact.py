import json
import random
import string
import os.path
import getopt
import sys
from model.contact import Contact

# Обработка аргументов командной строки
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    print(str(err))
    print("Usage: generate_contacts.py -n <number> -f <output_file>")
    sys.exit(2)

# Параметры по умолчанию
n = 5  # Количество контактов
f = "../data/contacts.json"  # Файл для сохранения

# Разбор аргументов командной строки
for opt, arg in opts:
    if opt == "-n":
        n = int(arg)
    elif opt == "-f":
        f = arg

def random_string(prefix, maxlen):
    """Генерация случайной строки"""
    symbols = string.ascii_letters + string.digits + " " * 5
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])

def random_phone():
    """Генерация случайного телефонного номера"""
    return "+" + "".join([str(random.randint(0, 9)) for _ in range(11)])

def random_email():
    """Генерация случайного email"""
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "example.com"]
    return random_string("user", 10) + "@" + random.choice(domains)

def random_date(part):
    """Генерация случайной даты"""
    if part == "day":
        return str(random.randint(1, 28))
    elif part == "month":
        return random.choice(["January", "February", "March", "April", "May", "June",
                            "July", "August", "September", "October", "November", "December"])
    elif part == "year":
        return str(random.randint(1900, 2023))

def contact_to_dict(contact):
    """Преобразует объект Contact в словарь"""
    return {
        'firstname': contact.firstname,
        'lastname': contact.lastname,
        'address': contact.address,
        'homephone': contact.homephone,
        'mobilephone': contact.mobilephone,
        'workphone': contact.workphone,
        'email': contact.email,
        'email2': contact.email2,
        'email3': contact.email3,
        'bday': contact.bday,
        'bmonth': contact.bmonth,
        'byear': contact.byear,
        'aday': contact.aday,
        'amonth': contact.amonth,
        'ayear': contact.ayear
    }

# Генерация тестовых данных
testdata = [
    Contact(
        firstname="",
        lastname="",
        address="",
        homephone="",
        mobilephone="",
        workphone="",
        email="",
        email2="",
        email3=""
    )
] + [
    Contact(
        firstname=random_string("firstname", 10),
        lastname=random_string("lastname", 10),
        address=random_string("address", 20),
        homephone=random_phone(),
        mobilephone=random_phone(),
        workphone=random_phone(),
        email=random_email(),
        email2=random_email(),
        email3=random_email(),
        bday=random_date("day"),
        bmonth=random_date("month"),
        byear=random_date("year"),
        aday=random_date("day"),
        amonth=random_date("month"),
        ayear=random_date("year")
    )
    for _ in range(n)
]

# Преобразование объектов Contact в словари
testdata_dicts = [contact_to_dict(contact) for contact in testdata]

# Создание директории, если её нет
os.makedirs(os.path.dirname(f), exist_ok=True)

# Сохранение в JSON файл
with open(f, "w", encoding="utf-8") as out:
    json.dump(testdata_dicts, out, indent=2, ensure_ascii=False)

print(f"Сгенерировано {n+1} контактов и сохранено в {f}")