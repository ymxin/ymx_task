#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-29 22:24
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : app.py
import yaml
from appium import webdriver

from appium_demo2.page.base_page import BasePage
from appium_demo2.page.main import Main


class App(BasePage):
    _package = 'com.xueqiu.android'
    _activity = '.view.WelcomeActivityAlias'

    def start(self):

        # 不用每次都初始化一个driver
        if self._driver is None:
            # 字典
            caps = dict()
            caps["platformName"] = 'android'
            caps['devicesName'] = '127.0.0.1:7555'
            caps['appPackage'] = self._package
            caps['appActivity'] = self._activity
            # 不清空缓存启动APP
            caps['noReset'] = True
            # 设置等待页面空闲状态的时间为0s
            caps['settings[waitForIdleTimeout]'] = 0
            caps['udid'] = yaml.safe_load(open("../page/configuration.yaml"))['caps']['udid']
            # 初始化driver
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        else:
            # 启动APP
            self._driver.start_activity(self._package, self._activity)

        # 显示等待10s
        self._driver.implicitly_wait(5)
        # 返回自身；原因：后面对另一个方法定义
        return self

    # 定义一个返回类型;后续调用app.start().main()
    def main(self) -> Main:
        return Main(self._driver)
