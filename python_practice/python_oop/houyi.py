#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-21 17:08
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : houyi.py
from python_practice.python_oop.game_oop import Game


# 快速导报：alt+enter


class Houyi(Game):

    def __init__(self):
        self.defense = 100
        # 继承父类的构造方法
        super().__init__(1000, 1100)

    def fight(self):
        while True:
            # 我的剩余血量
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            # 敌人的剩余血量
            self.enemy_hp = self.enemy_hp - self.my_power

            print(f"我的血量：{self.my_hp} VS 敌人的血量：{self.enemy_hp}")
            # 胜负判断
            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                break


if __name__ == '__main__':
    houyi = Houyi()
    # 子对象可以直接调用父类的属性和方法
    print(houyi.my_hp)
    houyi.fight()
    houyi.rest(10)
