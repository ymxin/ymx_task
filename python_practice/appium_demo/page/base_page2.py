#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-28 17:36
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : base_page2.py
import json
from time import sleep
from typing import Dict, List

import allure
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage2:
    # 定义一个字典，将要替换的内容放到字典里
    _params = {}
    # 黑名单列表
    _blacklist = [(MobileBy.ID, 'com.tencent.wework:id/ig0'),
                  (MobileBy.XPATH, '//*[@text="关闭"]')]
    # 最大次数
    _max_num = 3
    # 初始值
    _error_num = 0

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_click(self, by, locator):
        # self.driver.find_element(MobileBy.XPATH, locator).click()
        self.find(by, locator).click()

    def setup_implicitly_wait(self, timeout):
        self.driver.implicitly_wait(timeout)

    def find(self, by, locator):
        try:
            # 没找到元素从这步就开始抛异常，找到了就执行清0操作
            element = self.driver.find_element(by, locator)
            self._error_num = 0
            # 找到了，重新设置成10s
            self.setup_implicitly_wait(10)
            return element
        except Exception as e:
            # 开始处理黑名单逻辑
            # 每次查找重新设置隐式等待时间
            self.setup_implicitly_wait(2)
            # 截图
            self.driver.get_screenshot_as_file("tmp.png")
            allure.attach.file("tmp.png", attachment_type=allure.attachment_type.PNG)
            # 设置最大查找次数
            if self._error_num > self._max_num:
                # 执行清空操作，再下一次出现弹窗时，可以继续执行处理弹窗的操作
                # 如果不清0，出现第四个弹窗就没法去自动处理了
                self._error_num = 0
                # 找到了，重新设置成10s
                self.setup_implicitly_wait(10)
                raise e
            # 每次进入except 都执行 +1操作
            self._error_num += 1
            # 弹窗处理
            # 先遍历黑名单列表
            for ele in self._blacklist:
                # 找到元素并返回列表[element1,element2...]
                # 没有找到会返回空列表
                eles = self.driver.find_elements(*ele)
                if len(eles) > 0:
                    # 关闭弹窗
                    eles[0].click()
                    # 继续执行find操作
                    return self.find(by, locator)
            # 如果弹窗黑名单都处理完，仍然没有找到想要的元素，则抛出异常
            raise e

    def swipe_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    # def parse_action(self, steps: List[Dict])
    # def parse_action(self, path):
    #     with open(path,"r", encoding="utf-8") as f:
    #         steps: List[Dict]= yaml.safe_load(f)
    #     #  解析列表：列出列表中的内容
    #     for step in steps:
    #        # 取出列表中的每个字典；items：取出字典中的每一个元素
    #        # for key, value in step.items():
    #         if step["action"] == "find_click":
    #             self.find_click(step["locator"])
    #         elif step["action"] == "find":
    #             self.find(step["locator"])
    def parse_action(self, path, fun_name):
        with open(path, "r", encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps: List[Dict] = function[fun_name]
        # json序列表与反序列化
        # json.dumps() 序列化   会将一个Python的对象转化为字符串
        # json.loads() 反序列表  将字符串转化为Python对象
        raw = json.dumps(steps)
        # 1、进行替换
        for key, value in self._params.items():
            # 将params里的key和value进行替换
            raw = raw.replace("${" + key + "}", value)
        # 再转成Python对象
        steps = json.loads(raw)
        for step in steps:
            # "find_click"关键字要和yaml文件里的值对应上，不然会报错
            if step["action"] == "find_click":
                self.find_click(step["by"], step["locator"])
            elif step["action"] == "find":
                self.find(step["by"], step["locator"])
            elif step["action"] == "swipe_click":
                self.swipe_click(step["text"])
            elif step["action"] == "find_sendkeys":
                self.find(step["by"], step["locator"]).send_keys(step["text"])
