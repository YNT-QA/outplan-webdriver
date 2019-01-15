# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/18 11:59
# 文件: login.py
import sys
sys.path.append('..')
from common.get_value import GetValue
import time

class Login():
    global data
    data=GetValue()

    def __init__(self,driver):
        self.driver=driver

    def login(self,url,account,password):
        global data
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(data.getvalue('e_account')).send_keys(account)
        time.sleep(1)
        self.driver.find_element_by_xpath(data.getvalue('e_password')).send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_xpath(data.getvalue('e_login_button')).click()
        time.sleep(2)

