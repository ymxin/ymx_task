#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-02 21:44
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_ordering.py
from time import sleep

import pytest


@pytest.mark.run(order=2)
def test_1():
    sleep(1)
    assert True


@pytest.mark.third
def test_2():
    sleep(1)
    assert True


@pytest.mark.run(order=1)
def test_3():
    sleep(1)
    assert True
