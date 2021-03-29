#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-29 21:27
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_add_member.py
from address_book_task.page.app import App


class TestAddMember:

    def setup(self):
        self.app = App()

    def test_add_member(self):
        self.app.goto_main().goto_address_book().goto_add_member().goto_add_for_manual_input().is_quick_or_full__page()
