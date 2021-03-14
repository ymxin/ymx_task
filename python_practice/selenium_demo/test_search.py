#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-04 20:31
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_search.py

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSearch:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def test_search(self):
        self.driver.find_element(By.ID, 'kw').send_keys("selenium")
        self.driver.find_element(By.ID, 'su').click()
        # //*[@id="3001"]/div[1]/h3/a
        self.driver.find_element(By.XPATH, '//*[@id="3001"]/div[1]/h3/a')

    def teardown(self):
        self.driver.quit()
