#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-19 8:28
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : main.py
from appium_demo.page.base_page import BasePage
from appium_demo.page.market import Market


class Main(BasePage):
    def goto_market(self):
        # 这个steps是在testcase下调用的。所以要进入上一级目录
        self.steps("../page/main.yaml")
        return Market(self._driver)
