#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-02 21:37
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_assume.py


import pytest


def test_assume():
    pytest.assume(1 == 1)
    pytest.assume(False == True)
    pytest.assume(100 == 200)
