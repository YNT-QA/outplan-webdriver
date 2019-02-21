# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/2/20 11:58
# 文件: accmgcms_page.py
from data.userinfo_cms import *
from src.common.xpth import Xpth
from time import sleep

class AccMgCms(Xpth):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    def into_accmg(self):
        self.click(e_cusmanage_cms)

    def add_account(self,email,phone,companyname,number):
        flag=True
        i=1
        while flag:
            elements = self.locate_elements(e_officialacc_cms)
            for element in elements:
                try:
                    element.click()
                    flag=False
                    break
                except:
                    i+=1
            if i>5:
                flag = False

        self.click(e_corpcus_cms)
        self.click(e_addacc_cms)
        self.send_keys(e_email_cms,email)
        self.send_keys(e_phone_cms,phone)
        self.send_keys(e_companyname_cms,companyname)

        elements_step = self.locate_elements(e_nextstep_cms)
        for element in elements_step:
            try:
                element.click()
                break
            except:
                pass

        #self.driver.find_element_by_class_name('editAccountModal-input').clear()
        #self.driver.find_element_by_class_name('editAccountModal-input').send_keys(number)
        self.click(e_indtype_cms)
        self.click(e_industrys_cms,'金融类')
        self.click(e_industrys_cms,'其他类')

        elements_step2 = self.locate_elements(e_nextstep_cms)
        for element in elements_step2:
            try:
                element.click()
                break
            except:
                pass

        self.click(e_returnlist_cms)

    def delete_account(self):
        self.click(e_radio_cms,cusemail_cms)
        self.click(e_delcusacc)
        elements = self.locate_elements(e_ensure_cms)
        for element in elements:
            try:
                element.click()
                break
            except:
                pass
        sleep(2)
