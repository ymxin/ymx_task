#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-06 21:22
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : main.py
from selenium.webdriver.common.by import By

from selenium_demo.page.base_page import BasePage
from selenium_demo.page.login import Login
from selenium_demo.page.register import Register


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self.find(By.XPATH, '//*[@id="tmp"]/div[1]/a').click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.XPATH, '//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        return Login(self._driver)
