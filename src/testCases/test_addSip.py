# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/16 10:19
# 文件: test_addSip.py
import sys
sys.path.append('..')
from selenium import webdriver
from pages.login import Login
import unittest
from common.assertFunction import AssertFunction
from pages.sip_page import SipPage
from data.userinfo import *
import os

class TestAddSip(unittest.TestCase):
    driver=None
    sip=None
    ft=None
    user=None

    def setUp(self):
        global driver,ft,user
        browser = os.path.dirname(os.path.abspath('..'))+'\\'+Driver
        driver = webdriver.Chrome(browser)
        #登录
        user = Login(driver)
        user.login(address,account,password)
        ft = AssertFunction()
        self.assertTrue(ft.isElementExist(driver,e_personalDetails))

    def test_addSip(self):
        u"""添加线路"""
        global sip
        sip=SipPage(driver)
        sip.into_sip()
        #添加线路
        sip.add_sip(sipAccount,sipPassword,sipIp,sipPort,city)
        #断言
        self.assertTrue(ft.isElementExist(driver,e_assertSip,sipAccount))

    def tearDown(self):
        #删除线路
        sip.delete_sip(sipAccount,'编辑','删除')
        #断言
        self.assertFalse(ft.isElementExist(driver,e_assertSip,sipAccount))
        #登出
        user.loginOut(account)
        driver.quit()