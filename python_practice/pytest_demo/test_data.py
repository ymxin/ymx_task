#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-23 22:56
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_data.py
import pytest
import yaml


class TestData:
    # @pytest.mark.parametrize(("a", "b"), [
    #     (2, 3),
    #     (10, 20),
    #     (30, 5)
    # ])
    # def test_data(self, a, b):
    #     print(a + b)
    #
    # @pytest.mark.parametrize(["a", "b"], [
    #     (2, 3),
    #     (10, 20),
    #     (30, 5)
    # ])
    # def test_data2(self, a, b):
    #     print(a - b)
    #
    # @pytest.mark.parametrize("a,b", [
    #     (2, 3),
    #     (10, 20),
    #     (30, 5)
    # ])
    # def test_data3(self, a, b):
    #     print(a * b)

    @pytest.mark.parametrize(('a', 'b'), yaml.safe_load(open("./data.yaml")))
    def test_data(self, a, b):
        print(a + b)
