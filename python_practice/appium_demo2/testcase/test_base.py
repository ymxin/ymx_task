#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-30 22:07
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_base.py
from appium_demo2.page.app import App


class TestBase:
    app = None

    def setup(self):
        self.app = App()
