#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-02 20:04
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_params.py


import pytest


@pytest.fixture(params=[1, 2, 3])
def login1(request):
    data = request.param
    print("获取测试数据")
    return data


def test_case1(login1):
    # 调用login1的参数
    print(login1)
    print("测试用例1")
