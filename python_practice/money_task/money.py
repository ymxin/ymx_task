#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-23 23:41
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : money.py

'''
课后作业
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
'''


class Money:

    def __init__(self, saved_money):
        self.saved_money = saved_money

    # def send_money(self):
    #     while True:
    #         if self.saved_money == 2000:
    #             print("终于攒够2000元了")
    #             break
    #         else:
    #             self.saved_money += self.salary
    #             print(f"目前攒了{self.saved_money}元钱了")

    # def select_money(self):
    #     print(self.money_test)

# if __name__ == '__main__':
#     money = Money(100)
#     money.send_money()
