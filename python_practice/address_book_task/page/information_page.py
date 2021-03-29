#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-28 20:32
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : information_page.py
from address_book_task.page.address_book_page import AddressBookPage
from address_book_task.page.basepage import BasePage


class InformationPage(BasePage):

    def goto_address_book(self):
        self.parse_action("../page/information_page.yaml", "goto_address_book")
        return AddressBookPage(self.driver)
