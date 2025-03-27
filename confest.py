import pytest
import json
import os
from application.application import Application
from application.db import DbFixture

# Global variables
target = None
fixture = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook")


@pytest.fixture
def app(request):
    global fixture
    global target

    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")

    if target is None:
        config_file = request.config.getoption("--target")
        target = load_config(config_file)

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=base_url)

    fixture.session.ensure_login(username=target['username'], password=target['password'])
    yield fixture
    fixture.session.ensure_logout()


@pytest.fixture
def group_data():
    return Group(name="Test Group")


@pytest.fixture
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = DbFixture(
        host=db_config["host"],
        name=db_config["name"],
        user=db_config["user"],
        password=db_config["password"]
    )
    yield dbfixture
    dbfixture.destroy()


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check-ui")
