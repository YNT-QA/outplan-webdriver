# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/29 17:03
# 文件: test_createscene.py
import unittest
import sys
sys.path.append('..')
from selenium import webdriver
from pages.login_page import Login
from common.assertfunc import AssertFunction
from common.browsers import Browsers
from pages.scene_page import ScenePage
from data.userinfo import *

class TestCreateScene(unittest.TestCase):
    driver = None
    plan = None
    check = None
    user=None
    scene=None

    def setUp(self):
        global driver,check,user
        browser = Browsers(browserType)
        driver = webdriver.Chrome(browser.select_browser())
        #登录
        user = Login(driver)
        user.login(address,account,password)
        check = AssertFunction()
        self.assertTrue(check.isElementExist(driver,e_personalDetails))
        self.assertIn('homepage', driver.current_url)

    def test_create_scene(self):
        u"""创建场景库"""
        global scene
        scene=ScenePage(driver)
        scene.into_scene()
        scene.create_scene(groupName)
        self.assertTrue(check.isElementExist(driver,e_scene,groupName))
        scene.edit_scene(groupName,nameList)

    def tearDown(self):
        #删除场景库
        scene.delete_scene(groupName)
        #登出
        user.loginOut(account)
        driver.quit()