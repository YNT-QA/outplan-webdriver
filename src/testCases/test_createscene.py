# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/29 17:03
# 文件: test_createscene.py
import unittest
import sys
sys.path.append('..')
from selenium import webdriver
from pages.login import Login
from common.assertFunction import AssertFunction
from pages.scene_page import ScenePage
from data.userinfo import *
import os

class TestCreateScene(unittest.TestCase):
    driver = None
    plan = None
    check = None
    user=None
    scene=None

    def setUp(self):
        global driver,check,user
        browser = os.path.dirname(os.path.abspath('..'))+'\\'+Driver
        driver = webdriver.Chrome(browser)
        #登录
        user = Login(driver)
        user.login(address,account,password)
        check = AssertFunction()
        self.assertTrue(check.isElementExist(driver,e_personalDetails))

    def test_create_scene(self):
        u"""创建场景库"""
        global scene
        scene=ScenePage(driver)
        scene.into_scene()
        scene.create_scene(groupName)
        self.assertTrue(check.isElementExist(driver,e_deleteScene,groupName))

    def tearDown(self):
        scene.delete_scene(groupName)
        #登出
        user.loginOut(account)
        driver.quit()