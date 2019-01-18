# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/19 10:48
# 文件: cusmanage.py
import sys
sys.path.append('..')
from common.get_value import GetValue
import time
from selenium.webdriver.common.action_chains import ActionChains

class cusManage():

      def __init__(self,driver):
          self.driver=driver
          self.data = GetValue()

      def cus_manage(self):
          self.driver.find_element_by_xpath(self.data.getvalue('e_phoneNumManage')).click()
          time.sleep(2)

      #添加客户组并导入号码
      def add_group(self,groupName,number):
          self.driver.find_element_by_xpath(self.data.getvalue('e_updateGroup')).click()
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_addGroup')).click()
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_inputName')).send_keys(groupName)
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_commit')).click()
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_closeCusGroup')).click()
          time.sleep(2)
          ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.data.getvalue('e_importNumber'))).perform()
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_manuallyAdd')).click()
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_selectExistingGroup')).click()
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_selectGroup')).click()
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_all').replace('%var%','全部')).click()
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_all').replace('%var%','kalamodo')).click()
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_all').replace('%var%',groupName)).click()
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_numberText')).send_keys(number)
          time.sleep(2)
          elements = self.driver.find_elements_by_xpath(self.data.getvalue('e_ensure'))
          for element in elements:
              try:
                  element.click()
              except:
                  pass
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_closePrompt')).click()
          time.sleep(2)

      def delete_group(self,groupName):
          self.driver.find_element_by_xpath(self.data.getvalue('e_updateGroup')).click()
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_deleteGroup').replace('%var%',groupName)).click()
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_deleteCommit').replace('%var%',groupName)).click()
          time.sleep(2)
          self.driver.find_element_by_xpath(self.data.getvalue('e_ok')).click()
          time.sleep(2)
