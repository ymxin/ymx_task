#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-09 8:36
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_location.py
from time import sleep

from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *


class TestLocation:

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

    def test_search(self):
        '''
        1、打开雪球app
        2、点击搜索输入框
        3、在输入框输入：阿里巴巴
        4、在搜索结果里选择阿里巴巴,然后进行点击
        5、获取 阿里巴巴的股价，并判断这只股价的价格>200
        :return:
        '''
        print("这是搜索用例")

        self.driver.find_element_by_id("tv_search").click()
        # 这里使用中文需要在desired_caps设置两个参数:"unicodeKeyBoard":True,"resetKeyBoard": True
        self.driver.find_element_by_id("search_input_text").send_keys("阿里巴巴")
        # 点击阿里巴巴
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴'] ").click()

        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        expect_price = 200
        # assert current_price > 200
        assert_that(current_price, close_to(expect_price, expect_price * 0.2))

    def test_arr(self):
        '''
        打开雪球应用首页
        判断搜索框是否可用，并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和他的宽高
        向搜索框输入：alibaba
        判断[阿里巴巴]是否可见
        如果可见，打印“搜索成功”点击，如果不可见，打印“搜索失败”
        :return:
        '''
        element = self.driver.find_element_by_id("tv_search")
        search_enabled = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enabled == True:
            element.click()
            self.driver.find_element_by_id("search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴'] ")
            # alibaba_element.is_displayed()
            element_display = alibaba_element.get_attribute("displayed")
            if element_display == "true":
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchaction(self):
        action = TouchAction(self.driver)
        # action.press(x=361,y=613).move_to(x=361,y=1500).release().perform()
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        action.press(x=x1, y=y_start).move_to(x=x1, y=y_end).release().perform()

    # 模拟手势密码操作
    def test_touchaction2(self):
        print("解锁手势密码")

    # 获取股票的价格
    def test_get_current_price(self):
        self.driver.find_element_by_id("tv_search").click()
        # 这里使用中文需要在desired_caps设置两个参数:"unicodeKeyBoard":True,"resetKeyBoard": True
        self.driver.find_element_by_id("search_input_text").send_keys("阿里巴巴")
        # 点击阿里巴巴
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴'] ").click()
        locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        # current_price = self.driver.find_element(*locator).text
        ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        current_price = ele.text
        print(f"当前股票09988对应的股票价格{current_price}")
        assert float(current_price) > 200

    def test_uiautomator(self):
        '''
        1、点击我的，进入个人信息页面
        2、点击登录，进入到登录页面
        3、输入用户名和密码
        4、点击登录
        :return:
        '''
        # mine_text = 'resourceId("com.xueqiu.android:id/tab_icon").text("我的")'
        # self.driver.find_element_by_android_uiautomator(mine_text).click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("登录雪球")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("ymx")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("123456")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        return True

        # self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("账号密码")').click()

    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiScrollable\
        (new Uiselector().\
        scrollable(true).instance(0)).\
        scrollIntoView(new UiSelector().text("qwer").instance(0));')


if __name__ == '__main__':
    pytest.main()
