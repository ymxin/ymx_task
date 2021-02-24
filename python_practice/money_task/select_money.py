#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-24 22:40
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : select_money.py

'''
课后作业
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
'''
from send_money import Send


class Select(Send):

    def __init__(self):
        super().__init__(1000)

    def select_money(self):
        print(f"你当前的工资为{self.salary}元哦，继续努力~")
