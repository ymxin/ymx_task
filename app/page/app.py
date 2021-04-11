#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-04-08 20:45
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : app.py
from appium import webdriver

from app.page.information_page import InformationPage


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
        caps['noReset'] = 'true'
        caps['settings[waitForIdleTimeout]'] = 0

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

        self.driver.implicitly_wait(10)

    def goto_main(self):
        '''
        进入到主页面
        :return:
        '''
        return InformationPage(self.driver)
