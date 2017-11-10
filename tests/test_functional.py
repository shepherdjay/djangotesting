import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()


def test_basic(live_server, browser):
    browser.get(live_server.url)
    assert 'Hello World' in browser.title
