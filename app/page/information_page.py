#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-04-11 11:02
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : information_page.py
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.manage_contacts_page import ManageContactsPage


class InformationPage(BasePage):

    def goto_manage_contacts(self):
        '''
        进入到通讯录页面
        :return:
        '''
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]' ).click()
        self.parse_action("../page/information_page.yaml", "goto_manage_contacts")
        return ManageContactsPage(self.driver)
