import pytest
from model.group import Group


def test_add_group(app, group_data):
    """Тест для добавления группы"""
    old_groups = app.group.get_group_list()
    app.group.create_group(group_data)

    # Проверки
    assert app.group.count() == len(old_groups) + 1
    new_groups = app.group.get_group_list()
    old_groups.append(group_data)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)