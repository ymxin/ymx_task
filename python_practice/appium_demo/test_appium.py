#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-07 18:46
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_appium.py
from time import sleep

from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "noReset": True
}
# 这个地址是本机地址，固定写法
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.click()
el2.send_keys("alibaba")
el3 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
el3.click()
sleep(3)
driver.quit()
