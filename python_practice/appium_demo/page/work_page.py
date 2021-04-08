#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-28 12:04
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : work_page.py
from appium.webdriver.common.mobileby import MobileBy

from appium_demo.page.base_page2 import BasePage2
from appium_demo.page.sign_page import SignPage


class WorkPage(BasePage2):
    # 初始化，接收到一个driver，并把它存起来
    # def __init__(self, driver):
    #     self.driver = driver

    # 进入打开页面
    def goto_sign_page(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().'
        #                          'scrollable(true).instance(0)).'
        #                          'scrollIntoView(new UiSelector().'
        #                          'text("打卡").instance(0));').click()

        self.swipe_click("打卡")

        return SignPage(self.driver)
