#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-22 21:26
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : cat.py
'''
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
作业上传到自己的 github 仓库中，把 github 仓库地址回复到课程贴中
'''
from python_practice.animal_task.animal import Animal


class Cat(Animal):
    # 重写父类的__init__方法
    def __init__(self):
        # 添加新属性
        self.hair = "短毛"
        # 继承父类属性
        super().__init__("Tom", "blue", 20, "男")

    def catching_mice(self):
        print("猫会捉老鼠~")

    # 重写方法
    def call(self):
        print("猫会喵喵叫")


if __name__ == '__main__':
    cat = Cat()

    print(f"猫的性别是{cat.sex}，毛发是{cat.hair}", )
    cat.call()
