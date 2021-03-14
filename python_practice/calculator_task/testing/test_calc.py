#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-14 15:47
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_calc.py

'''
课后作业
1、补全计算器（加减乘除）的测试用例，编写用例顺序：【加-减-乘-除】
2、创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
3、将 fixture 方法存放在 conftest.py ，设置 scope=module(这个步骤没有实现)
4、控制测试用例顺序按照[加-除-减-乘]这个顺序执行
5、结合 allure 生成本地测试报告

'''
import allure
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


@allure.testcase("https://www.jianshu.com/p/bdd1d6fcc5df")
@allure.feature("计算器操作")
class TestCalculator:

    # def setup_class(self):
    #     print("开始计算")
    #     self.cal = Calculator()
    # def teardown_class(self):
    #     print("计算结束")

    @pytest.fixture()
    def get_calc(self):
        print("计算开始")
        self.cal = Calculator()
        # yield 关键字可以激活 fixture 的 teardown 功能
        yield
        print("计算结束")

    @allure.story("两个数的加法运算")
    @pytest.mark.parametrize(
        "a,b,expect",
        add_datas, ids=add_myid
    )
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, a, b, expect):
        with allure.step("计算两个数的和"):
            # 调用add方法
            result = self.cal.add(a, b)
            # 判断result 是否是 浮点数，是，保留两位小数
            if isinstance(result, float):
                # 得出结果，写断言
                assert round(result, 2) == expect
            else:
                # 得到结果，断言处理
                assert result == expect

    @allure.story("两个数的减法运算")
    @pytest.mark.parametrize(
        "a,b,expect",
        sub_datas, ids=sub_myid
    )
    @pytest.mark.run(order=3)
    def test_subtract(self, get_calc, a, b, expect):
        # 调用subtract方法
        result = self.cal.subtract(a, b)
        # 判断result 是否是 浮点数，是，保留两位小数
        if isinstance(result, float):
            # 得出结果，写断言
            assert round(result, 2) == expect
        else:
            # 得到结果，断言处理
            assert result == expect

    @allure.story("两个数的乘法运算")
    @pytest.mark.parametrize(
        "a,b,expect",
        mul_datas, ids=mul_myid
    )
    @pytest.mark.run(order=4)
    def test_multiply(self, get_calc, a, b, expect):
        # 调用multiply方法
        result = self.cal.multiply(a, b)
        # 判断result 是否是 浮点数，是，保留两位小数
        if isinstance(result, float):
            # 得出结果，写断言
            assert round(result, 2) == expect
        else:
            # 得到结果，断言处理
            assert result == expect

    @allure.story("两个数的除法运算")
    @pytest.mark.parametrize(
        "a,b,expect",
        div_datas, ids=div_myid
    )
    @pytest.mark.run(order=2)
    def test_divide(self, get_calc, a, b, expect):
        # 调用divide方法
        result = self.cal.divide(a, b)
        # 判断result 是否是 浮点数，是，保留两位小数
        if isinstance(result, float):
            # 得出结果，写断言
            assert round(result, 2) == expect
        else:
            # 得到结果，断言处理
            assert result == expect
