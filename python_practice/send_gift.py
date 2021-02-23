#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-20 21:27
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : send_gift.py

"""
送礼物
1、定义礼物标识
2、定义送礼物方法
3、定义收礼物方法
4、启动方法
"""

have_gift = False


def send_gift():
    print("送礼物啦")
    global have_gift
    have_gift = True


def show():
    if have_gift == True:
        print("收到礼物很开心")
    else:
        print("没有礼物了")


print(f"{__name__}")
if __name__ == '__main__':
    send_gift()
    show()
