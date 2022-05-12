import allure

import page
from base.base import Base


class PageAdd(Base):
    @allure.step(title="输入姓名")
    def page_input_name(self,name):
        allure.attach("写","写姓名",allure.attachment_type.TEXT)
        self.base_input(page.add_name,name)

    @allure.step(title="输入电话")
    def page_input_phone(self,phone):
        allure.attach("写","写电话",allure.attachment_type.TEXT)
        self.base_input(page.add_phone,phone)
    @allure.step(title="点击返回")
    def page_click_back(self):
        allure.attach("点","点返回",allure.attachment_type.TEXT)
        self.base_click(page.add_back)
        allure.attach("通讯录截图",self.driver.get_screenshot_as_png(),allure.attachment_type.PNG)