# !/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
 # @Date:2018/11/13
from selenium import webdriver
from time import sleep
class dgg:
    def __init__(self):
        pass

    def hhg(self):
        self.ieDriver = webdriver.Ie(executable_path='C:\Program Files\Internet Explorer\IEDriverServer.exe')
        self.ieDriver.maximize_window()
        self.ieDriver.get('http://192.168.102.151:82/hyweb/hyebid/smallScaleProject.do?projId=352')
        sleep(3)
        self.ieDriver.find_element_by_css_selector('div#openHallUrl>a').click()
        self.ieDriver.switch_to_alert().accept()

if __name__ == '__main__':
    t = dgg()
    t.hhg()
