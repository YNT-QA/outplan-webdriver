# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/15 17:26
# 文件: sip_page.py
import sys
sys.path.append('..')
import time
from selenium.webdriver.common.action_chains import ActionChains
from data.userinfo import *

class SipPage():

    def __init__(self,driver):
        self.driver = driver

    #进入线路管理菜单
    def into_sip(self):
        self.driver.find_element_by_xpath(e_sip).click()
        time.sleep(2)

    #添加线路
    def add_sip(self,sipAccount,sipPassword,sipIp,sipPort,city):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(e_addButton)).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath(e_ownSip).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(e_industryType).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(e_financial).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(e_education).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(e_sipText).send_keys(sipAccount)
        time.sleep(1)
        self.driver.find_element_by_xpath(e_sipPassword).send_keys(sipPassword)
        time.sleep(1)
        self.driver.find_element_by_xpath(e_ipText).send_keys(sipIp)
        time.sleep(1)
        self.driver.find_element_by_xpath(e_portText).clear()
        self.driver.find_element_by_xpath(e_portText).send_keys(sipPort)
        time.sleep(1)
        self.driver.find_element_by_xpath(e_locationSelectText).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(e_city.replace('%var%',city)).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(e_saveButton).click()
        time.sleep(2)

    #删除线路
    def delete_sip(self,sipAccount,edit,deleteButton):
        time.sleep(1)
        self.driver.find_element_by_xpath(e_updateSip.replace('%var%',sipAccount).replace('%edit%',edit)).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(e_sipState).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(e_saveButton).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(e_updateSip.replace('%var%',sipAccount).replace('%edit%',deleteButton)).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(e_ensure).click()
        time.sleep(2)