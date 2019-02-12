# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/16 16:09
# 文件: test_createplan.py
import sys
sys.path.append('..')
from selenium import webdriver
from pages.login import Login
import unittest
from common.assertFunction import AssertFunction
from pages.outplan_page import OutPlanPage
from pages.sip_page import SipPage
from pages.cusmanage import cusManage
import time
from data.userinfo import *
import os

class TestCreatePlan(unittest.TestCase):
    driver = None
    plan = None
    ft = None
    sip=None
    group = None
    user=None

    def setUp(self):
        global driver,ft,sip,group,user
        browser =os.path.dirname(os.path.abspath('..'))+'\\'+Driver
        driver = webdriver.Chrome(browser)
        #登录
        user = Login(driver)
        user.login(address,account,password)
        ft = AssertFunction()
        self.assertTrue(ft.isElementExist(driver,e_personalDetails))
        #添加线路
        sip =SipPage(driver)
        sip.into_sip()
        #添加线路
        sip.add_sip(sipAccount,sipPassword,sipIp,sipPort,city)
        #断言
        self.assertTrue(ft.isElementExist(driver,e_assertSip,sipAccount))
        #添加客户组导入号码
        group = cusManage(driver)
        group.cus_manage()
        group.add_group(groupName,number)
        self.assertTrue(ft.isElementExist(driver,e_deleteGroup,groupName))


    def test_createplan(self):
        u"""创建外呼计划"""
        #创建计划
        global plan
        plan=OutPlanPage(driver)
        plan.into_outPlan()
        plan.create_outplan(planName,sceneName,sipAccount,groupName)


    def tearDown(self):
        #删除计划
        plan.delete_plan(planName)
        #删除线路
        sip.into_sip()
        sip.delete_sip(sipAccount,'编辑','删除')
        #删除客户组
        group.cus_manage()
        group.delete_group(groupName)
        driver.find_element_by_xpath(e_closeCusGroup).click()
        time.sleep(2)
        self.assertFalse(ft.isElementExist(driver,e_deleteGroup,groupName))
        #断言
        self.assertFalse(ft.isElementExist(driver,e_assertSip,sipAccount))
        #登出
        user.loginOut(account)
        driver.quit()

