import pytest
from playwright.sync_api import sync_playwright
from resources.fixtures.ui_fixture import UIFixture


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


@pytest.fixture
def ui(browser):
    context = browser.new_context()
    page = context.new_page()
    ui_fixture = UIFixture(page)
    yield ui_fixture
    context.close()
