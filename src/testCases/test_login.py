# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/18 13:39
# 文件: test_login.py
from selenium import webdriver
from src.pages.login_page import Login
import unittest
from src.common.assertfunc import AssertFunction
from src.common.browsers import Browsers
from data.userinfo import *

class Testlogin(unittest.TestCase):
    driver=None
    check = None
    user=None

    @classmethod
    def setUpClass(cls):
        print('first...')

    @classmethod
    def tearDownClass(cls):
        print('last...')

    def setUp(self):
        global driver
        browser = Browsers(browserType)
        driver = webdriver.Chrome(browser.select_browser())

    def test_login(self):
        u"""账号登录"""
        global check,user
        user=Login(driver)
        user.login(address,account,password)
        check = AssertFunction()
        self.assertTrue(check.isElementExist(driver,e_personalDetails))
        self.assertIn('homepage',driver.current_url)

    def tearDown(self):
        #登出
        user.loginOut(account)
        driver.quit()

