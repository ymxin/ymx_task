#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-02 20:30
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : check_demo.py

import pytest


def test_demo():
    print("test demo")


def check_demo():
    print("check demo")


class CheckDemo:
    def check_a(self):
        print("check a")
