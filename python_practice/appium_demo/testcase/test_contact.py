#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-31 22:10
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_contact.py
from appium_demo.page.app2 import App2


class TestContact:

    def setup(self):
        self.app = App2()

    def test_contact(self):
        name = 'aa_015'
        phone_num = '17623456765'

        edit_page = self.app.goto_main().goto_addressList().click_addcontact().addContact_menual()
        edit_page.exit_contact(name, phone_num)
        edit_page.verify_ok()
