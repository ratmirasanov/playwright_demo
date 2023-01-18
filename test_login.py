"""Module TestLogin for testing login action to the application."""

import pytest

import settings
from pom.home_page import HomePage
from pom.login_page import LoginPage
from pom.profile_page import ProfilePage


class TestLogin:
    """Class TestLogin for testing login action to the application."""

    @pytest.mark.parametrize(
        "user", [settings.USER]
    )
    def test_valid_login(self, browser, user):
        """A method (test case) for testing a valid login action."""
        home_page = HomePage(browser)
        login_page = LoginPage(browser)
        profile_page = ProfilePage(browser)
        home_page.go_to_login_page()
        login_page.login(user)
        assert profile_page.username_value_field.is_visible() is True \
               and profile_page.username_value_field.text_content() == "Hello, admin."
