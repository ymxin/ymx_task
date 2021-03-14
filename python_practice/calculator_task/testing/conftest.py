#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-02 8:38
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : conftest.py.py

import pytest

from calculator_task.python_code.calculator import Calculator


@pytest.fixture(scope="module")
def get_print(self):
    print("计算开始")
    yield
    print("计算结束")
