# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/2/18 11:59
# 文件: Xpath.py
from time import sleep
import logging
from selenium.webdriver.common.action_chains import ActionChains

class Xpath():

    def __init__(self,driver):
        self.driver=driver

    #xpth定位单个元素
    def locate_element(self,locator,old_name=None,old_name2=None):
        tag = True
        n = 1
        while tag:
            if n <= 9:
                if old_name and old_name2==None:
                    try:
                        element =self.driver.find_element_by_xpath(locator.replace('%var%',old_name))
                        return element
                    except:
                        n += 1
                        sleep(1)
                elif old_name and old_name2:
                    try:
                        element =self.driver.find_element_by_xpath(locator.replace('%var%',old_name).replace('%edit%',old_name2))
                        return element
                    except:
                        n += 1
                        sleep(1)
                elif old_name==None and old_name2==None:
                    try:
                        element=self.driver.find_element_by_xpath(locator)
                        return element
                    except:
                        n += 1
                        sleep(1)
            else:
                tag = False
                logging.error('NoSuchElement!!!(locate_element:%s)'%locator)

    #xpth定位多个元素
    def locate_elements(self,locator,old_name=None):
        tag = True
        n = 1
        while tag:
            if n <= 9:
                if old_name:
                    try:
                        elements=self.driver.find_elements_by_xpath(locator.replace('%var%',old_name))
                        return elements
                    except:
                        n += 1
                        sleep(1)
                else:
                    try:
                        elements =self.driver.find_elements_by_xpath(locator)
                        return elements
                    except:
                        n += 1
                        sleep(1)
            else:
                tag = False
                logging.error('NoSuchElement!!!(locate_elements:%s)'%locator)

    #隐式等待，点击事件
    def click(self,locator,old_name=None,old_name2=None):
        tag = True
        n = 1
        while tag:
            if n <= 9:
                if old_name and old_name2==None:
                    try:
                        element=self.locate_element(locator,old_name)
                        element.click()
                        tag =False
                        break
                    except:
                        n+=1
                        sleep(1)
                elif old_name and old_name2:
                    try:
                        element=self.locate_element(locator,old_name,old_name2)
                        element.click()
                        tag = False
                        break
                    except:
                        n+=1
                        sleep(1)
                elif old_name == None and old_name2 == None:
                    try:
                        element=self.locate_element(locator)
                        element.click()
                        tag = False
                        break
                    except:
                        n+=1
                        sleep(1)
            else:
                tag = False
                logging.error('NoSuchElement!!!(click:%s)'%locator)

    #文本框输入事件
    def send_keys(self,locator,keys,old_name=None):
        tag = True
        n = 1
        while tag:
            if n <= 7:
                if old_name:
                    try:
                        element =self.locate_element(locator,old_name)
                        element.send_keys(keys)
                        tag = False
                        break
                    except:
                        n+=1
                        sleep(1)
                else:
                    try:
                        element =self.locate_element(locator)
                        element.send_keys(keys)
                        tag = False
                        break
                    except:
                        n+=1
                        sleep(1)
            else:
                tag = False
                logging.error('NoSuchElement!!!(send_keys:%s)'%locator)

    #清除文本框
    def text_clear(self,locator):
        self.locate_element(locator).clear()

    #鼠标悬停事件
    def move_to_element(self,locator,old_name=None):
        sleep(3)
        if old_name:
            element = self.locate_element(locator,old_name)
            ActionChains(self.driver).move_to_element(element).perform()
        else:
            element = self.locate_element(locator)
            ActionChains(self.driver).move_to_element(element).perform()

