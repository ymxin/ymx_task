#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-02 22:16
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_selenium.py

import selenium

from selenium import webdriver


def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
