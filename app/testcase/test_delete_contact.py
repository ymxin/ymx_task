#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-04-11 11:56
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_delete_contact.py
from app.page.app import App


class TestDeleteContact:

    def setup(self):
        self.app = App()

    def test_delete_contact(self):
        delete_page = self.app.goto_main().goto_manage_contacts().goto_edit_contact().goto_delete_contact()
        delete_page.delete_contact()
        delete_page.confirm_delete_popup()
