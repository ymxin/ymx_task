#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-29 22:17
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : base_page.py
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    # driver被定义为实例变量；好处：子类也可以用
    _driver: WebDriver
    _black_list = [(By.ID, "com.xueqiu.android:id/iv_close")]

    # 定义一个初始化的构造方法，传一个driver进来
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # locator定位方式，value表达式
    def find(self, locator, value):
        try:
            element = self._driver.find_element(locator, value)
            return element
        except:
            # 怎么捕获弹窗：维护一个黑名单
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    # 为什么是0呢？一般默认只能找出一个
                    elements[0].click()
                    break
            # 再次调用find()，如果找到元素就执行；没有再次执行捕获弹窗操作
            return self.find(locator, value)

    # path:路径
    def steps(self, path):
        with open(path) as f:
            steps = yaml.safe_load(f)
        element = None
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"], step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()
