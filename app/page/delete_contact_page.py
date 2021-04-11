#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-04-11 11:20
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : delete_contact_page.py
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage


class DeleteContactPage(BasePage):
    # 删除成员
    def delete_contact(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        self.parse_action("../page/delete_contact_page.yaml", "delete_contact")

    # 点击删除确认弹窗：确定
    def confirm_delete_popup(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="确定"]').click()
        self.parse_action("../page/delete_contact_page.yaml", "confirm_delete_popup")
