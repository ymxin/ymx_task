#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-19 8:40
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : search.py
from appium_demo.page.base_page import BasePage


class Search(BasePage):

    def search(self, value):
        self._params["value"] = value
        self.steps("../page/search.yaml")
