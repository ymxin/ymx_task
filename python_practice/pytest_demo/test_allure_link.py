#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-28 21:00
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_allure_link.py

import allure


@allure.link("http://www.baidu.com", name="链接")
def test_allure_link():
    print("这是一条加了链接的测试")
