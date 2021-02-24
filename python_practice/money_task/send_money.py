#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-24 22:31
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : send_money.py

'''
课后作业
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
'''
from money import Money


# 定义发工资的类
class Send(Money):

    # 初始化参数
    def __init__(self, salary):
        self.salary = salary
        super().__init__(1000)

    def send_money(self):
        while True:
            if self.saved_money == 20000:
                print("终于攒够20000元了")
                break
            else:
                self.saved_money += self.salary
                print(f"目前攒了{self.saved_money}元钱了")
