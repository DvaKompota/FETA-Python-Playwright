from ..page_objects.home_page import HomePage
from ..page_objects.docs_inro_page import DocsIntroPage


class UIFixture:
    def __init__(self, page):
        self.home = HomePage(page)
        self.intro = DocsIntroPage(page)
