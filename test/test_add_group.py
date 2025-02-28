# test/test_add_group.py
import pytest
from application.application import Application  # Импортируем класс Application
from model.group import Group
from confest import app
from utils.group_input import load_group_from_json
def test_add_group(app):
    """Тест для добавления группы"""
    group = load_group_from_json("utils/group_data.json")  # Загружаем данные и создаем объект группы
    app.group.create_group(group)
    app.group.return_to_groups_page()