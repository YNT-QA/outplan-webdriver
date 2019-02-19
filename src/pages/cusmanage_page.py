# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/19 10:48
# 文件: cusmanage_page.py
import sys
sys.path.append('..')
import time
from selenium.webdriver.common.action_chains import ActionChains
from data.userinfo import *
from src.common.incident import Incident

class cusManage(Incident):

      def __init__(self,driver):
          self.driver=driver
          super().__init__(driver)

      def cus_manage(self):
          self.click(e_phoneNumManage)
          time.sleep(2)

      #添加客户组并导入号码
      def add_group(self,groupName,number):
          self.click(e_updateGroup)
          time.sleep(2)
          self.click(e_addGroup)
          time.sleep(2)
          self.send_keys(e_inputName,groupName)
          time.sleep(2)
          self.click(e_commit)
          time.sleep(2)
          self.click(e_closeCusGroup)
          time.sleep(2)
          ActionChains(self.driver).move_to_element(self.locate_element(e_importNumber)).perform()
          time.sleep(2)
          self.click(e_manuallyAdd)
          time.sleep(2)
          self.click(e_selectExistingGroup)
          time.sleep(2)
          self.click(e_selectGroup)
          time.sleep(2)
          self.click(e_all,'全部')
          time.sleep(2)
          self.click(e_all,'kalamodo')
          time.sleep(2)
          self.click(e_all,groupName)
          time.sleep(2)
          self.send_keys(e_numberText,number)
          time.sleep(2)
          elements = self.locate_elements(e_ensure)
          for element in elements:
              try:
                  element.click()
              except:
                  pass
          time.sleep(2)
          self.click(e_closePrompt)
          time.sleep(2)

      def delete_group(self,groupName):
          self.click(e_updateGroup)
          time.sleep(2)
          self.click(e_deleteGroup,groupName)
          time.sleep(2)
          self.click(e_deleteCommit,groupName)
          time.sleep(2)
          self.click(e_ok)
          time.sleep(2)

