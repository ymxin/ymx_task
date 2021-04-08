#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-28 15:12
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_sign.py
from appium_demo.page.app2 import App2
from appium_demo.page.information_page import InformationPage


class TestSign:

    def setup(self):
        # self.information_page = InformationPage()
        self.app = App2()

    def test_sign(self):
        self.app.goto_main().goto_work_page().goto_sign_page().sign()
