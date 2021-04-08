#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-07 17:03
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : first_demo.py


'''
代码执行不成功，之后尝试处理

'''

from appium import webdriver

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['version'] = '7.1.1'
desired_caps['deviceName'] = '127.0.0.1:7555'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = '.view.WelcomeActivityAlias'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.quit()
