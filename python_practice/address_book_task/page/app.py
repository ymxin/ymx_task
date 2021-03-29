#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-28 20:39
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : app.py
from appium import webdriver

from address_book_task.page.information_page import InformationPage


class App:

    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        caps = {}
        caps["platformName"] = 'android'
        caps['devicesName'] = '127.0.0.1:7555'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.WwMainActivity'
        # 不清空缓存启动APP
        caps['noReset'] = 'true'
        # 设置等待页面空闲状态的时间为0s
        caps['settings[waitForIdleTimeout]'] = 0

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        # 显示等待10s
        self.driver.implicitly_wait(10)

    def goto_main(self):
        return InformationPage(self.driver)
