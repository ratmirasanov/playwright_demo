"""Module LoginPage for mapping the login page."""


class LoginPage:
    """Class LoginPage for mapping the login page."""

    def __init__(self, page):
        """Constructor."""
        self.page = page

    # Mapping web elements on the page.
    @property
    def login_form(self):
        return self.page.wait_for_selector(".form")

    @property
    def username_field(self):
        return self.login_form.wait_for_selector("#id_username")

    @property
    def password_field(self):
        return self.login_form.wait_for_selector("#id_password")

    @property
    def login_button(self):
        return self.login_form.wait_for_selector("button[name='submit']")

    def login(self, user):
        """A method for login into the application."""
        self.username_field.fill(user["username"])
        self.password_field.fill(user["password"])
        self.login_button.click()
