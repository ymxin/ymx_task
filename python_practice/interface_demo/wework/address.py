#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-08-04 8:05
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : address.py

import requests

from interface_demo.wework.base import Base


class Address(Base):

    def get_member(self, userid):
        get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get"
        params = {
            "userid": userid
        }
        # r = requests.get(url=get_member_url, params=params)
        # self.s  是一个python类
        # r = self.s.get(url=get_member_url, params=params)
        r = self.send("get", url=get_member_url, params=params)
        return r.json()

    def update_member(self, userid, name, mobile):
        update_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        json_data = {
            'userid': userid,
            'mobile': mobile,
            'name': name
        }
        # r = self.s.post(url=update_member_url, json=json_data)
        r = self.send("post", url=update_member_url, json=json_data)
        return r.json()

    def create_member(self, userid, name, mobile, department):
        create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department,
        }
        # r = self.s.post(url=create_member_url, json=data)
        r = self.send("post", url=create_member_url, json=data)
        return r.json()

    def delete_member(self, userid):
        delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        params = {
            'userid': userid
        }
        # r = self.s.get(url=delete_member_url, params=params)
        r = self.send("get", url=delete_member_url, params=params)
        return r.json()
