# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/19 11:38
# 文件: test_addgroup.py
import sys
sys.path.append('..')
from selenium import webdriver
from pages.login import Login
from pages.cusmanage import cusManage
import unittest
import time
from common.assertFunction import AssertFunction
from data.userinfo import *
import os

class TestAddGroupNum(unittest.TestCase):
    driver=None
    group=None
    ft=None
    user=None

    def setUp(self):
        global driver,ft,user

        browser = os.path.dirname(os.path.abspath('..'))+'\\'+Driver
        driver = webdriver.Chrome(browser)
        user = Login(driver)
        user.login(address,account,password)
        ft = AssertFunction()
        self.assertTrue(ft.isElementExist(driver,e_personalDetails))

    def test_addGroupNum(self):
        u"""添加客户组号码"""
        global group
        group=cusManage(driver)
        group.cus_manage()
        time.sleep(2)
        group.add_group(groupName,number)
        time.sleep(2)
        self.assertTrue(ft.isElementExist(driver,e_deleteGroup,groupName))

    def tearDown(self):
        #删除客户组
        group.delete_group(groupName)
        driver.find_element_by_xpath(e_closeCusGroup).click()
        time.sleep(2)
        self.assertFalse(ft.isElementExist(driver,e_deleteGroup,groupName))
        #登出
        user.loginOut(account)
        driver.quit()
