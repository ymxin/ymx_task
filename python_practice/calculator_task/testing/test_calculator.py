#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-14 10:31
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_calculator.py
'''
课后作业：
补全计算器中加法和除法的测试用例
使用参数化完成测试用例的自动生成
在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：

使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()
'''
import pytest
import yaml

from calculator_task.python_code.calculator import Calculator

with open("./datas/calc.yaml", encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_myid = datas['add']['myid']
    sub_datas = datas['subtract']['datas']
    sub_myid = datas['subtract']['myid']
    mul_datas = datas['multiply']['datas']
    mul_myid = datas['multiply']['myid']
    div_datas = datas['divide']['datas']
    div_myid = datas['divide']['myid']


class TestCalculator:
    def setup_class(self):
        print("开始计算")
        self.cal = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a,b,expect",
        add_datas, ids=add_myid
    )
    def test_add(self, a, b, expect):
        # 调用add方法
        result = self.cal.add(a, b)
        # 判断result 是否是 浮点数，是，保留两位小数
        if isinstance(result, float):
            # 得出结果，写断言
            assert round(result, 2) == expect
        else:
            # 得到结果，断言处理
            assert result == expect

    @pytest.mark.parametrize(
        "a,b,expect",
        sub_datas, ids=sub_myid
    )
    def test_subtract(self, a, b, expect):
        # 调用subtract方法
        result = self.cal.subtract(a, b)
        # 判断result 是否是 浮点数，是，保留两位小数
        if isinstance(result, float):
            # 得出结果，写断言
            assert round(result, 2) == expect
        else:
            # 得到结果，断言处理
            assert result == expect

    @pytest.mark.parametrize(
        "a,b,expect",
        mul_datas, ids=mul_myid
    )
    def test_multiply(self, a, b, expect):
        # 调用multiply方法
        result = self.cal.multiply(a, b)
        # 判断result 是否是 浮点数，是，保留两位小数
        if isinstance(result, float):
            # 得出结果，写断言
            assert round(result, 2) == expect
        else:
            # 得到结果，断言处理
            assert result == expect

    @pytest.mark.parametrize(
        "a,b,expect",
        div_datas, ids=div_myid
    )
    def test_divide(self, a, b, expect):
        # 调用divide方法
        result = self.cal.divide(a, b)
        # 判断result 是否是 浮点数，是，保留两位小数
        if isinstance(result, float):
            # 得出结果，写断言
            assert round(result, 2) == expect
        else:
            # 得到结果，断言处理
            assert result == expect
