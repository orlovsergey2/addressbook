from model.group import Group
from confest import app
from random import randrange
def test_modify_group_name(app):
    """Тест для изменения имени группы."""
    if app.group.count() == 0:
        app.group.create_group(Group(name="test", header="test", footer="test"))
    # Модифицируем имя группы
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    new_group = Group(
        name="New group name",
        header="New group header",
        footer="New group footer",
        id = old_groups[index].id)
    app.group.modify(new_group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)