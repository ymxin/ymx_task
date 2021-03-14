#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-04 22:22
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_window.py
'''
百度窗口切换案例
1、点击登录按钮
2、打开登录弹窗，点击立即注册
3、输入用户名，手机号，密码
4、回到上一个窗口
5、点击用户名登录
6、输入用户名，密码，点击注册按钮
'''

from time import sleep

from selenium.webdriver.common.by import By

from selenium_demo.base import Base


class TestWindow(Base):

    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        # //*[@id="u1"]/a
        # 点击登录
        self.driver.find_element(By.XPATH, '//*[@id="u1"]/a').click()
        print(self.driver.current_window_handle)
        # 点击立即注册
        self.driver.find_element(By.LINK_TEXT, '立即注册').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        # TANGRAM__PSP_4__userName

        # 跳转了一个新的页面
        # ----------------------------------
        # 获取所有窗口
        windows = self.driver.window_handles
        # 切换窗口
        self.driver.switch_to_window(windows[-1])
        # 输入用户名
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__userName').send_keys("username")
        # 输入手机号
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__phone').send_keys("18333604761")
        # 输入密码
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__password').send_keys("username")

        # 切换窗口
        self.driver.switch_to_window(windows[0])
        # 点击用户名登录
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__footerULoginBtn').click()

        # 输入用户名
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys("login_name")
        # 输入密码
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__password').send_keys("login_password")
        # 点击登录按钮
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__submit').click()

        sleep(3)
