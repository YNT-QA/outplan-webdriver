# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/29 14:50
# 文件: scene_page.py
import sys
sys.path.append('..')
from time import sleep
from data.userinfo import *
from selenium.webdriver.support.ui import WebDriverWait
from src.common.incident import Incident

class ScenePage(Incident):

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    #进入话述配置菜单
    def into_scene(self):
        self.click(e_intoScene)
        sleep(2)

    #创建场景库
    def create_scene(self,sceneName):
        self.click(e_sceneManage)
        sleep(1)
        self.click(e_textVersion)
        sleep(1)
        self.click(e_createScene)
        sleep(1)

        elements=self.locate_elements(e_scene_Name)
        for element in elements:
            try:
                element.send_keys(sceneName)
            except:
                pass
        sleep(1)

        self.click(e_businessType)
        sleep(2)

        elements3 =self.locate_elements(e_type_financial)
        for element in elements3:
            try:
                element.click()
            except:
                pass
        sleep(2)

        elements4 =self.locate_elements(e_loans)
        for element in elements4:
            try:
                element.click()
            except:
                pass
        sleep(1)

        elements2=self.locate_elements(e_ensure)
        for element in elements2:
            try:
                element.click()
            except:
                pass

        flag=True
        while flag:
            try:
                self.locate_element(e_deleteScene,sceneName)
                flag=False
            except:
                pass
    #添加问答
    def add_question(self,name1,name2,triggerCondition,flag=False,name3=None):
        sleep(1)
        self.click(e_addQuestion)
        sleep(1)
        self.click(e_triggerCondition)
        sleep(1)
        #选择触发条件
        self.click(triggerCondition)
        sleep(1)
        if triggerCondition in e_selectOther:
            self.click(e_trigger_answer1_1,'触发问答1')
            sleep(1)
            self.click(e_job,name3)
            sleep(1)
            self.click(e_trigger_answer1_2,'触发问答1')
            sleep(1)
            self.click(e_job,'否定')

        self.send_keys(e_processName,name1)
        self.send_keys(e_wordDetils,name2)
        sleep(1)
        self.click(e_otherWay)
        sleep(1)
        self.click(e_syntheticVoice)
        sleep(1)
        if flag:
            try:
                #element = WebDriverWait(self.driver,15).until(lambda x: x.find_element_by_xpath(e_sure))
                self.driver.implicitly_wait(10)
                self.locate_element(e_sure)
                sleep(2)
                self.click(e_sure)
            except:
                print("定位失败")
            sleep(1)
            self.click(e_negate)
        sleep(3)
        self.click(e_submit)
        sleep(2)

    #添加结束语
    def add_endWords(self,name1,name2,triggerCondition,name3=None,name4=None,n=0,name5=None):
        self.click(e_endWord)
        sleep(1)
        self.click(e_triggerCondition)
        sleep(1)
        # 选择触发条件
        self.click(triggerCondition)
        sleep(1)
        if triggerCondition in e_selectOther:
            #触发问答1
            self.click(e_trigger_answer1_1,'触发问答1')
            sleep(1)
            self.click(e_job,name3)
            sleep(1)
            self.click(e_trigger_answer1_2,'触发问答1')
            sleep(1)
            self.click(e_job,name4)

            if n==2:
                #触发问答2
                self.click(e_addTriggerAnswer)
                sleep(1)
                self.click(e_trigger_answer1_1,'触发问答2')
                sleep(1)
                self.click(e_answer2,name3)
                sleep(1)
                self.click(e_trigger_answer1_2,'触发问答2')
                sleep(1)
                self.click(e_answer2,name5)

        self.send_keys(e_endWordName,name1)
        self.send_keys(e_wordDetils,name2)
        sleep(1)
        self.click(e_otherWay)
        sleep(1)
        self.click(e_syntheticVoice)
        sleep(3)
        self.click(e_submit)
        sleep(2)

    #编辑场景库
    def edit_scene(self,scenename,nameList):
        sleep(2)
        self.click(e_edit,scenename)
        sleep(1)
        self.click(e_mainProcess)
        sleep(1)
        #1开场语
        self.add_question(nameList[0],nameList[1],e_selectNatural)

        #2工作的打算
        self.add_question(nameList[2],nameList[3],e_selectNatural,True)

        #3挽留语1
        self.add_question(nameList[4],nameList[5],e_selectOther,True,name2_1)

        #4加微信
        self.add_question(nameList[6],nameList[7],e_selectOther,False,name3_1)

        #5结束语1
        self.add_endWords(nameList[8],nameList[9],e_selectOther,nameList[6],'匹配知识库',2,'其他任意回答')

        #6工作类型询问


        #7工作地点询问


        #8安排顾问


        #9加微信(安排顾问-否定)


        #10结束语1


        #11结束语2


    #删除场景库
    def delete_scene(self,sceneName):
        sleep(2)
        self.click(e_deleteScene,sceneName)
        sleep(1)
        self.click(e_endEnsure)
        sleep(2)