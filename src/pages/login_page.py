# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/18 11:59
# 文件: login.py
import sys
sys.path.append('..')
import time
from selenium.webdriver.common.action_chains import ActionChains
from data.userinfo import *
from src.common.xpth import Xpth

class Login(Xpth):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    #登录
    def login(self,url,account,password):
        self.driver.get(url)
        self.driver.maximize_window()
        self.send_keys(e_account,account)
        self.send_keys(e_password,password)
        self.click(e_login_button)
        time.sleep(3)

    #登出
    def loginOut(self,account):
        ActionChains(self.driver).move_to_element(self.locate_element(e_moveAccount.replace('%var%',account))).perform()
        self.click(e_loginOut)