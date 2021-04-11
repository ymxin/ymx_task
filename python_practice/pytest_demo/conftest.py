#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-02 8:38
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : conftest.py.py

import pytest


@pytest.fixture(scope="session")
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库操作")