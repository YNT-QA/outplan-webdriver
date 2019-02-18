# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/29 14:50
# 文件: scene_page.py
import sys
sys.path.append('..')
from time import sleep
from data.userinfo import *
from selenium.webdriver.support.ui import WebDriverWait

class ScenePage():

    def __init__(self,driver):
        self.driver = driver

    #进入话述配置菜单
    def into_scene(self):
        self.driver.find_element_by_xpath(e_intoScene).click()
        sleep(2)

    #创建场景库
    def create_scene(self,sceneName):
        self.driver.find_element_by_xpath(e_sceneManage).click()
        sleep(1)
        self.driver.find_element_by_xpath(e_textVersion).click()
        sleep(1)
        self.driver.find_element_by_xpath(e_createScene).click()
        sleep(1)

        elements=self.driver.find_elements_by_xpath(e_scene_Name)
        for element in elements:
            try:
                element.send_keys(sceneName)
            except:
                pass
        sleep(1)

        self.driver.find_element_by_xpath(e_businessType).click()
        sleep(2)

        elements3 =self.driver.find_elements_by_xpath(e_type_financial)
        for element in elements3:
            try:
                element.click()
            except:
                pass
        sleep(2)

        elements4 =self.driver.find_elements_by_xpath(e_loans)
        for element in elements4:
            try:
                element.click()
            except:
                pass
        sleep(1)

        elements2=self.driver.find_elements_by_xpath(e_ensure)
        for element in elements2:
            try:
                element.click()
            except:
                pass

        flag=True
        while flag:
            try:
                self.driver.find_element_by_xpath(e_deleteScene.replace('%var%',sceneName))
                flag=False
            except:
                pass
    #添加问答
    def add_question(self,name1,name2,triggerCondition,flag=False,name3=None):
        sleep(1)
        self.driver.find_element_by_xpath(e_addQuestion).click()
        sleep(1)
        self.driver.find_element_by_xpath(e_triggerCondition).click()
        sleep(1)
        #选择触发条件
        self.driver.find_element_by_xpath(triggerCondition).click()
        sleep(1)
        if triggerCondition in e_selectOther:
            self.driver.find_element_by_xpath(e_trigger_answer1_1.replace('%var%','触发问答1')).click()
            sleep(1)
            self.driver.find_element_by_xpath(e_job.replace('%var%',name3)).click()
            sleep(1)
            self.driver.find_element_by_xpath(e_trigger_answer1_2.replace('%var%','触发问答1')).click()
            sleep(1)
            self.driver.find_element_by_xpath(e_job.replace('%var%','否定')).click()

        self.driver.find_element_by_xpath(e_processName).send_keys(name1)
        self.driver.find_element_by_xpath(e_wordDetils).send_keys(name2)
        sleep(1)
        self.driver.find_element_by_xpath(e_otherWay).click()
        sleep(1)
        self.driver.find_element_by_xpath(e_syntheticVoice).click()
        sleep(1)
        if flag:
            try:
                element = WebDriverWait(self.driver,15).until(lambda x: x.find_element_by_xpath(e_sure))
                sleep(2)
                self.driver.find_element_by_xpath(e_sure).click()
            except:
                print("定位失败：%s"%element)
            sleep(1)
            self.driver.find_element_by_xpath(e_negate).click()
        sleep(3)
        self.driver.find_element_by_xpath(e_submit).click()
        sleep(2)

    #添加结束语
    def add_endWords(self,name1,name2,triggerCondition,name3=None,name4=None,n=0,name5=None):
        self.driver.find_element_by_xpath(e_endWord).click()
        sleep(1)
        self.driver.find_element_by_xpath(e_triggerCondition).click()
        sleep(1)
        # 选择触发条件
        self.driver.find_element_by_xpath(triggerCondition).click()
        sleep(1)
        if triggerCondition in e_selectOther:
            #触发问答1
            self.driver.find_element_by_xpath(e_trigger_answer1_1.replace('%var%','触发问答1')).click()
            sleep(1)
            self.driver.find_element_by_xpath(e_job.replace('%var%',name3)).click()
            sleep(1)
            self.driver.find_element_by_xpath(e_trigger_answer1_2.replace('%var%','触发问答1')).click()
            sleep(1)
            self.driver.find_element_by_xpath(e_job.replace('%var%',name4)).click()

            if n==2:
                #触发问答2
                self.driver.find_element_by_xpath(e_addTriggerAnswer).click()
                sleep(1)
                self.driver.find_element_by_xpath(e_trigger_answer1_1.replace('%var%','触发问答2')).click()
                sleep(1)
                self.driver.find_element_by_xpath(e_answer2.replace('%var%',name3)).click()
                sleep(1)
                self.driver.find_element_by_xpath(e_trigger_answer1_2.replace('%var%','触发问答2')).click()
                sleep(1)
                self.driver.find_element_by_xpath(e_answer2.replace('%var%',name5)).click()


        self.driver.find_element_by_xpath(e_endWordName).send_keys(name1)
        self.driver.find_element_by_xpath(e_wordDetils).send_keys(name2)
        sleep(1)
        self.driver.find_element_by_xpath(e_otherWay).click()
        sleep(1)
        self.driver.find_element_by_xpath(e_syntheticVoice).click()
        sleep(3)
        self.driver.find_element_by_xpath(e_submit).click()
        sleep(2)

    #编辑场景库
    def edit_scene(self,scenename,nameList):
        sleep(2)
        self.driver.find_element_by_xpath(e_edit.replace('%var%',scenename)).click()
        sleep(1)
        self.driver.find_element_by_xpath(e_mainProcess).click()
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
        self.driver.find_element_by_xpath(e_deleteScene.replace('%var%',sceneName)).click()
        sleep(1)
        self.driver.find_element_by_xpath(e_endEnsure).click()
        sleep(2)