# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/16 16:09
# 文件: test_createplan.py
import sys
sys.path.append('..')
from selenium import webdriver
from common.get_path import GetPath
from common.get_value import GetValue
from pages.login import Login
import unittest
from common.assertFunction import AssertFunction
from pages.outplan_page import OutPlanPage
from pages.sip_page import SipPage
from pages.cusmanage import cusManage
import time

class TestCreatePlan(unittest.TestCase):
    driver = None
    data = None
    plan = None
    ft = None
    sip=None
    group = None

    def setUp(self):
        global driver,data,ft,sip,group
        data = GetValue()
        browser =GetPath(data.getvalue('driver'))
        driver = webdriver.Chrome(browser.get_filePath())
        # 登录
        user = Login(driver)
        user.login(data.getvalue('address'),data.getvalue('account'),data.getvalue('password'))
        ft = AssertFunction()
        self.assertTrue(ft.isElementExist(driver,'e_personalDetails'))
        #添加线路
        sip =SipPage(driver)
        sip.into_sip()
        #添加线路
        sip.add_sip(data.getvalue('sipAccount'),data.getvalue('sipPassword'),data.getvalue('sipIp'),data.getvalue('sipPort'),data.getvalue('city'))
        #断言
        self.assertTrue(ft.isElementExist(driver,'e_assertSip',data.getvalue('sipAccount')))
        #添加客户组导入号码
        group = cusManage(driver)
        group.cus_manage()
        group.add_group(data.getvalue('groupName'),data.getvalue('number'))
        self.assertTrue(ft.isElementExist(driver, 'e_deleteGroup', data.getvalue('groupName')))


    def test_createplan(self):
        #创建计划
        global plan
        plan=OutPlanPage(driver)
        plan.into_outPlan()
        plan.create_outplan(data.getvalue('planName'),data.getvalue('sceneName'),data.getvalue('sipAccount'),data.getvalue('groupName'))


    def tearDown(self):
        #删除计划
        plan.delete_plan(data.getvalue('planName'))
        #删除线路
        sip.into_sip()
        sip.delete_sip(data.getvalue('sipAccount'),'编辑','删除')
        #删除客户组
        group.cus_manage()
        group.delete_group(data.getvalue('groupName'))
        driver.find_element_by_xpath(data.getvalue('e_closeCusGroup')).click()
        time.sleep(2)
        self.assertFalse(ft.isElementExist(driver, 'e_deleteGroup',data.getvalue('groupName')))
        #断言
        self.assertFalse(ft.isElementExist(driver,'e_assertSip',data.getvalue('sipAccount')))
        driver.quit()

