#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-13 21:46
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_action.py
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestAction:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "cn.kmob.screenfingermovelock",
            "appActivity": "com.samsung.ui.MainActivity",
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

    def test_action(self):
        print("模拟手势密码")

        action = TouchAction(self.driver)
        action.press(x=119, y=175).move_to(x=365, y=175).move_to(x=598, y=175).move_to(x=596, y=414). \
            move_to(x=599, y=568).release().perform()
