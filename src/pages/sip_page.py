# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/15 17:26
# 文件: sip_page.py
import sys
sys.path.append('..')
from common.get_value import GetValue
import time
from selenium.webdriver.common.action_chains import ActionChains

class SipPage():

    def __init__(self,driver):
        self.driver = driver
        self.data = GetValue()

    #进入线路管理菜单
    def into_sip(self):
        self.driver.find_element_by_xpath(self.data.getvalue('e_sip')).click()
        time.sleep(2)

    #添加线路
    def add_sip(self,sipAccount,sipPassword,sipIp,sipPort,city):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.data.getvalue('e_addButton'))).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.data.getvalue('e_ownSip')).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.data.getvalue('e_industryType')).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.data.getvalue('e_financial')).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.data.getvalue('e_education')).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.data.getvalue('e_sipText')).send_keys(sipAccount)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.data.getvalue('e_sipPassword')).send_keys(sipPassword)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.data.getvalue('e_ipText')).send_keys(sipIp)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.data.getvalue('e_portText')).clear()
        self.driver.find_element_by_xpath(self.data.getvalue('e_portText')).send_keys(sipPort)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.data.getvalue('e_locationSelectText')).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.data.getvalue('e_city').replace('%var%',city)).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.data.getvalue('e_saveButton')).click()
        time.sleep(2)

    #删除线路
    def delete_sip(self,sipAccount,edit,deleteButton):
        time.sleep(1)
        self.driver.find_element_by_xpath(self.data.getvalue('e_updateSip').replace('%var%',sipAccount).replace('%edit%',edit)).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.data.getvalue('e_sipState')).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.data.getvalue('e_saveButton')).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.data.getvalue('e_updateSip').replace('%var%',sipAccount).replace('%edit%',deleteButton)).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.data.getvalue('e_ensure')).click()
        time.sleep(2)