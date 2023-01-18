"""Module class ProfilePage for mapping the profile page."""


class ProfilePage:
    """Class ProfilePage for mapping the profile page."""

    def __init__(self, page):
        """Constructor."""
        self.page = page

    # Mapping web elements on the page.
    @property
    def username_value_field(self):
        return self.page.wait_for_selector("span.navbar-text")
