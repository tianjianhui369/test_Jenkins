from base.get_driver import get_driver
from page.page_add import PageAdd
from page.page_index import PageIndex

class Page:
    def __init__(self,driver):
        self.driver = driver
    def page_add(self):
        return PageAdd(self.driver)
    def page_index(self):
        return PageIndex(self.driver)
