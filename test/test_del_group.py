
# test/test_del_group.py
import pytest
from confest import app
from model.group import Group
def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test", header="test", footer="test"))
    app.group.delete_first_group()
