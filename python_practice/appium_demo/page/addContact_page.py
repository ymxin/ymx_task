#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-31 21:25
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : addContact_page.py
from appium_demo.page.base_page2 import BasePage2
from appium_demo.page.editContact_page import EditContactPage


class AddContactPage(BasePage2):

    def addContact_menual(self):
        # 点击手动添加
        self.parse_action("../page/addContact_page.yaml", "addContact_menual")

        return EditContactPage(self.driver)
