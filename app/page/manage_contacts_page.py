#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-04-11 11:18
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : manage_contacts_page.py
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.edit_contact_page import EditContactPage


class ManageContactsPage(BasePage):

    def goto_edit_contact(self):
        '''
        进入到管理通讯录页面
        :return:
        '''
        # self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/igf"]').click()
        self.parse_action("../page/manage_contacts_page.yaml", "goto_edit_contact")
        return EditContactPage(self.driver)
