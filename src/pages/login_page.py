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

    #登出
    def loginOut(self,account):
        self.move_to_element(e_moveAccount,account)
        self.click(e_loginOut)
