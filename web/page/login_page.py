#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-08 20:03
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : login_page.py


from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.page.register_page import RegisterPage


# 登录页面的PO
class LoginPage(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scan(self):
        '''
        扫码
        :return:
        '''

    def goto_register(self):
        # 点击企业注册
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        # 进入注册页面
        return RegisterPage(self.driver)
