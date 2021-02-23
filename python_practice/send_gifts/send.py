#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-20 21:37
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : show.py

# from gift import have_gift
import gift


def show():
    have_gift = gift.have_gift
    if have_gift == True:
        print("收到礼物很开心")
    else:
        print("没有礼物了")
