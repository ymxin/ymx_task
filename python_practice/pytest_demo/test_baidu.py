#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-28 21:30
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_baidu.py

import allure
import pytest
from selenium import webdriver
import time


@allure.testcase("https://www.jianshu.com/p/bdd1d6fcc5df")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data', ['allure', 'pytest', 'selenium'])
def test_baidu_demo(test_data):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome(r"D:\ymx_software\Python38\Lib\site-packages\selenium\webdriver\chromedriver.exe")
        driver.get("http://www.baidu.com")
        driver.maximize_window()
    with allure.step(f"输入搜索词:{test_data}"):
        driver.find_element_by_id("kw").send_keys(test_data)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)
    with allure.step("保存图片"):
        driver.save_screenshot("img/baidu.png")
        allure.attach.file("img/baidu.png", attachment_type=allure.attachment_type.PNG)
        allure.attach("<head></head><body>首页</body>", "html code", allure.attachment_type.HTML)
        time.sleep(2)

    with allure.step("关闭浏览器"):
        driver.quit()
