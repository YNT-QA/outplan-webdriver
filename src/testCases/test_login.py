# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/18 13:39
# 文件: test_login.py
import sys
sys.path.append('..')
from selenium import webdriver
from pages.login import Login
import unittest
from common.assertFunction import AssertFunction
import os
from data.userinfo import *


class Testlogin(unittest.TestCase):
    driver=None
    ft = None
    user=None

    def setUp(self):
        pass

    def test_login(self):
        u"""账号登录"""
        global driver,ft,user
        browser=os.path.dirname(os.path.abspath('..'))+'\\'+Driver
        driver=webdriver.Chrome(browser)
        user=Login(driver)
        user.login(address,account,password)
        ft = AssertFunction()
        self.assertTrue(ft.isElementExist(driver,e_personalDetails))

    def tearDown(self):
        #登出
        user.loginOut(account)
        driver.quit()