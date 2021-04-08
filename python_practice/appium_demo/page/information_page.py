#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time：2021-03-28 12:02
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : information_page.py
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver

from appium_demo.page.addressList_page import AddressListPage
from appium_demo.page.base_page2 import BasePage2
from appium_demo.page.work_page import WorkPage


class InformationPage(BasePage2):

    # 进入工作台
    def goto_work_page(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # self.find_click("//*[@text='工作台']")
        self.parse_action("../page/information_page.yaml", "goto_work_page")
        # 需要使用一个driver，复用;;;用return是因为链式调用
        return WorkPage(self.driver)

    def goto_addressList(self):
        # 进入到通讯录
        self.parse_action("../page/information_page.yaml", "goto_addressList")
        # 需要使用一个driver，复用;;;用return是因为链式调用
        return AddressListPage(self.driver)
