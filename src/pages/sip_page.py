# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/15 17:26
# 文件: sip_page.py
import sys
sys.path.append('..')
import time
from selenium.webdriver.common.action_chains import ActionChains
from data.userinfo import *
from src.common.incident import Incident

class SipPage(Incident):

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    #进入线路管理菜单
    def into_sip(self):
        self.click(e_sip)
        time.sleep(2)

    #添加线路
    def add_sip(self,sipAccount,sipPassword,sipIp,sipPort,city):
        ActionChains(self.driver).move_to_element(self.locate_element(e_addButton)).perform()
        time.sleep(1)
        self.click(e_ownSip)
        time.sleep(1)
        self.click(e_industryType)
        time.sleep(1)
        self.click(e_financial)
        time.sleep(1)
        self.click(e_education)
        time.sleep(1)
        self.send_keys(e_sipText,sipAccount)
        time.sleep(1)
        self.send_keys(e_sipPassword,sipPassword)
        time.sleep(1)
        self.send_keys(e_ipText,sipIp)
        time.sleep(1)
        self.text_clear(e_portText)
        self.send_keys(e_portText,sipPort)
        time.sleep(1)
        self.click(e_locationSelectText)
        time.sleep(1)
        self.click(e_city,city)
        time.sleep(1)
        self.click(e_saveButton)
        time.sleep(2)

    #删除线路
    def delete_sip(self,sipAccount,edit,deleteButton):
        time.sleep(1)
        self.click(e_updateSip,sipAccount,edit)
        time.sleep(1)
        self.click(e_sipState)
        time.sleep(1)
        self.click(e_saveButton)
        time.sleep(1)
        self.click(e_updateSip,sipAccount,deleteButton)
        time.sleep(1)
        self.click(e_ensure)
        time.sleep(2)