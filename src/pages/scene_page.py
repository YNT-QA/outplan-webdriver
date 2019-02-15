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

    #编辑场景库
    def edit_scene(self,scenename,name_1,name_2):
        sleep(2)
        self.driver.find_element_by_xpath(e_edit.replace('%var%',scenename)).click()
        sleep(1)
        self.driver.find_element_by_xpath(e_mainProcess).click()
        sleep(1)
        self.driver.find_element_by_xpath(e_addQuestion).click()
        sleep(1)
        self.driver.find_element_by_xpath(e_triggerCondition).click()
        sleep(1)
        self.driver.find_element_by_xpath(e_selectNatural).click()
        sleep(1)
        self.driver.find_element_by_xpath(e_processName).send_keys(name_1)
        self.driver.find_element_by_xpath(e_wordDetils).send_keys(name_2)
        sleep(1)
        self.driver.find_element_by_xpath(e_otherWay).click()
        sleep(1)
        self.driver.find_element_by_xpath(e_syntheticVoice).click()
        sleep(3)
        self.driver.find_element_by_xpath(e_sure).click()
        #element=WebDriverWait(self.driver,15).until(lambda x: x.find_element_by_xpath(e_sure))
        sleep(1)
        self.driver.find_element_by_xpath(e_negate).click()
        self.driver.find_element_by_xpath(e_submit).click()
        sleep(2)

    #删除场景库
    def delete_scene(self,sceneName):
        sleep(2)
        self.driver.find_element_by_xpath(e_deleteScene.replace('%var%',sceneName)).click()
        sleep(1)
        self.driver.find_element_by_xpath(e_endEnsure).click()
        sleep(2)