# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/15 16:39
# 文件: assertFunction.py
import sys
sys.path.append('..')
from data.userinfo import *

class AssertFunction():

    def isElementExist(self,driver,xpth,name=None):

        try:
            if name:
                driver.find_element_by_xpath(xpth.replace('%var%',name))
            else:
                driver.find_element_by_xpath(xpth)
            return True
        except:
            return False
