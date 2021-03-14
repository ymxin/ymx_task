#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-03 21:04
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_hogwards.py
import time

# 导入依赖模块
from selenium import webdriver

'''
1、打开测试人网站主页
2、点击社团
3、点击求职面试圈
4、点击第一条内容
'''


class TestHogwards:
    # 初始化环境
    def setup(self):
        # 初始化driver
        self.driver = webdriver.Chrome()
        # 窗口最大化
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(5)

    # 资源回收
    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        # 打开测试人首页
        self.driver.get("https://testerhome.com/")
        # 直接等待
        # time.sleep(1)
        # 点击社团
        self.driver.find_element_by_link_text("社团").click()
        # 点击求职面试圈
        self.driver.find_element_by_link_text("求职面试圈").click()
        # 点击第一条内容
        self.driver.find_element_by_css_selector(".topic-27641 .title > a").click()
