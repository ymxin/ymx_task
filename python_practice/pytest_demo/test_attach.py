#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-28 21:14
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_attach.py

import allure


def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)


def test_allure_html():
    allure.attach("<body>这是一个代码块</body>", "html代码块", attachment_type=allure.attachment_type.HTML)
