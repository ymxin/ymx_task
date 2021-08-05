#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-29 22:32
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : main.py
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from appium_demo2.page.base_page import BasePage


class Main(BasePage):

    def goto_search(self):
        # self.find(MobileBy.ID, "tv_search").click()
        self.steps("../page/main.yaml")

    def goto_windows(self):
        self.find(By.ID, "post_status").click()
        self.find(By.ID, "tv_search").click()
