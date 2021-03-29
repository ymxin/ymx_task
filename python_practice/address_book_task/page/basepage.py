#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-28 20:39
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : basepage.py
from typing import List, Dict

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_click(self, locator):
        self.find(locator).click()

    def find(self, locator):
        return self.driver.find_element(MobileBy.XPATH, locator)

    def find_send(self, locator, send_key):
        self.driver.find_element(MobileBy.XPATH, locator).send_keys(send_key)

    def parse_action(self, path, fun_name):
        with open(path, "r", encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps: List[Dict] = function[fun_name]
        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["locator"])
            elif step["action"] == "find":
                self.find(step["locator"])
            elif step["action"] == "find_send":
                self.find_send(step["locator"], step["send_key"])
