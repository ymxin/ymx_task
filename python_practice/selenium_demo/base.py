#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-04 22:25
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : base.py

'''
mac运行： browser=chrome pytest 文件名
'''

import os

from selenium import webdriver


class Base:
    def setup(self):
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()
