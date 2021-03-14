#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-13 22:44
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : calculator.py

# 计算器
class Calculator:

    # 加法 add
    def add(self, x, y):
        return x + y

    # 减法 subtract
    def subtract(self, x, y):
        return x - y

    # 乘法 multiply
    def multiply(self, x, y):
        return x * y

    # 除法 divide
    def divide(self, x, y):
        return x / y


if __name__ == '__main__':
    calculator = Calculator()
    print(calculator.add(4, 5))
    print(calculator.divide(5, 1))
    print(calculator.subtract(4, 5))
    print(calculator.multiply(20, 4))
