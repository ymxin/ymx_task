#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-04 23:09
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_frame.py
from selenium.webdriver.common.by import By

from selenium_demo.base import Base


class TestFrame(Base):

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # ID：iframeResult
        # 切换到所在的frame
        # self.driver.switch_to_frame('iframeResult')
        self.driver.switch_to.frame('iframeResult')
        print(self.driver.find_element(By.ID, 'draggable').text)
        # 切换到父frame
        # self.driver.switch_to.parent_frame()
        # 切换到默认frame
        self.driver.switch_to.default_content()
        # submitBTN
        print(self.driver.find_element(By.ID, 'submitBTN').text)
