#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-28 20:33
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : address_book_page.py
from address_book_task.page.add_member_page import AddMemberPage
from address_book_task.page.basepage import BasePage


class AddressBookPage(BasePage):

    def goto_add_member(self):
        self.parse_action("../page/address_book_page.yaml", "goto_add_member")
        return AddMemberPage(self.driver)
