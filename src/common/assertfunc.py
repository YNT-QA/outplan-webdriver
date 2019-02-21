# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/1/15 16:39
# 文件: assertfunc.py
import sys
sys.path.append('..')
from time import sleep

class AssertFunction():

    def isElementExist(self,driver,xpth,name=None):
        flag=True
        i=1
        sleep(2)
        if name:
            while flag:
                try:
                    driver.find_element_by_xpath(xpth.replace('%var%',name))
                    return True
                except:
                    i+=1
                    sleep(1)

                if i>6:
                    return False
        else:
            while flag:
                try:
                    driver.find_element_by_xpath(xpth)
                    return True
                except:
                    i+=1
                    sleep(1)

                if i>6:
                    return False


