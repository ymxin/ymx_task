#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-18 9:05
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : app.py
from appium import webdriver

from appium_demo.page.base_page import BasePage
from appium_demo.page.main import Main


class App(BasePage):

    def start(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["devicesName"] = "127.0.0.1:7555"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["autoGrantPermissions"] = True
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self._driver.implicitly_wait(3)
        else:
            # 复用
            self._driver.start_activity(_package, _activity)
        return self

    def main(self):
        return Main(self._driver)
