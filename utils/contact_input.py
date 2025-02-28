# utils/contact_input.py
import json
from model.contact import Contact

def load_contact_from_json(file_path):
    """Загружает данные контакта из JSON-файла и возвращает объект Contact."""
    with open(file_path, "r", encoding="utf-8") as file:
        contact_data = json.load(file)
    return Contact(**contact_data)

def input_contact_data():
    """Функция для ввода данных контакта и сохранения их в JSON-файл."""
    print("\nДобавление нового контакта:")
    contact_data = {
        "firstname": input("Введите имя: "),
        "middlename": input("Введите отчество: "),
        "lastname": input("Введите фамилию: "),
        "nickname": input("Введите никнейм: "),
        "title": input("Введите заголовок: "),
        "company": input("Введите компанию: "),
        "address": input("Введите адрес: "),
        "home": input("Введите домашний телефон: "),
        "mobile": input("Введите мобильный телефон: "),
        "work": input("Введите рабочий телефон: "),
        "fax": input("Введите факс: "),
        "email": input("Введите email: "),
        "email2": input("Введите второй email: "),
        "email3": input("Введите третий email: "),
        "homepage": input("Введите домашнюю страницу: "),
        "bday": input("Введите день рождения (число): "),
        "bmonth": input("Введите месяц рождения (название): "),
        "byear": input("Введите год рождения: "),
        "aday": input("Введите день годовщины (число): "),
        "amonth": input("Введите месяц годовщины (название): "),
        "ayear": input("Введите год годовщины: ")
    }

    # Сохраняем данные в JSON-файл
    with open("contact_data.json", "w", encoding="utf-8") as file:
        json.dump(contact_data, file, ensure_ascii=False, indent=4)

    print("Данные контакта сохранены в файл 'contact_data.json'.")
if __name__ == "__main__":
    input_contact_data()