# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/15 17:26
# 文件: sip_page.py
import sys
sys.path.append('..')
from data.userinfo import *
from src.common.xpath import Xpath

class SipPage(Xpath):

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    #进入线路管理菜单
    def into_sip(self):
        self.click(e_sip)

    #添加线路
    def add_sip(self,sipAccount,sipPassword,sipIp,sipPort,city):
        self.move_to_element(e_addButton)
        self.click(e_ownSip)
        self.click(e_industryType)
        self.click(e_financial)
        self.click(e_education)
        self.send_keys(e_sipText,sipAccount)
        self.send_keys(e_sipPassword,sipPassword)
        self.send_keys(e_ipText,sipIp)
        self.text_clear(e_portText)
        self.send_keys(e_portText,sipPort)
        self.click(e_locationSelectText)
        self.click(e_city,city)
        self.click(e_saveButton)

    #删除线路
    def delete_sip(self,sipAccount,edit,deleteButton):
        self.click(e_updateSip,sipAccount,edit)
        self.click(e_sipState)
        self.click(e_saveButton)
        self.click(e_updateSip,sipAccount,deleteButton)
        self.click(e_ensure)