import pytest
import json
import os
from application.application import Application
from model.group import Group
from model.contact import Contact


# 1. Конфигурация приложения
def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json",
                     help="Path to config file")
    parser.addoption("--groups-data", action="store", default="data/groups.json",
                     help="Path to groups test data")
    parser.addoption("--contacts-data", action="store", default="data/contacts.json",
                     help="Path to contacts test data")


@pytest.fixture(scope="session")
def config(request):
    config_path = request.config.getoption("--config")
    if not os.path.exists(config_path):
        config_path = os.path.join(os.path.dirname(__file__), config_path)
        if not os.path.exists(config_path):
            pytest.skip(f"Config file not found: {config_path}")

    with open(config_path) as f:
        return json.load(f)


# 2. Фикстура приложения с конфигурацией
@pytest.fixture
def app(request, config):
    fixture = Application(
        base_url=config["web"]["base_url"],
        browser=config["web"]["browser"],
        group_data= config["data/groups.json"],
        contact_data=config["data/contacts.json"]
    )
    fixture.session.ensure_login(
        config["web"]["username"],
        config["web"]["password"]
    )

    def fin():
        fixture.session.ensure_logout()
        fixture.tear_down()

    request.addfinalizer(fin)

    return fixture


# 3. Загрузка тестовых данных и параметризация
def pytest_generate_tests(metafunc):
    def load_test_data(file_option, model_class):
        file_path = metafunc.config.getoption(file_option)
        if not os.path.exists(file_path):
            file_path = os.path.join(os.path.dirname(__file__), file_path)
            if not os.path.exists(file_path):
                pytest.skip(f"Test data file not found: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            return [model_class(**item) for item in json.load(f)]

    if "group_data" in metafunc.fixturenames:
        groups = load_test_data("--groups-data", Group)
        metafunc.parametrize("group_data", groups, ids=[str(g) for g in groups])

    if "contact_data" in metafunc.fixturenames:
        contacts = load_test_data("--contacts-data", Contact)
        metafunc.parametrize("contact_data", contacts, ids=[str(c) for c in contacts])