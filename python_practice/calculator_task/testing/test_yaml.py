#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-14 12:55
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_yaml.py
import yaml


def test_yaml():
    with open("./datas/calc.yaml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        print(datas)
