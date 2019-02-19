# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/2/18 11:59
# 文件: incident.py
from time import sleep

class Xpth():

    def __init__(self,driver):
        self.driver=driver

    #xpth定位单个元素
    def locate_element(self,locator,old_name=None,old_name2=None):
        tag = True
        n = 1
        while tag:
            if n <= 10:
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

    #xpth定位多个元素
    def locate_elements(self,locator,old_name=None):
        tag = True
        n = 1
        while tag:
            if n <= 10:
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

    #隐式等待，点击事件
    def click(self,locator,old_name=None,old_name2=None):
        tag = True
        n = 1
        while tag:
            if n <= 10:
                if old_name and old_name2==None:
                    try:
                        element=self.locate_element(locator.replace('%var%',old_name))
                        element.click()
                        tag =False
                    except:
                        n+=1
                        sleep(1)
                elif old_name and old_name2:
                    try:
                        element=self.locate_element(locator,old_name,old_name2)
                        element.click()
                        tag = False
                    except:
                        n+=1
                        sleep(1)
                elif old_name == None and old_name2 == None:
                    try:
                        element=self.locate_element(locator)
                        element.click()
                        tag = False
                    except:
                        n+=1
                        sleep(1)
            else:
                tag = False

    #文本框输入事件
    def send_keys(self,locator,keys,old_name=None):
        if old_name:
            self.locate_element(locator.replace('%var%',old_name)).send_keys(keys)
        else:
            self.locate_element(locator).send_keys(keys)

    def text_clear(self,locator):
        self.locate_element(locator).clear()