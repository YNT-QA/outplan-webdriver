# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/2/19 18:02
# 文件: test_login_cms.py

from selenium import webdriver
from src.pages.logincms_page import LoginCms
import unittest
from src.common.assertfunc import AssertFunction
from src.common.browsers import Browsers
from data.userinfo_cms import *
from data.userinfo import *

class TestloginCms(unittest.TestCase):
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

    def test_login_cms(self):
        u"""外呼后台账号登录"""
        global check,user
        user=LoginCms(driver)
        user.login_cms(plan_url_cms,plan_act_cms,plan_pswd_cms)
        check = AssertFunction()
        self.assertTrue(check.isElementExist(driver,e_username_cms,acc_name))

    def tearDown(self):
        #登出
        user.loginOut_cms(acc_name)
        driver.quit()