import allure

import page
from base.base import Base


class PageIndex(Base):
    @allure.step(title="点击新增")
    def page_click_add(self):
        allure.attach("点","点击新增",allure.attachment_type.TEXT)
        self.base_click(page.index_add)