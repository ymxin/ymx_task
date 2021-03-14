#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-06 21:43
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : login.py

from selenium.webdriver.common.by import By

from selenium_demo.page.base_page import BasePage
from selenium_demo.page.register import Register


class Login(BasePage):
    def scan(self):
        pass

    def goto_register(self):
        self.find(By.XPATH, '//*[@id="wework_admin.loginpage_wx_$"]/main/div[2]/a').click()
        return Register(self._driver)
