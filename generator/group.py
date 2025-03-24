import json
import random
import string
import os.path
import getopt
import sys
from model.group import Group

# Обработка аргументов командной строки
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    print(str(err))
    print("Usage: generate_groups.py -n <number> -f <output_file>")
    sys.exit(2)

# Параметры по умолчанию
n = 5  # Количество групп
f = "data/groups.json"  # Файл для сохранения

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

def group_to_dict(group):
    """Преобразует объект Group в словарь"""
    return {
        'name': group.name,
        'header': group.header,
        'footer': group.footer,
        'id': group.id
    }

# Генерация тестовых данных
testdata = [Group(name="", header="", footer="")] + [
    Group(
        name=random_string("name", 10),
        header=random_string("header", 20),
        footer=random_string("footer", 20)
    )
    for _ in range(n)
]

# Преобразование объектов Group в словари
testdata_dicts = [group_to_dict(group) for group in testdata]

# Создание директории, если её нет
os.makedirs(os.path.dirname(f), exist_ok=True)

# Сохранение в JSON файл
with open(f, "w", encoding="utf-8") as out:
    json.dump(testdata_dicts, out, indent=2, ensure_ascii=False)

print(f"Сгенерировано {n+1} групп и сохранено в {f}")