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
        self.assertTrue(check.isElementExist(driver,e_deleteScene,groupName))
        nameList=[name1_1,name1_2,name2_1,name2_2,name3_1,name3_2,name4_1,name4_2,name5_1,name5_2,name6_1,name6_2,name7_1,name7_2,name8_1,name8_2,name10_1,name11_1,name11_2]
        scene.edit_scene(groupName,nameList)
        driver.find_element_by_xpath(e_sceneManage).click()

    def tearDown(self):
        #删除场景库
        scene.delete_scene(groupName)
        #登出
        user.loginOut(account)
        driver.quit()