from model.group import Group
from confest import app
def test_modify_group_name(app):
    """Тест для изменения имени группы."""
    # Модифицируем имя группы
    new_group = Group(
        name="New group name",
        header="New group header",
        footer="New group footer")
    app.group.modify(new_group)



