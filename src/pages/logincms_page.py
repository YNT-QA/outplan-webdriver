# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/2/19 17:54
# 文件: logincms_page.py

import sys
sys.path.append('..')
import time
from data.userinfo_cms import *
from src.common.xpth import Xpth

class LoginCms(Xpth):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    #登录
    def login_cms(self,url,account,password):
        self.driver.get(url)
        self.driver.maximize_window()
        self.send_keys(e_act_cms,account)
        self.send_keys(e_pswd_cms,password)
        self.click(e_lgButton_cms)

    #登出
    def loginOut_cms(self,account):
        self.move_to_element(e_mvacc_cms,account)
        self.click(e_lgOut_cms)
        time.sleep(1)