#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-17 20:34
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_get_attribute.py
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestGetAttribute:

    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            "dontStopAppOnReset": True,
            "skipDeviceInitialization": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_get_attribute(self):
        search_ele = self.driver.find_element(MobileBy.ID, 'tv_search')
        print(search_ele.get_attribute('content-desc'))
        print(search_ele.get_attribute('resource-id'))
        print(search_ele.get_attribute('class'))
        print(search_ele.get_attribute('enabled'))
        print(search_ele.get_attribute('clickable'))
        assert 'search' in search_ele.get_attribute('resource-id')
