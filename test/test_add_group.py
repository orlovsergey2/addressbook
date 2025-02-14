# test/test_add_group.py
import pytest
from application.application import Application  # Импортируем класс Application
from model.group import Group
from confest import app
def test_add_group(app):
    """Тест для добавления группы"""
    app.login()
    group = Group(name="Test Group", header="Header", footer="Footer")
    app.group.create_group(group)
    app.group.return_to_groups_page()