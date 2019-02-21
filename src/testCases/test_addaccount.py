# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/2/20 13:41
# 文件: test_addaccount.py

import unittest
from selenium import webdriver
from src.common.browsers import Browsers
from src.common.assertfunc import AssertFunction
from data.userinfo import *
from data.userinfo_cms import *
from src.pages.logincms_page import LoginCms
from src.pages.accmgcms_page import AccMgCms

class TestAddacc(unittest.TestCase):
    user=None
    driver=None
    check = None
    cus=None

    @classmethod
    def setUpClass(cls):
        global driver
        browser = Browsers(browserType)
        driver = webdriver.Chrome(browser.select_browser())

    def setUp(self):
        global check, user
        user = LoginCms(driver)
        user.login_cms(plan_url_cms, plan_act_cms, plan_pswd_cms)
        check = AssertFunction()
        self.assertTrue(check.isElementExist(driver, e_username_cms, acc_name))

    def test_addcusacc(self):
        '''外呼后台添加正式账号'''
        global cus
        cus=AccMgCms(driver)
        cus.into_accmg()
        cus.add_account(cusemail_cms,cusphone_cms,companyname_cms,num)


    def tearDown(self):
        #删除正式账号
        cus.delete_account()

    @classmethod
    def tearDownClass(cls):
        # 登出
        user.loginOut_cms(acc_name)
        driver.quit()