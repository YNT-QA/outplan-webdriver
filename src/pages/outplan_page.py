# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/16 15:15
# 文件: outplan_page.py
import sys
sys.path.append('..')
import time
from selenium.webdriver.common.action_chains import ActionChains
from data.userinfo import *

class OutPlanPage():

    def __init__(self,driver):
        self.driver = driver

    #进入外呼计划菜单
    def into_outPlan(self):
        self.driver.find_element_by_xpath(e_outPlanMenu).click()
        time.sleep(2)

    #创建外呼计划
    def create_outplan(self,planName,sceneName,sipAccount,groupName,callType='立即呼叫'):

        self.driver.find_element_by_xpath(e_createPlan).click()
        time.sleep(2)

        elements=self.driver.find_elements_by_xpath(e_planName)
        for element in elements:
            try:
                element.send_keys(planName)
            except:
                pass
        time.sleep(2)

        elements2=self.driver.find_elements_by_xpath(e_selectScene)
        for element in elements2:
            try:
                element.click()
            except:
                pass
        time.sleep(2)

        self.driver.find_element_by_xpath(e_sceneName.replace('%var%',sceneName)).click()
        #选择呼叫类型
        if callType=='立即呼叫':
            self.select_callType(callType)

        elif callType=='定时呼叫':
            self.select_callType(callType)

        else:
            self.select_callType(callType)

        time.sleep(2)
        elements3 = self.driver.find_elements_by_xpath(e_selectSip)
        for element in elements3:
            try:
                element.click()
            except:
                pass
        time.sleep(2)

        self.driver.find_element_by_xpath(e_allSelectSip).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(e_addSip.replace('%var%',sipAccount)).click()
        time.sleep(2)

        elements4 = self.driver.find_elements_by_xpath(e_group)
        for element in elements4:
            try:
                element.click()
            except:
                pass

        elements5=self.driver.find_elements_by_xpath(e_down)
        for element in elements5:
            try:
                ActionChains(self.driver).drag_and_drop_by_offset(element,0,10000).perform()
            except:
                pass
        time.sleep(2)

        self.driver.find_element_by_xpath(e_checkGroup.replace('%var%',groupName)).click()
        time.sleep(2)
        elements6 = self.driver.find_elements_by_xpath(e_ensure)
        for element in elements6:
            try:
                element.click()
            except:
                pass
        time.sleep(3)
        elements7 = self.driver.find_elements_by_xpath(e_closeSuccessPlan)
        for element in elements7:
            try:
                element.click()
            except:
                pass


    def select_callType(self,callType):
        elements = self.driver.find_elements_by_xpath(e_callType.replace('%var%',callType))
        for element in elements:
            try:
                element.click()
            except:
                pass


    #删除计划
    def delete_plan(self,planName):
        flag=True
        n=1
        while flag:
            time.sleep(2)
            self.driver.refresh()
            try:
                #已结束状态点击删除计划
                self.driver.find_element_by_xpath(e_finish.replace('%var%',planName))
                ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(e_plan.replace('%var%',planName))).perform()
                time.sleep(2)
                self.driver.find_element_by_xpath(e_x).click()
                time.sleep(2)
                self.driver.find_element_by_xpath(e_x_ensure).click()
                flag=False
            except:
                try:
                    #已暂停状态点击删除计划
                    self.driver.find_element_by_xpath(e_planSuspended.replace('%var%',planName))
                    time.sleep(2)
                    self.driver.find_element_by_xpath(e_end.replace('%var%',planName)).click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(e_endEnsure.replace('%var%',planName)).click()
                    time.sleep(2)
                    self.driver.refresh()
                    time.sleep(2)
                    ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(e_plan.replace('%var%',planName))).perform()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(e_x).click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(e_x_ensure).click()
                    flag = False
                except:
                    pass
            if n>50:
                flag = False
            n+=1
        time.sleep(2)