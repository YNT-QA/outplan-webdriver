# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/29 14:50
# 文件: scene_page.py
import sys
sys.path.append('..')
from time import sleep
from data.userinfo import *
from selenium.webdriver.support.ui import WebDriverWait
from src.common.xpth import Xpth

class ScenePage(Xpth):

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    #进入话述配置菜单
    def into_scene(self):
        self.click(e_intoScene)

    #创建场景库
    def create_scene(self,sceneName):
        self.click(e_sceneManage)
        self.click(e_textVersion)
        self.click(e_createScene)

        elements=self.locate_elements(e_scene_Name)
        for element in elements:
            try:
                element.send_keys(sceneName)
            except:
                pass

        self.click(e_businessType)

        elements3 =self.locate_elements(e_type_financial)
        for element in elements3:
            try:
                element.click()
            except:
                pass

        elements4 =self.locate_elements(e_loans)
        for element in elements4:
            try:
                element.click()
            except:
                pass

        elements2=self.locate_elements(e_ensure)
        for element in elements2:
            try:
                element.click()
            except:
                pass
        #删除场景库
        self.locate_element(e_deleteScene, sceneName)

    #添加问答
    def add_question(self,name1,name2,triggerCondition,flag=False,name3=None):
        self.click(e_addQuestion)
        self.click(e_triggerCondition)
        #选择触发条件
        self.click(triggerCondition)

        if triggerCondition in e_selectOther:
            self.click(e_trigger_answer1_1,'触发问答1')
            self.click(e_job,name3)
            self.click(e_trigger_answer1_2,'触发问答1')
            self.click(e_job,'否定')

        self.send_keys(e_processName,name1)
        self.send_keys(e_wordDetils,name2)
        self.click(e_otherWay)
        self.click(e_syntheticVoice)

        #单轮预设回答：肯定/否定
        if flag:
            self.click(e_sure)
            self.click(e_negate)

        self.click(e_submit)

    #添加结束语
    def add_endWords(self,name1,name2,triggerCondition,name3=None,name4=None,n=0,name5=None):
        self.click(e_endWord)
        self.click(e_triggerCondition)
        # 选择触发条件
        self.click(triggerCondition)

        if triggerCondition in e_selectOther:
            #触发问答1
            self.click(e_trigger_answer1_1,'触发问答1')
            self.click(e_job,name3)
            self.click(e_trigger_answer1_2,'触发问答1')
            self.click(e_job,name4)

            if n==2:
                #触发问答2
                self.click(e_addTriggerAnswer)
                self.click(e_trigger_answer1_1,'触发问答2')
                self.click(e_answer2,name3)
                self.click(e_trigger_answer1_2,'触发问答2')
                self.click(e_answer2,name5)

        self.send_keys(e_endWordName,name1)
        self.send_keys(e_wordDetils,name2)
        self.click(e_otherWay)
        self.click(e_syntheticVoice)
        self.click(e_submit)

    #编辑场景库
    def edit_scene(self,scenename,nameList):
        self.click(e_edit,scenename)
        self.click(e_mainProcess)
        #1开场语
        self.add_question(nameList[0],nameList[1],e_selectNatural)
        #2工作的打算
        self.add_question(nameList[2],nameList[3],e_selectNatural,True)
        #3挽留语1
        self.add_question(nameList[4],nameList[5],e_selectOther,True,nameList[2])
        #4加微信
        self.add_question(nameList[6],nameList[7],e_selectOther,False,nameList[4])
        #5结束语1
        self.add_endWords(nameList[8],nameList[9],e_selectOther,nameList[6],'匹配知识库',2,'其他任意回答')
        #6工作类型询问
        self.add_question(nameList[10],nameList[11],e_selectNatural)
        #7工作地点询问
        self.add_question(nameList[12],nameList[13],e_selectNatural)
        #8安排顾问
        self.add_question(nameList[14],nameList[15],e_selectNatural,True)
        #9加微信(安排顾问-否定)
        self.add_question(nameList[6],nameList[7],e_selectOther,False,nameList[14])
        #10结束语1
        self.add_endWords(nameList[16],nameList[9],e_selectOther,nameList[6],'匹配知识库',2,'其他任意回答')
        #11结束语2
        self.add_endWords(nameList[17],nameList[18],e_selectNatural)

    #删除场景库
    def delete_scene(self,sceneName):
        self.click(e_deleteScene,sceneName)
        self.click(e_endEnsure)
        sleep(2)