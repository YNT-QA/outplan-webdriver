# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/19 11:38
# 文件: test_addgroup.py
import sys
sys.path.append('..')
from selenium import webdriver
from common.get_path import GetPath
from common.get_value import GetValue
from pages.login import Login
from pages.cusmanage import cusManage
import unittest
import time
from common.assertFunction import AssertFunction

class TestAddGroupNum(unittest.TestCase):
    driver=None
    data=None
    group=None
    ft=None

    def setUp(self):
        global driver,data,ft
        data = GetValue()
        browser = GetPath(data.getvalue('driver'))
        driver = webdriver.Chrome(browser.get_filePath())
        user = Login(driver)
        user.login(data.getvalue('address'), data.getvalue('account'), data.getvalue('password'))
        ft = AssertFunction()
        self.assertTrue(ft.isElementExist(driver,'e_personalDetails'))

    def test_addGroupNum(self):
        global group
        group=cusManage(driver)
        group.cus_manage()
        time.sleep(2)
        group.add_group(data.getvalue('groupName'),data.getvalue('number'))
        time.sleep(2)
        self.assertTrue(ft.isElementExist(driver,'e_deleteGroup',data.getvalue('groupName')))

    def tearDown(self):
        #删除客户组
        group.delete_group(data.getvalue('groupName'))
        driver.find_element_by_xpath(data.getvalue('e_closeCusGroup')).click()
        time.sleep(2)
        self.assertFalse(ft.isElementExist(driver,'e_deleteGroup',data.getvalue('groupName')))
        driver.quit()
