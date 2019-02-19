# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/19 11:38
# 文件: test_addgroup.py
import sys
sys.path.append('..')
from selenium import webdriver
from pages.login_page import Login
from pages.cusmanage_page import cusManage
import unittest
import time
from common.assertFunction import AssertFunction
from common.browsers import Browsers
from data.userinfo import *

class TestAddGroupNum(unittest.TestCase):
    driver=None
    group=None
    check=None
    user=None

    def setUp(self):
        global driver,check,user

        browser = Browsers(browserType)
        driver = webdriver.Chrome(browser.select_browser())
        user = Login(driver)
        user.login(address,account,password)
        check = AssertFunction()
        self.assertTrue(check.isElementExist(driver,e_personalDetails))
        self.assertIn('homepage', driver.current_url)

    def test_addGroupNum(self):
        u"""添加客户组号码"""
        global group
        group=cusManage(driver)
        group.cus_manage()
        time.sleep(2)
        group.add_group(groupName,number)
        time.sleep(2)
        self.assertTrue(check.isElementExist(driver,e_deleteGroup,groupName))

    def tearDown(self):
        #删除客户组
        group.delete_group(groupName)
        driver.find_element_by_xpath(e_closeCusGroup).click()
        time.sleep(2)
        self.assertFalse(check.isElementExist(driver,e_deleteGroup,groupName))
        #登出
        user.loginOut(account)
        driver.quit()
