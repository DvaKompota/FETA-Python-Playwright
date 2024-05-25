from .base_page import BasePage


class DocsIntroPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.installation_heading = self.page.get_by_role("heading", name="Installation")

    def wait_for_installation_heading(self):
        self.installation_heading.wait_for(state="visible")
