#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-18 8:28
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : base_page.py
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    # 添加弹窗黑名单
    _black_lsit = [(By.ID, "image_cancel")]
    # 计数器
    _error_count = 0
    # 错误最大值
    _errot_max = 10

    _params = {}

    def __init__(self, driver: WebDriver = None):
        '''
        1、定义一个driver，外部传来一个值（添加一个driver参数）
        2、外部的driver的复用
        3、给driver指定一个WebDriver类型
        3、
        :param driver:
        '''
        self._driver = driver

    def find(self, by, locator=None):
        try:
            # 查找元素本身接受两个参数，一个是ID，一个是value，如果你传入元祖类型*，代表解元祖；后面if是判断你传的类型，元祖就解包，非元祖就接收两个参数
            element = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_element(by,
                                                                                                              locator)
            self._error_count = 0
            return element
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._errot_max:
                raise e
            # 弹窗处理
            for black in self._black_lsit:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by, locator)
            raise e

    def send(self, value, by, locator=None):
        try:
            self.find(by, locator).send_keys(value)
            self._error_count = 0
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._errot_max:
                raise e
            # 弹窗处理
            for black in self._black_lsit:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.send(value, by, locator)
            raise e

    # 读取yaml文件
    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            steps: list[dict] = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])

                if "action" in step.keys():
                    if "click" == step["action"]:
                        element.click()
                    if "send" == step["action"]:
                        # {value}
                        content: str = step["value"]
                        for param in self._params:
                            content = content.replace("{%s}" % param, self._params[param])
                        self.send(content, step["by"], step["locator"])
