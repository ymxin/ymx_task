#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-24 23:27
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_date_driven.py
import pytest
import yaml


class TestDataDriven:

    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yaml")))
    def test_data(self, env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境的IP是", env["test"])
        elif "dev" in env:
            print("这是开发环境")
