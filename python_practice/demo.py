#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-20 21:03
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : demo.py


a = 1


def fun():
    a = 2
    print(f"变量a的值：{a}")
    print("这是一个方法")


print(a)
fun()
print(a)
