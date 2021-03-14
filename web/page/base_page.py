#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-10 22:29
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : base_page.py

# 基类：专门存放init，find方法
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ""

    def __init__(self, driver: WebDriver = None):

        if driver == None:
            # 复用浏览器 option.debugger_address
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)
            # 创建完driver，立刻设置隐式等待
            self.driver.implicitly_wait(3)
        else:
            self.driver = driver
        # 仅第一次打开这个页面，后面使用已打开的URL
        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self, locator, value):
        return self.driver.find_element(locator, value)

    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    def with_for_click(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
