# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/29 17:03
# 文件: test_createscene.py
import unittest
import sys
sys.path.append('..')
from selenium import webdriver
from common.get_path import GetPath
from common.get_value import GetValue
from pages.login import Login
from common.assertFunction import AssertFunction
from pages.scene_page import ScenePage

class TestCreateScene(unittest.TestCase):
    driver = None
    data = None
    plan = None
    ft = None
    user=None
    scene=None

    def setUp(self):
        global driver,data,ft,user
        data = GetValue()
        browser = GetPath(data.getvalue('driver'))
        driver = webdriver.Chrome(browser.get_filePath())
        # 登录
        user = Login(driver)
        user.login(data.getvalue('address'), data.getvalue('account'), data.getvalue('password'))
        ft = AssertFunction()
        self.assertTrue(ft.isElementExist(driver,'e_personalDetails'))

    def test_create_scene(self):
        u"""创建场景库"""
        global scene
        scene=ScenePage(driver)
        scene.into_scene()
        scene.create_scene(data.getvalue('groupName'))
        self.assertTrue(ft.isElementExist(driver,'e_deleteScene',data.getvalue('groupName')))

    def tearDown(self):
        scene.delete_scene(data.getvalue('groupName'))
        # 登出
        user.loginOut(data.getvalue('account'))
        driver.quit()