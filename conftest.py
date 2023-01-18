"""Module conftest for pytest."""

import pytest
from playwright.sync_api import Playwright

import settings


@pytest.fixture
def browser(playwright: Playwright):
    """Function (fixture) for launching and closing the browser."""
    chromedriver = playwright.chromium.launch(headless=False)
    page = chromedriver.new_page()
    page.goto(settings.BASE_URL)
    yield page
    page.close()
    chromedriver.close()
