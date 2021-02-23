#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-20 23:12
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : game_oop.py

'''
回合制格斗游戏

'''
from python_practice.python_oop.log_decorator import log_decorator


class Game:
    # def __init__(self):
    #     # 初始化属性
    #     self.my_hp = 1000
    #     self.my_power = 200
    #     self.enemy_hp = 1000
    #     self.enemy_power = 199

    def __init__(self, my_hp, enemy_hp):
        # 初始化属性
        self.my_hp = my_hp
        self.my_power = 200
        self.enemy_hp = enemy_hp
        self.enemy_power = 199

    # 对打方法
    @log_decorator
    def fight(self):
        while True:
            # 我的剩余血量
            self.my_hp = self.my_hp - self.enemy_power
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

    # 定义休息方法
    def rest(self, timenum):
        print(f"太累了休息{timenum}分钟")


if __name__ == '__main__':
    game = Game(1000, 900)
    game.fight()
