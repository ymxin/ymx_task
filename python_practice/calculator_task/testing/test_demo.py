#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-14 10:48
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_demo.py
import pytest


def test_a():
    print("test_demo test_a")


def test_b():
    print("test_demo test_b")


def test_c():
    assert 1 == 2


@pytest.mark.parametrize('a', [1, 2, 3])
@pytest.mark.parametrize('b', [4, 5, 6])
def test_param(a, b):
    print(f"a={a},b={b}")
