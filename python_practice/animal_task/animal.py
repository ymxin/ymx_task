#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-21 21:05
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : animal.py

'''
自己写一个面向对象的例子：

比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
作业上传到自己的 github 仓库中，把 github 仓库地址回复到课程贴中
'''


# 创建动物类
class Animal:
    # 构造函数
    def __init__(self, name, color, age, sex):
        # 初始化属性
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def call(self):
        print("动物会叫")

    def run(self):
        print("动物会跑")


if __name__ == '__main__':
    animal = Animal("Lily", "red", 27, "女")
    print(animal.name, animal.age)
    animal.call()
