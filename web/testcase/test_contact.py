#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-10 9:08
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_contact.py
import yaml

from web.page.main_page import MainPage

with open("./contact.yaml", encoding="utf-8") as f:
    datas = yaml.safe_load(f)
    username = datas['username']
    print(username)
    account = datas['account']
    print(account)
    phonenum = datas['phonenum']
    print(phonenum)


class TestContact:

    def setup(self):
        self.mainpage = MainPage()

    def teardown(self):
        pass

    def test_contact(self):
        self.username = username
        self.account = account
        self.phonenum = phonenum
        page = self.mainpage.goto_add_member()
        page.add_member(username, account, phonenum)
        names = page.get_member()
        print(names)
        assert username in names
