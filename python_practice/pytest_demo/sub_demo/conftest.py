#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-02 8:54
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : conftest.py
import pytest


@pytest.fixture()
def connectDB():
    print("sub_demo 下面的 connect DB")
