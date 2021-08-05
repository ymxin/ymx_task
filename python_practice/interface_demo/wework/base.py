#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-08-05 8:28
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : base.py

import requests


class Base:

    def __init__(self):
        # 声明一个session
        self.s = requests.Session()
        self.token = self.get_token()
        # token 放到session里
        self.s.params = {"access_token": self.token}

    def get_token(self):
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww8a97a9d7d2f57334&corpsecret=9_Rkq0A6b8wjLoJ_VZTRn4x6FWYANF2uORK-qH8fcX0")
        token = r.json()['access_token']
        return token

    def send(self, *args, **kwargs):
        return self.s.request(*args, **kwargs)
