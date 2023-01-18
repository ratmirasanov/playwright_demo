"""Module HomePage for mapping the home page."""


class HomePage:
    """Class HomePage for mapping the home page."""

    def __init__(self, page):
        """Constructor."""
        self.page = page

    # Mapping web elements on the page.
    @property
    def login_link(self):
        return self.page.wait_for_selector("a[href*='login']")

    def go_to_login_page(self):
        """A method for opening the login page."""
        self.login_link.click()
