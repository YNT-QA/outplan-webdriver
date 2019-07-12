# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/2/18 11:59
# 文件: Xpath.py
from time import sleep
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from poium import Page,PageElements,PageElement
import datetime
import os
from src.common.logger import Logger

#create a logger instance
logger = Logger(logger="BasePage").getlog()
class Xpath(Page):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    #xpth定位单个元素
    def locate_element(self,locator,old_name=None,old_name2=None,timeout=10):
        tag = True
        n = 1
        while tag:
            if n <= timeout:
                if old_name and old_name2==None:
                    try:
                        element =self.driver.find_element_by_xpath(locator.replace('%var%',old_name))
                        logger.info("locate element %s"%element)
                        return element
                    except:
                        n += 1
                        sleep(1)
                elif old_name and old_name2:
                    try:
                        element =self.driver.find_element_by_xpath(locator.replace('%var%',old_name).replace('%edit%',old_name2))
                        logger.info("locate element %s" % element)
                        return element
                    except:
                        n += 1
                        sleep(1)
                elif old_name==None and old_name2==None:
                    try:
                        element=self.driver.find_element_by_xpath(locator)
                        logger.info("locate element %s" % element)
                        return element
                    except:
                        n += 1
                        sleep(1)
            else:
                #tag=False
                #logging.error('NoSuchElement!!!(locate_element:%s)'%locator)
                raise ValueError('NoSuchElement!!!(locate_element:%s)'%locator)

    #xpth定位多个元素
    def locate_elements(self,locator,old_name=None,timeout=10):
        tag = True
        n = 1
        while tag:
            if n <= timeout:
                if old_name:
                    try:
                        elements=self.driver.find_elements_by_xpath(locator.replace('%var%',old_name))
                        logger.info("locate elements %s" % elements)
                        return elements
                    except:
                        n += 1
                        sleep(1)
                else:
                    try:
                        elements =self.driver.find_elements_by_xpath(locator)
                        logger.info("locate elements %s" % elements)
                        return elements
                    except:
                        n += 1
                        sleep(1)
            else:
                #tag = False
                #logging.error('NoSuchElement!!!(locate_elements:%s)'%locator)
                raise ValueError('NoSuchElement!!!(locate_elements:%s)' % locator)

    #隐式等待，点击事件
    def click(self,locator,old_name=None,old_name2=None,timeout=10):
        tag = True
        n = 1
        while tag:
            if n <= timeout:
                if old_name and old_name2==None:
                    try:
                        element=self.locate_element(locator,old_name)
                        element.click()
                        logger.info("click element %s" % element)
                        tag =False
                        break
                    except:
                        n+=1
                        sleep(1)
                elif old_name and old_name2:
                    try:
                        element=self.locate_element(locator,old_name,old_name2)
                        element.click()
                        logger.info("click element %s" % element)
                        tag = False
                        break
                    except:
                        n+=1
                        sleep(1)
                elif old_name == None and old_name2 == None:
                    try:
                        element=self.locate_element(locator)
                        element.click()
                        logger.info("click element %s" % element)
                        tag = False
                        break
                    except:
                        n+=1
                        sleep(1)
            else:
                #tag = False
                #logging.error('NoSuchElement!!!(click:%s)'%locator)
                raise ValueError('NoSuchElement!!!(click:%s)'%locator)

    #文本框输入事件
    def send_keys(self,locator,keys,old_name=None,timeout=10):
        tag = True
        n = 1
        while tag:
            if n <= timeout:
                if old_name:
                    try:
                        element =self.locate_element(locator,old_name)
                        element.send_keys(keys)
                        logger.info("send_keys %s" % element)
                        tag = False
                        break
                    except:
                        n+=1
                        sleep(1)
                else:
                    try:
                        element =self.locate_element(locator)
                        element.send_keys(keys)
                        logger.info("send_keys %s" % element)
                        tag = False
                        break
                    except:
                        n+=1
                        sleep(1)
            else:
                #tag = False
                #logging.error('NoSuchElement!!!(send_keys:%s)'%locator)
                raise ValueError('NoSuchElement!!!(send_keys:%s)'%locator)

    #清除文本框
    def text_clear(self,locator):
        #self.locate_element(locator).clear()
        self.locate_element(locator).send_keys(Keys.CONTROL+'a')
        logger.info("clear text %s" % locator)


    #鼠标悬停事件
    def move_to_element(self,locator,old_name=None):
        sleep(4)
        if old_name:
            element = self.locate_element(locator,old_name)
            ActionChains(self.driver).move_to_element(element).perform()
            logger.info("move_to_element %s" % element)
        else:
            element = self.locate_element(locator)
            ActionChains(self.driver).move_to_element(element).perform()
            logger.info("move_to_element %s" % element)

    #截图保存
    def get_windows_img(self):
        now_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screen_name = os.path.dirname(os.path.abspath('..')) + '\\' + 'screenshot\\' + now_time + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

