#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-19 8:48
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_search.py
from appium_demo.page.app import App


class TestSearch:

    def test_search(self):
        App().start().main().goto_market().goto_search().search("jd")
