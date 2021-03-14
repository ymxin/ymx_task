#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-06 21:48
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_register.py
from selenium_demo.page.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()

    def test_register(self):
        assert self.main.goto_register().register()
