#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-28 12:05
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : sign_page.py
from appium.webdriver.common.mobileby import MobileBy

from appium_demo.page.base_page2 import BasePage2


class SignPage(BasePage2):

    # def __init__(self, driver):
    #     self.driver = driver

    def sign(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        # self.find_click("//*[@text='外出打卡']")
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        # self.find_click("//*[contains(@text,'次外出')]")
        # 获取
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡成功']")
        # self.find("//*[@text='外出打卡成功']")
        self.parse_action("../page/sign_page.yaml", "sign")

    # 有两个方法:上下班打卡
    def check_in_or_out(self):
        # self.find_click("//*[@text='上下班打卡']")
        self.parse_action("../page/sign_page.yaml", "check_in_or_out")
