#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

# os.mkdir("testdir")
# print(os.listdir("./"))

# os.removedirs("testdir")

# print(os.getcwd())


# 判断b文件夹是否存在
# print(os.path.exists("b"))

if not os.path.exists("b"):
    os.mkdir("b")
if not os.path.exists("b/test.txt"):
    f = open("b/test.txt", "w")
    f.write("hello,os")
    f.close()
