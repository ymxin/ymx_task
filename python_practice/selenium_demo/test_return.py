#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-06 19:26
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_return.py
from selenium_demo.mian import Main


class TestReturn:
    def setup(self):
        main = Main()
        main.click_first_link().title()
