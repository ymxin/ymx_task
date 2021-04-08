#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-29 8:49
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_common_api.py
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestCommonApi:

    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "UQG5T20730001040",
            "appPackage": "com.chaozh.iReaderFree",
            "appActivity": "com.chaozh.iReader.ui.activity.WelcomeActivity",
            "noReset": True,
            "dontStopAppOnReset": False,
            "skipDeviceInitialization": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_mobile(self):
        self.driver.make_gsm_call('18333604761', GsmCallActions.CALL)

        self.driver.send_sms('18333604761', 'hello appium api')
