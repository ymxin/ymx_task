#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-08 20:39
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_register.py
from web.page.index_page import IndexPage


class TestRegister:

    def setup(self):
        self.index = IndexPage()

    def test_register(self):
        assert self.index.goto_login().goto_register()

    def teardown(self):
        self.index.driver.quit()
