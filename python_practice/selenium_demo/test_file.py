#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-04 23:31
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_file.py
from time import sleep

from selenium.webdriver.common.by import By

from selenium_demo.base import Base


class TestFile(Base):
    def test_file(self):
        self.driver.get("https://image.baidu.com/")
        # //*[@id="sttb"]/img[1]
        self.driver.find_element(By.XPATH, '//*[@id="sttb"]/img[1]').click()
        self.driver.find_element(By.ID, 'stfile').send_keys(
            "D:\ymx_software\ymx_project\pythonProject\ymx_python_project\python_practice\selenium_demo\img\img.png")
        sleep(3)
