#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-28 20:36
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : add_for_manual_input_page.py
from appium.webdriver.common.mobileby import MobileBy

from address_book_task.page.basepage import BasePage
from address_book_task.page.full_input_page import FullInputPage
from address_book_task.page.quick_input_page import QuickInputPage


class AddForManualInputPage(BasePage):

    def goto_quick_input(self):
        self.parse_action("../page/add_for_manual_input_page.yaml", "goto_quick_input")
        # return QuickInputPage(self.driver)

    def goto_full_input(self):
        self.parse_action("../page/add_for_manual_input_page.yaml", "goto_full_input")
        # return FullInputPage(self.driver)

    def is_quick_or_full__page(self):

        if self.driver.find_element(MobileBy.XPATH, "//*[@text='快速输入']"):
            self.goto_full_input()

        elif self.driver.find_element(MobileBy.XPATH, "//*[@text='完整输入']"):
            self.goto_quick_input()
