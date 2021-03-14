#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-06 17:47
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_js.py
from time import sleep

from selenium.webdriver.common.by import By

from selenium_demo.base import Base


class TestJS(Base):

    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        # 输入：selenuim测试
        self.driver.find_element(By.ID, 'kw').send_keys("selenuim测试")
        # 点击搜索按钮
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        sleep(2)
        # 滑动到最底部
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(2)
        # 点击下一页
        self.driver.find_element(By.XPATH, '//*[@id="page"]/div/a[10]').click()

        sleep(5)
        # 输出性能数据
        for code in [
            'return document.title',
            'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("return document.getElementById('train_date').value='2021-4-1'")
        sleep(3)
