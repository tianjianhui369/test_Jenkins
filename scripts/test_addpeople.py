from time import sleep
import pytest

from base.base_data import base_data
from base.get_driver import get_driver
from page.page import Page

class TestAddPeople:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)
    def teardown(self):
        self.driver.quit()

    # """
    # allure版本是2.9.0
    # pip安装的不是pytest-allure-adaptor
    # 而是allure-pytest，最新版配最新版，如果版本不一致也不可能显示出报告
    # """
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("args",base_data("data.yaml","test_contact"))
    def test_addPeople(self,args):
        self.page.page_index().page_click_add()
        self.page.page_add().page_input_name(args["name"])
        self.page.page_add().page_input_phone(args["phone"])
        self.page.page_add().page_click_back()
        sleep(2)