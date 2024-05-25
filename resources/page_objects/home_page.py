from .base_page import BasePage


class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.get_started_link = self.page.get_by_role("link", name="Get started")

    def load_page(self):
        self.page.goto(self.url)

    def get_started(self):
        self.get_started_link.click()
