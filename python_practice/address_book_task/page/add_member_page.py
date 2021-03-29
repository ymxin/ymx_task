#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-28 20:34
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : add_member_page.py
from address_book_task.page.add_for_manual_input_page import AddForManualInputPage
from address_book_task.page.basepage import BasePage


class AddMemberPage(BasePage):

    def goto_add_for_manual_input(self):
        self.parse_action("../page/add_member_page.yaml", "goto_add_for_manual_input")
        return AddForManualInputPage(self.driver)
