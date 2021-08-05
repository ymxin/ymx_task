#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-29 22:37
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_main.py
import pytest
import yaml

from appium_demo2.page.app import App
from appium_demo2.testcase.test_base import TestBase


class TestMain(TestBase):

    @pytest.mark.parametrize("value1,value2", yaml.safe_load(open("../page/test_main.yaml")))
    def test_main(self, value1, value2):
        self.app.start().main().goto_search()

        print(value1)
        print(value2)

    def test_windows(self):
        self.app.start().main().goto_windows()
