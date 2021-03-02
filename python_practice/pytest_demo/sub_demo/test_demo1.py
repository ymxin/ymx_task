#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-02 8:52
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_demo1.py

import pytest


@pytest.fixture()
def connectDB():
    print("test_demo1 下面的 connect DB")


def test_a(connectDB):
    print("sub_demo test_a")


class TestA:
    def test_b(self):
        print("sub_demo test_b")
