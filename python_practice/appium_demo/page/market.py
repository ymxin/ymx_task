#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-19 8:36
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : market.py
from appium_demo.page.base_page import BasePage
from appium_demo.page.search import Search


class Market(BasePage):

    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)
