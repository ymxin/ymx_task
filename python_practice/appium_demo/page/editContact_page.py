#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-31 21:30
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : editContact_page.py
from appium_demo.page.base_page2 import BasePage2


class EditContactPage(BasePage2):
    # 接收test_contact传过来的参数，怎么将参数传递到editContact_page.yaml中？？
    # 定义一个规则：yaml和解析文件通用的规则
    def exit_contact(self, name, phone_num):
        '''
        编辑成员
        :return:
        '''
        # 想要替换，先给params赋值
        self._params['name'] = name
        self._params['phone_num'] = phone_num

        self.parse_action("../page/editContact_page.yaml", "exit_contact")

    def verify_ok(self):
        '''
        判断是否有添加成功的toast
        :return:
        '''
        self.parse_action("../page/editContact_page.yaml", "verify_ok")
