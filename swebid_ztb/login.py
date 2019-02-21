#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/11/16
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Login:
    # ieDriver = webdriver.Ie(executable_path='C:\Program Files\Internet Explorer\IEDriverServer.exe')
    ieDriver = ''

    def __init__(self):
        pass
        # self.verifyCode = verifyCode

    @staticmethod
    def login(path, username, password):
        global ieDriver
        ieDriver = webdriver.Ie(executable_path='C:\Program Files\Internet Explorer\IEDriverServer.exe')
        # self.path = path
        # self.username = username
        # self.password = password
        ieDriver.get(path)
        ieDriver.maximize_window()
        for handle in ieDriver.window_handles:
            ieDriver.switch_to.window(handle)
            if ieDriver.find_element_by_id('userid').get_attribute('value') == '':
                ieDriver.find_element_by_id('userid').send_keys(username)
                ieDriver.find_element_by_id('password').clear()
                ieDriver.find_element_by_id('password').send_keys(password)
                check_code = ieDriver.find_element_by_id('code').get_attribute('value')
                ieDriver.find_element_by_id('verifyCode').send_keys(check_code)
                ieDriver.find_element_by_xpath('//input[@value="登录"]').click()
                WebDriverWait(ieDriver, 500, 0.5).until(
                    EC.presence_of_element_located((By.LINK_TEXT, '进入交易平台'))
                )
                login_in = ieDriver.find_element_by_css_selector('span.right').text
                return ieDriver, login_in
            else:
                print('请先退出登录')

# if __name__ == '__main__':
#     r = Login()
#     r.login('http://218.67.123.106/swebid/website/index.jsp#', 'zbdl', 'aa000000')

