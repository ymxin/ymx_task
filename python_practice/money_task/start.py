#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-23 23:47
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : start.py

'''
课后作业
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
'''
from select_money import Select
from send_money import Send

if __name__ == "__main__":
    send = Send(1000)
    send.send_money()
    print("--------------------------------")
    select = Select()
    select.select_money()
