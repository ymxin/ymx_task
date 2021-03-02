#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-23 21:39
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_a.py
import pytest


def inc(x):
    return x + 1


@pytest.mark.parametrize('a,b', [
    (1, 2),
    (4, 5),
    (3, 3)
])
def test_answer(a, b):
    assert inc(a) == b


def test_answer2():
    assert inc(3) == 4


# 装饰器
@pytest.fixture()
def login():
    print("登录操作")
    username = "ymx"
    return username


class TestDemo:

    def test_a(self, login):
        print(f"你好，a, username={login}")

    def test_b(self):
        print("你好，b")


if __name__ == '__main__':
    pytest.main(['test_a.py'])
    # pytest.main(['test_a.py::TestDemo', '-v'])
