#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-03 21:49
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_wait.py
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.LINK_TEXT, '最新').click()
        # sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '#ember23 .name').click()
        self.driver.find_element(By.XPATH, '//li[@id="ember198"]/span').click()
        # 自定义函数一定传一个参数，参数可以不用，但是一定要传
        # def wait(x):
        #     return len(self.driver.find_elements(By.LINK_TEXT, 'selenium')) >= 1
        # 显示等待
        # WebDriverWait(self.driver, 10).until(wait)
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//li[@id="ember198"]/span' )))
        self.driver.find_element(By.LINK_TEXT, '热门').click()
