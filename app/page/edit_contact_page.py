#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-04-11 11:34
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : edit_contact_page.py
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.delete_contact_page import DeleteContactPage


class EditContactPage(BasePage):
    def goto_delete_contact(self):
        '''
        进入删除联系人页面
        :return:
        '''
        # //*[ @ resource - id = "com.tencent.wework:id/enj"][last() - 1] 倒数第二个元素
        # self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/enj"][last()-1]').click()
        self.parse_action("../page/edit_contact_page.yaml", "goto_delete_contact")
        return DeleteContactPage(self.driver)
