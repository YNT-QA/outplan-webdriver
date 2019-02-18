# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/2/18 11:59
# 文件: incident.py

class Incident():

    def __init__(self,driver):
        self.driver=driver

    def locate_element(self,locator,old_name=None):
        if old_name:
            return self.driver.find_element_by_xpath(locator.replace('%var%',old_name))
        else:
            return self.driver.find_element_by_xpath(locator)

    def locate_elements(self,locator,old_name=None):
        if old_name:
            return self.driver.find_elements_by_xpath(locator.replace('%var%',old_name))
        else:
            return self.driver.find_elements_by_xpath(locator)

    def click(self,locator,old_name=None,old_name2=None):
        if old_name and old_name2==None:
            self.locate_element(locator.replace('%var%',old_name)).click()
        elif old_name and old_name2:
            return self.driver.find_element_by_xpath(locator.replace('%var%',old_name).replace('%edit%',old_name2)).click()
        else:
            self.locate_element(locator).click()

    def send_keys(self,locator,keys,old_name=None):
        if old_name:
            self.locate_element(locator.replace('%var%',old_name)).send_keys(keys)
        else:
            self.locate_element(locator).send_keys(keys)

    def text_clear(self,locator):
        self.driver.find_element_by_xpath(locator).clear()