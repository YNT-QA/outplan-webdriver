# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/18 13:39
# 文件: test_login.py
import sys
sys.path.append('..')
from selenium import webdriver
from common.get_path import GetPath
from common.get_value import GetValue
from pages.login import Login
import unittest
from common.assertFunction import AssertFunction

class Testlogin(unittest.TestCase):
    driver=None
    data=None
    ft = None

    def setUp(self):
        pass

    def test_login(self):
        global driver,data,ft
        data = GetValue()
        browser=GetPath(data.getvalue('driver'))
        driver=webdriver.Chrome(browser.get_filePath())
        user=Login(driver)
        user.login(data.getvalue('address'),data.getvalue('account'),data.getvalue('password'))
        ft = AssertFunction()
        self.assertTrue(ft.isElementExist(driver,'e_personalDetails'))

    def tearDown(self):
        driver.quit()