# test/test_add_group.py
import pytest
from application.application import Application  # Импортируем класс Application
from model.group import Group
from confest import app
from utils.group_input import load_group_from_json
def test_add_group(app):
    """Тест для добавления группы"""
    old_groups = app.group.get_group_list()
    group = load_group_from_json("utils/group_data.json")  # Загружаем данные и создаем объект группы
    app.group.create_group(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    app.group.return_to_groups_page()