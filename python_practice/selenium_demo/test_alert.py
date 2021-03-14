#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-04 23:51
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_alert.py
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium_demo.base import Base


class TestAlert(Base):
    def test_alert(self):
        '''
        1、打开网页：https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        2、操作窗口右侧页面，将元素1拖拽到元素2
        3、这时出现一个alert弹窗，点击弹窗上的确定
        4、然后点击“点击运行”
        5、关闭网页
        :return:
        '''

        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        # 查找元素1
        drag = self.driver.find_element(By.ID, "draggable")
        # 查找元素2
        drop = self.driver.find_element(By.ID, "droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        sleep(3)
        # 切换到alert
        print("点击alert 确定按钮")
        self.driver.switch_to.alert.accept()
        # 切换到默认的frame
        self.driver.switch_to.default_content()
