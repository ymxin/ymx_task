#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-06 21:35
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : register.py
from selenium.webdriver.common.by import By

from selenium_demo.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        # 输入企业名称
        self.find(By.ID, 'corp_name').send_keys('Lily')
        # 输入 管理员名称
        self.find(By.ID, 'manager_name').send_keys('Tom')

        return True
