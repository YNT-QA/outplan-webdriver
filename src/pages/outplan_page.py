# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/16 15:15
# 文件: outplan_page.py
import sys
sys.path.append('..')
import time
from selenium.webdriver.common.action_chains import ActionChains
from data.userinfo import *
from src.common.incident import Incident

class OutPlanPage(Incident):

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    #进入外呼计划菜单
    def into_outPlan(self):
        self.click(e_outPlanMenu)
        time.sleep(2)

    #创建外呼计划
    def create_outplan(self,planName,sceneName,sipAccount,groupName,callType='立即呼叫'):
        self.click(e_createPlan)
        time.sleep(2)

        elements=self.locate_elements(e_planName)
        for element in elements:
            try:
                element.send_keys(planName)
            except:
                pass
        time.sleep(2)

        elements2=self.locate_elements(e_selectScene)
        for element in elements2:
            try:
                element.click()
            except:
                pass
        time.sleep(2)

        self.click(e_sceneName,sceneName)
        #选择呼叫类型
        if callType=='立即呼叫':
            self.select_callType(callType)

        elif callType=='定时呼叫':
            self.select_callType(callType)

        else:
            self.select_callType(callType)

        time.sleep(2)
        elements3 = self.locate_elements(e_selectSip)
        for element in elements3:
            try:
                element.click()
            except:
                pass
        time.sleep(2)

        self.click(e_allSelectSip)
        time.sleep(2)
        self.click(e_addSip,sipAccount)
        time.sleep(2)

        elements4 = self.locate_elements(e_group)
        for element in elements4:
            try:
                element.click()
            except:
                pass

        elements5=self.locate_elements(e_down)
        for element in elements5:
            try:
                ActionChains(self.driver).drag_and_drop_by_offset(element,0,10000).perform()
            except:
                pass
        time.sleep(2)

        self.click(e_checkGroup,groupName)
        time.sleep(2)
        elements6 = self.locate_elements(e_ensure)
        for element in elements6:
            try:
                element.click()
            except:
                pass
        time.sleep(3)
        elements7 = self.locate_elements(e_closeSuccessPlan)
        for element in elements7:
            try:
                element.click()
            except:
                pass


    def select_callType(self,callType):
        elements = self.locate_elements(e_callType,callType)
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
                self.locate_element(e_finish,planName)
                ActionChains(self.driver).move_to_element(self.locate_element(e_plan,planName)).perform()
                time.sleep(2)
                self.click(e_x)
                time.sleep(2)
                self.click(e_x_ensure)
                flag=False
            except:
                try:
                    #已暂停状态点击删除计划
                    self.locate_element(e_planSuspended,planName)
                    time.sleep(2)
                    self.click(e_end,planName)
                    time.sleep(2)
                    self.click(e_endEnsure,planName)
                    time.sleep(2)
                    self.driver.refresh()
                    time.sleep(2)
                    ActionChains(self.driver).move_to_element(self.locate_element(e_plan,planName)).perform()
                    time.sleep(2)
                    self.click(e_x)
                    time.sleep(2)
                    self.click(e_x_ensure)
                    flag = False
                except:
                    pass
            if n>50:
                flag = False
            n+=1
        time.sleep(2)