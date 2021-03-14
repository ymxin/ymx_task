#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-08 20:04
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : register_page.py


from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


# 注册PO
class RegisterPage(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        '''
        注册
        :return:
        '''

        # 输入公司名
        self.driver.find_element(By.ID, "corp_name").send_keys("alibaba")
        # 输入管理人员姓名
        self.driver.find_element(By.ID, "manager_name").send_keys("zhangsan")
        # 输入管理员手机号
        self.driver.find_element(By.ID, "register_tel").send_keys("18300000000")

        return True
