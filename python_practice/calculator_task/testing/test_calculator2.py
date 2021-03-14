#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-14 10:31
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_calculator.py

'''
计算器练习-仅加法
'''
import pytest
import yaml

from calculator_task.python_code.calculator import Calculator

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(datas)
    myid = datas['myid']
    print(myid)


class TestCalculator:
    def setup_class(self):
        print("开始计算")
        self.cal = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a,b,expect",
        add_datas, ids=myid
    )
    def test_add(self, a, b, expect):
        # 实例化计算器
        # cal = Calculator()
        # 调用add方法
        result = self.cal.add(a, b)
        # 判断result 是否是 浮点数，是，保留两位小数
        if isinstance(result, float):
            # 得出结果，写断言
            assert round(result, 2) == expect
        else:
            # 得到结果，断言处理
            assert result == expect

    # @pytest.mark.parametrize(
    #     "a,b,expect",
    #     [
    #         (2, 4, 6),
    #         (4.0, 5.0, 9.0),
    #         (-1, -2, -3),
    #         (0.1, 0.2, 0.3)
    #     ], ids=['int', 'float', 'negative', 'round']
    # )
    # def test_add(self, a, b, expect):
    #     # 实例化计算器
    #     # cal = Calculator()
    #     # 调用add方法
    #     result = self.cal.add(a, b)
    #     # 判断result 是否是 浮点数，是，保留两位小数
    #     if isinstance(result, float):
    #         # 得出结果，写断言
    #         assert round(result, 2) == expect
    #     else:
    #         # 得到结果，断言处理
    #         assert result == expect

    # def test_add2(self):
    #     result = self.cal.add(0.1, 0.2)
    #     assert round(result, 2) == 0.3

    # def test_add3(self):
    #     # cal = Calculator()
    #     assert self.cal.add(-2, -3) == -5

    def test_subtract(self):
        pass

    def test_multiply(self):
        pass

    def test_divide(self):
        pass
