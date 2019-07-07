# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/19 10:48
# 文件: cusmanage_page.py
import sys
sys.path.append('..')
import time
from data.userinfo import *
from src.common.xpath import Xpath

class cusManage(Xpath):

      def __init__(self,driver):
          self.driver=driver
          super().__init__(driver)

      def cus_manage(self):
          self.click(e_phoneNumManage)

      #添加客户组并导入号码
      def add_group(self,groupName,number):
          self.click(e_updateGroup)
          self.click(e_addGroup)
          self.send_keys(e_inputName,groupName)
          self.click(e_commit)
          self.click(e_closeCusGroup)
          self.click(e_importNumber)
          self.click(e_manuallyAdd)
          self.click(e_selectExistingGroup)
          self.click(e_selectGroup)
          self.click(e_all,'全部')
          self.click(e_all,'kalamodo')
          self.click(e_all,groupName)
          self.send_keys(e_numberText,number)

          elements = self.locate_elements(e_ensure)
          for element in elements:
              try:
                  element.click()
              except:
                  pass
          self.click(e_closePrompt)

      def delete_group(self,groupName):
          self.click(e_updateGroup)
          self.click(e_deleteGroup,groupName)
          self.click(e_deleteCommit,groupName)
          self.click(e_ok)
          time.sleep(2)

