#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-08 20:03
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : index_page.py
from selenium import webdriver

from selenium.webdriver.common.by import By

from web.page.login_page import LoginPage
from web.page.register_page import RegisterPage


# 首页的PO
class IndexPage:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(3)

    def goto_login(self):
        '''
        进入登录页面
        :return:
        '''
        # click login button
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # return login page
        return LoginPage(self.driver)

    def goto_register(self):
        '''
        进入注册页面
        :return:
        '''
        # click register button
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        # return register page
        return RegisterPage()
