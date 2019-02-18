# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/18 11:59
# 文件: login.py
import sys
sys.path.append('..')
import time
from selenium.webdriver.common.action_chains import ActionChains
from data.userinfo import *

class Login():

    def __init__(self,driver):
        self.driver=driver

    #登录
    def login(self,url,account,password):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(e_account).send_keys(account)
        time.sleep(1)
        self.driver.find_element_by_xpath(e_password).send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_xpath(e_login_button).click()
        time.sleep(3)

    #登出
    def loginOut(self,account):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(e_moveAccount.replace('%var%',account))).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath(e_loginOut).click()
        time.sleep(2)