#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-04-01 8:39
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_replace.py

def test_replace():
    a = {'name': '张三', 'phone_num': '18356574634'}
    b = "hello hello ${name} goto play ahaha ${phone_num}"

    for key, value in a.items():
        # print(key)
        # print(value)
        x = "${" + key + "}"
        print(x)
        b = b.replace(x, value)
    print(b)
