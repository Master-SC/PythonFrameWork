import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
from tests.home.login_test import login_page


@pytest.fixture()
def setup():
    print("Running Method level setup")
    yield
    print("Running Method level teardown")


@pytest.fixture(scope='class')
def oneTimeSetup(request, browser, ostype):
    print("Running One time setup")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running One time teardown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--ostype", help="Type of Operation System")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def ostype(request):
    return request.config.getoption("--ostype")
