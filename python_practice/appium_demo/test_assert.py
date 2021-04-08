#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-17 20:50
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_assert.py

from hamcrest import *


class TestAssert:

    def test_assert(self):
        a = 10
        b = 20

        assert a < b

    def test_assert2(self):
        a = 10
        b = 20

        assert a > b

    def test_assert3(self):
        assert 'h' in 'this'

    def test_hamrest(self):
        # assert_that(10, equal_to(9), '这是一个提示')
        # 上下浮动10
        # assert_that(13, close_to(10,2),'这是一个close_to提示')
        # 包含字符串
        assert_that('contains some strings', contains_string('string'))
