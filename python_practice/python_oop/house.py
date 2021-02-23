#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-20 22:31
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : house.py

'''
class 类名：
    多个类属性
    多个类方法

'''


class House:
    # 静态属性：类变量，在类中，方法之外定义
    door = "red"
    floor = "white"

    # 构造方法，在类实例化的时候自动执行，必须这么写，固定方法
    def __init__(self):
        # 加上self.变成实例变量
        print(self.door)
        # 定义实例变量->在类，方法之中，以self.变量名 方式定义
        # 实例变量的作用域是整个类中的所有方法
        self.kitchen = "cook"

    # 动态方法
    def sleep(self):
        # 普通变量->在类中，方法之中，并且前面没有self.开头
        bed = "席梦思"
        print(f"在房子里可以躺在{bed}睡觉")

    def cook(self):
        print("在房子里可以做饭")


if __name__ == '__main__':
    # 实例化->变量=类（）
    north_house = House()
    china_house = House()

    # 通过实例对象调用类属性
    # print(north_house.door)
    # 通过类也可以调用属性
    # print(House.door)

    # print(north_house.sleep())

    # 通过类直接修改属性
    # House.door = "green"
    # 通过实例对象调用类属性
    # print(north_house.door)
    # # 通过类也可以调用属性
    # print(House.door)

    # 通过实例修改属性
    # north_house.door = "white"
    # 通过实例对象调用类属性
    # print(north_house.door)
    # 通过类也可以调用属性
    # print(House.door)

    # print(china_house.door)
