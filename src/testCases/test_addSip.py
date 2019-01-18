# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/16 10:19
# 文件: test_addSip.py
import sys
sys.path.append('..')
from selenium import webdriver
from common.get_path import GetPath
from common.get_value import GetValue
from pages.login import Login
import unittest
from common.assertFunction import AssertFunction
from pages.sip_page import SipPage

class TestAddSip(unittest.TestCase):
    driver=None
    data=None
    sip=None
    ft=None
    user=None

    def setUp(self):
        global driver,data,ft,user
        data = GetValue()
        browser = GetPath(data.getvalue('driver'))
        driver = webdriver.Chrome(browser.get_filePath())
        #登录
        user = Login(driver)
        user.login(data.getvalue('address'),data.getvalue('account'),data.getvalue('password'))
        ft = AssertFunction()
        self.assertTrue(ft.isElementExist(driver,'e_personalDetails'))

    def test_addGroupNum(self):
        u"""添加线路"""
        global sip
        sip=SipPage(driver)
        sip.into_sip()
        #添加线路
        sip.add_sip(data.getvalue('sipAccount'),data.getvalue('sipPassword'),data.getvalue('sipIp'),data.getvalue('sipPort'),data.getvalue('city'))
        #断言
        self.assertTrue(ft.isElementExist(driver,'e_assertSip',data.getvalue('sipAccount')))

    def tearDown(self):
        #删除线路
        sip.delete_sip(data.getvalue('sipAccount'),'编辑','删除')
        #断言
        self.assertFalse(ft.isElementExist(driver,'e_assertSip',data.getvalue('sipAccount')))
        #登出
        user.loginOut(data.getvalue('account'))
        driver.quit()