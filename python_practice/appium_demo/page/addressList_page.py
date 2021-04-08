#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-31 21:19
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : addressList_page.py
from appium_demo.page.addContact_page import AddContactPage
from appium_demo.page.base_page2 import BasePage2


class AddressListPage(BasePage2):
    def click_addcontact(self):
        # 点击添加成员
        self.parse_action("../page/addressList_page.yaml", "click_addcontact")
        # 需要使用一个driver，复用;;;用return是因为链式调用
        return AddContactPage(self.driver)
