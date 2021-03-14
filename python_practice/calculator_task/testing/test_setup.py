#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-14 11:17
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_setup.py

def setup_module():
    print("模块级别的 setup")


def teardown_module():
    print("模块级别的 teardown")


def setup_function():
    print("函数级别的 setup")


def teardown_function():
    print("函数级别的 teardown")


def test_fun():
    print("测试函数1")


class TestSetup:

    def setup_class(self):
        print("类级别的 setup")

    def teardown_class(self):
        print("类级别的 teardown")

    def setup(self):
        print("方法级别的 setup")

    def teardown(self):
        print("方法级别的 teardown")

    def test_demo1(self):
        print("测试用例1：test_demo1")

    def test_demo2(self):
        print("测试用例2：test_demo2")


class TestSetup2:

    def setup_class(self):
        print("类级别的 setup")

    def teardown_class(self):
        print("类级别的 teardown")

    def setup(self):
        print("方法级别的 setup")

    def teardown(self):
        print("方法级别的 teardown")

    def test_demo1(self):
        print("测试用例1：test_demo1")

    def test_demo2(self):
        print("测试用例2：test_demo2")
