#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-17 21:24
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_param.py

# !/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-17 20:34
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_get_attribute.py
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestParam:

    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
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

    @pytest.mark.parametrize('searchkey, type, expect_price', [
        ('alibaba', 'BABA', 210.83),
        ('xiaomi', '01810', 22.25)
    ])
    def test_param(self, searchkey, type, expect_price):
        '''
        1、打开雪球应用
        2、点击搜索框
        3、输入搜索词：‘alibaba’ or 'xiaomi'...
        4、点击第一个搜索结果
        5、判断股票价格
        :return:
        '''

        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys(searchkey)
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/name').click()
        current_price = self.driver.find_element(MobileBy.XPATH,
                                                 f'//*[@text="{type}"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        # com.xueqiu.android:id/current_price
        print(f"当前价格：{current_price}")
        assert_that(current_price, close_to(expect_price, expect_price * 0.2))
        # assert_that(current_price, close_to(expect_price, 10.0))
