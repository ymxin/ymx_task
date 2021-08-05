#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-08-04 8:09
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_address.py
import pytest

from interface_demo.wework.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()
        self.user_id = "aa_010"
        self.name = "姚二姚"
        self.mobile = "+86 13800000123"
        self.department = [4]

    @pytest.mark.parametrize("user_id,name,mobile,department", [
        ("aa_011", "姚1姚", "+86 13810000123", [4]),
        ("aa_012", "姚2姚", "+86 13820000123", [4]),
        ("aa_013", "姚3姚", "+86 13830000123", [4]),
        ("aa_014", "姚4姚", "+86 13840000123", [4]),
        ("aa_015", "姚5姚", "+86 13850000123", [4]),
        ("aa_016", "姚6姚", "+86 13860000123", [4]),
        ("aa_017", "姚7姚", "+86 13870000123", [4]),
        ("aa_018", "姚8姚", "+86 13880000123", [4]),
    ])
    def test_create_member(self, user_id, name, mobile, department):
        # 利用删除接口进行数据清理
        self.address.delete_member(user_id)
        r = self.address.create_member(user_id, name, mobile, department)
        # 删除无用数据、测试数据
        # self.address.delete_member(self.user_id)
        # assert r['errmsg'] == 'created'
        # 如果由于网络请求r的值拿不到，可以用get获取
        assert r.get('errmsg', 'network error') == 'created'

        r = self.address.get_member(user_id)
        self.address.delete_member(user_id)
        assert r.get("name") == name

    def test_get_member(self):
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        r = self.address.get_member(self.user_id)
        assert r.get('errmsg') == 'ok'
        assert r.get("name") == self.name

    def test_delete_member(self):
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        r = self.address.delete_member(self.user_id)
        assert r.get('errmsg') == 'deleted'
        r = self.address.get_member(self.user_id)
        assert r.get('errcode') == 60111

    def test_update_member(self):
        # 保证，成员一定是新添加的
        self.address.delete_member(self.user_id)
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        new_name = self.name + "222"
        r = self.address.update_member(self.user_id, new_name, self.mobile)
        assert r.get('errmsg') == 'updated'
        r = self.address.get_member(self.user_id)
        assert r.get('name') == new_name
