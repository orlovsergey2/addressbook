import json
from model.group import Group

def load_group_from_json(file_path):
    """Загружает данные группы из JSON-файла и возвращает объект Group."""
    with open(file_path, "r", encoding="utf-8") as file:
        group_data = json.load(file)
    return Group(**group_data)
def input_group_data():
    """Функция для ввода данных группы и сохранения их в JSON-файл."""
    print("\nДобавление новой группы:")
    group_data = {
        "name": input("Введите имя: "),
        "header": input("Введите заголовок: "),
        "footer": input("Введите подвал: ")
    }

    # Сохраняем данные в JSON-файл
    with open("group_data.json", "w", encoding="utf-8") as file:
        json.dump(group_data, file, ensure_ascii=False, indent=4)

    print("Данные группы сохранены в файл 'group_data.json'.")
if __name__ == "__main__":
    input_group_data()