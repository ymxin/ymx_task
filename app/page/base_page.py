#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-04-08 20:45
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : base_page.py
import logging
from typing import List, Dict

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from app.conftest import root_log


class BasePage:
    # logging.basicConfig(
    #     level=logging.INFO,
    #     # 日志格式
    #     # 时间、代码所在文件、代码行号、日志级别名字、日志信息
    #     format ='%(asctime).19s %(filename)s[line:%(lineno)d] %(levelname)s %(message).500s',
    #     # 打印日志的时间
    #     datefmt='%a %d %b %Y %H:%M:%S',
    #     # 日志文件存在的目录（目录必须存在）及日志文件名
    #     filename='report.log',
    #     # 打开日志文件的方式
    #     filemode='w'
    # )
    # 黑名单列表
    _blacklist = [(MobileBy.ID, 'com.tencent.wework:id/ig0'),
                  (MobileBy.XPATH, '//*[@text="关闭"]')]
    # 最大次数
    _max_num = 3
    # 初始值
    _error_num = 0

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, by, locator):
        try:
            root_log.info(f'find: by={by}, locator={locator}')
            element = self.driver.find_element(by, locator)
            self._error_num = 0
            return element
        except Exception as e:
            root_log.info("未找到元素")
            if self._error_num > self._max_num:
                self._error_num = 0
                raise e
            self._error_num += 1
            for ele in self._blacklist:
                eles = self.driver.find_elements(*ele)
                if len(eles) > 0:
                    # 关闭弹窗
                    eles[0].click()
                    # 继续执行find操作
                    return self.find(by, locator)
            raise e

    def find_click(self, by, locator):
        self.find(by, locator).click()

    def find_send(self, by, locator, key):
        self.find(by, locator).send_keys(key)

    def swipe_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def parse_action(self, path, fun_name):
        with open(path, "r", encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps: List[Dict] = function[fun_name]

        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["by"], step["locator"])
            elif step["action"] == "find":
                self.find(step["by"], step["locator"])
            elif step["action"] == "find_send":
                self.find_send(step["by"], step["locator"], step["key"])
            elif step["action"] == "swipe_click":
                self.swipe_click(step["text"])
