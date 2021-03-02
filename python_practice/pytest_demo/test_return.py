#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-02 21:26
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_return.py
from time import sleep
import pytest


def test_return1():
    sleep(1)
    assert 1 == 2


def test_return2():
    sleep(1)
    assert 2 == 2


@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_return3():
    sleep(1)
    assert 3 == 2
