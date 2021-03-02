#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-01 21:37
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : text_fixture.py
import pytest


@pytest.fixture()
def login():
    print("登陆操作")
    username = "tom"
    password = 123456
    token = "tokenasuw878sui"
    # yield 关键字可以激活 fixture 的 teardown 功能
    yield [username, password, token]
    print("注销操作")


# 测试用例1：需要提前登录
# 在测试用例中传入 fixture 方法名
def test_case1(login):
    # 获取fixture方法的返回值，直接调用fixture方法名
    print(f"用户信息为：{login}")
    print("测试用例1")


def test_case2(connectDB):
    print("测试用例2")


# 测试用例3：需要提前登录
# 装饰器调用，方法名当做字符串传入
@pytest.mark.usefixtures("login")
def test_case3():
    print("测试用例3")


def test_case4():
    print("测试用例4")
