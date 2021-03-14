#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-03-04 21:38
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : test_form.py
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestForm:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.find_element(By.ID, 'user_login').send_keys("ymx")
        self.driver.find_element(By.ID, 'user_password').send_keys('123456')
        # 这里执行有个问题
        # self.driver.find_element(By.ID, 'user_remember_me').click()
        self.driver.find_element(By.XPATH, '//*[@id="new_user"]/div[4]/input').click()
        sleep(5)
