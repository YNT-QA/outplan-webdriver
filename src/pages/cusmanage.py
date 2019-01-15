# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/19 10:48
# 文件: cusmanage.py
import sys
sys.path.append('..')
from common.get_value import GetValue
import time

class cusManage():

      def __init__(self,driver):
          self.driver=driver
          self.data = GetValue()

      def cus_manage(self):
          self.driver.find_element_by_xpath(self.data.getvalue('e_phoneNumManage')).click()


      def add_group(self,groupName):
          self.driver.find_element_by_xpath(self.data.getvalue('e_updateGroup')).click()
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_addGroup')).click()
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_inputName')).send_keys(groupName)
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_commit')).click()

      def delete_group(self,groupName):
          self.driver.find_element_by_xpath(self.data.getvalue('e_deleteGroup').replace('%var%',groupName)).click()
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_deleteCommit').replace('%var%',groupName)).click()
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_ok')).click()
          time.sleep(2)

