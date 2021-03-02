#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-01 22:19
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_scope.py


class TestDemo:

    def test_a(self, connectDB):
        print("测试用例A")

    def test_b(self, connectDB):
        print("测试用例B")


class TestDemo2:

    def test_c(self, connectDB):
        print("测试用例C")

    def test_d(self, connectDB):
        print("测试用例D")
