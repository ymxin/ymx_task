#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-10 8:39
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : main_page.py

'''
作业
完成添加联系人PO封装
1、添加联系人操作
2、保存成功后，判断联系人是否存在，注意在第二页的情况(分页没写，后面补齐)
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

from web.page.add_member_page import AddMemberPage

# 企业微信主页面
from web.page.base_page import BasePage


class MainPage(BasePage):
    # 首页的时候要打开base_url,所以在这里设置它(会先初始化它的类变量)
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        '''
        添加成员
        :return:
        '''

        # 点击添加成员
        self.find(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        # 进入添加成员的页面
        return AddMemberPage(self.driver)
