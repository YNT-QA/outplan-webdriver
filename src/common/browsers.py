# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/2/13 9:32
# 文件: browsers.py
import os
from data.userinfo import *

class Browsers():

    def __init__(self,browserType):
        self.browserType=browserType

    def select_browser(self):

        if self.browserType=='Chrome':
            browser = os.path.dirname(os.path.abspath('..')) + '\\' + Driver
            return browser
        elif self.browserType=='IE':
            pass
        elif self.browserType=='FireFox':
            pass