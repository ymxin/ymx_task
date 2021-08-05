#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-07-31 18:28
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_demo.py

import requests
from jsonpath import jsonpath
from hamcrest import *
from requests.auth import HTTPBasicAuth


class TestDemo:
    def test_demo(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            'a': '1',
            'b': '2'
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            'a': 1,
            'b': '2'
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={"H": "header demo"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['headers']['H'] == "header demo"

    def test_post_json(self):
        payload = {
            'a': 1,
            'b': '2'
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_json2(self):
        r = requests.get('https://ceshiren.com/categories.json')
        # print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '开源项目'
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == '开源项目'

    def test_hamcrest(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert_that(jsonpath(r.json(), '$..name')[0], equal_to('开源项目'))

    def test_cookies(self):
        url = 'https://httpbin.testing-studio.com/cookies'
        header = {
            "Cookie": "iReader=story",
            'User-Agent': 'iReader'
        }
        r = requests.get(url=url, headers=header)
        print(r.request.headers)

    def test_cookies2(self):
        url = 'https://httpbin.testing-studio.com/cookies'
        header = {
            'User-Agent': 'iReader'
        }
        cookie_data = {"iReader": "story2", 'user': 'ymx'}
        r = requests.get(url=url, headers=header, cookies=cookie_data)
        print(r.request.headers)

    # from requests.auth import HTTPBasicAuth
    def test_auth(self):
        r = requests.get(url="https://httpbin.testing-studio.com/basic-auth/ymx/123", auth=HTTPBasicAuth("ymx", "123"))
        print(r)
        print(r.text)
