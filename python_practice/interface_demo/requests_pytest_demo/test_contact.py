#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-08-03 7:58
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_contact.py

import requests


def get_token():
    r = requests.get(
        "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww8a97a9d7d2f57334&corpsecret=9_Rkq0A6b8wjLoJ_VZTRn4x6FWYANF2uORK-qH8fcX0")
    token = r.json()['access_token']
    return token


def test_get_member():
    get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=YaoMiaoXin"
    r = requests.get(url=get_member_url)
    print(r.json())
    assert r.json()['name'] == '姚苗欣'


def test_update_member():
    update_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}"
    json_data = {
        'userid': 'YaoMiaoXin',
        'mobile': '18333604761',
        'name': '姚小姚'
    }
    r = requests.post(url=update_member_url, json=json_data)
    print(r.json())


def test_create_member():
    create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    data = {
        "userid": "aa_010",
        "name": "姚二姚",
        "alias": "second_yao",
        "mobile": "+86 13800000123",
        "department": [4],
    }
    r = requests.post(url=create_member_url, json=data)
    print(r.json())


def test_delete_member():
    delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=aa_010"
    r = requests.get(url=delete_member_url)
    print(r.json())
