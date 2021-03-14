# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTestsuite1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_testbaiduclick(self):
        self.driver.get("https://www.baidu.com/")
        time.sleep(1)
        self.driver.set_window_size(1920, 1040)
        time.sleep(1)
        self.driver.find_element(By.ID, "kw").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "kw").send_keys("中国")
        time.sleep(1)
        self.driver.find_element(By.ID, "kw").send_keys(Keys.ENTER)
        time.sleep(1)
        self.vars["window_handles"] = self.driver.window_handles
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "中国吧 - 百度贴吧").click()
        self.vars["win2148"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win2148"])
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])
        self.driver.close()
