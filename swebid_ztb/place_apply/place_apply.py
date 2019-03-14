#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/11/16
from swebid_ztb.login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from swebid_ztb.add_bidding_registion.convert_info_data_to_list import ConvertInfoDataToList
import logging
from swebid_ztb.conf_login import *


class PLACE_APPLY:
    def __init__(self):
        pass

    def place_apply(self, c):
        self.c = c
        self.url = conf_login()[0]  # 获取conf_login返回的url
        self.user = conf_login()[1]  # 获取conf_login返回的user
        self.password = conf_login()[2]  # 获取conf_login返回的password
        # 邵武
        self.driver_login_tuple = Login.login(self.url, self.user, self.password)  # 登录
        self.ieDriver = self.driver_login_tuple[0]
        self.login_in = self.driver_login_tuple[1]
        if 'zbdl' in self.login_in:
            for handle in self.ieDriver.window_handles:
                self.ieDriver.switch_to.window(handle)
                # 邵武
                self.ieDriver.get('http://218.67.123.106/swebid/common/skins/outlook/main.jsp')
                self.ieDriver.maximize_window()
                sleep(1)
                WebDriverWait(self.ieDriver, 500, 0.5).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'frameset')))
                self.ieDriver.switch_to.frame('topFrame')
                # 点击建设工程
                self.ieDriver.find_element_by_css_selector('div#header li:nth-child(2)>a').click()
                self.ieDriver.switch_to.default_content()
                # 点击招标登记
                self.ieDriver.switch_to.frame('bodyFrame_all')
                self.ieDriver.switch_to.frame('leftFrame')
                self.ieDriver.find_element_by_link_text('招标登记').click()
                self.ieDriver.switch_to.parent_frame()  # 跳出leftframe到bodyFrame_all
                self.ieDriver.switch_to.frame('bodyframe')
                # 查找自动化项目
                total_project = self.ieDriver.find_elements_by_css_selector(
                    'form[name="listForm"] table.EOS_table tr')  # 全部项目
                for i in range(len(total_project) - 3):  # <TR sizcache="6" nodeIndex="1">
                    project_industrial_code = self.ieDriver.find_element_by_css_selector(
                        'form[name="listForm"] table.EOS_table tr:nth-child(%s)>td:nth-child(1)' % (i + 4)).text
                    code = str(ConvertInfoDataToList.convert_tender_info_to_list()[self.c].get_bid_register_proj_code())
                    place_element = self.ieDriver.find_elements_by_css_selector(
                            'form[name="listForm"] table.EOS_table tr:nth-child(%s)>'
                            'td:nth-child(6)>input:nth-child(1)' % (i + 4))
                    auditing_status = self.ieDriver.find_element_by_css_selector(
                        'form[name="listForm"] table.EOS_table tr:nth-child(%s)>'
                        'td:nth-child(5)' % (i + 4)).text  # 审核状态
                    if code in project_industrial_code and auditing_status in '审核确认':
                        # 点击场地预约
                        # self.ieDriver.find_element_by_css_selector('input[value="场地预约"]').click()
                        place_element[0].click()
                        # 输入开始时间设定18:00
                        iframe1 = self.ieDriver.find_element_by_class_name('eos-popwin-body-iframe')
                        self.ieDriver.switch_to.frame(iframe1)
                        self.ieDriver.find_element_by_id('booktime_input').clear()
                        mouse_time = self.ieDriver.find_element_by_id('booktime_button')
                        ActionChains(self.ieDriver).move_to_element(mouse_time).perform()
                        self.ieDriver.find_element_by_id('booktime_button').send_keys(Keys.ENTER)
                        self.ieDriver.find_element_by_id('booktime_input').send_keys('18:00')
                        self.ieDriver.find_element_by_id('booktime_input').send_keys(Keys.ENTER)
                        sleep(2)
                        # 输入预约时段设定'晚上'
                        self.ieDriver.find_element_by_id('booklen_input').clear()
                        mouse_len = self.ieDriver.find_element_by_id('booklen_button')
                        ActionChains(self.ieDriver).move_to_element(mouse_len).perform()
                        self.ieDriver.find_element_by_id('booklen_button').send_keys(Keys.ENTER)

                        self.ieDriver.find_element_by_id('booklen_input').send_keys('晚上')
                        self.ieDriver.find_element_by_id('booklen_input').send_keys(Keys.ENTER)
                        # self.ieDriver.find_elements_by_xpath('//table[@class="eos-combo-optiontable"]')[
                        #     # 1].find_element_by_xpath('//nobr[contains(text(),"晚上")]').click()
                        # 选择开标室
                        # self.ieDriver.find_elements_by_name('cdxz')[0].click()
                        self.ieDriver.find_elements_by_xpath(
                            '//span[@id="cd"]/span[contains(@id,"cd")][contains(text(),"开标")]/input[1]')[0].click()
                        # 选择评标室
                        # self.ieDriver.find_elements_by_name('cdxz')[1].click()
                        self.ieDriver.find_elements_by_xpath(
                            '//span[@id="cd"]/span[contains(@id,"cd")][contains(text(),"评标")]/input[1]')[0].click()
                        self.ieDriver.find_element_by_name('bookdatil/linkman').send_keys('测试')
                        self.ieDriver.find_element_by_name('bookdatil/mobile').send_keys('11111111111')
                        self.ieDriver.find_element_by_css_selector('input[value="保存并提交申请"]').click()
                        print('%s该项目已提交场地预约' % project_industrial_code)
                        break  # 如果找到当前用例的待审核记录就审核之后终止循环
                    else:
                        continue  # 如果没有找到当前用例的待审核记录就继续执行下次循环直到找到
                    logging.info('没有待场地预约的项目')
                    print('没有待场地预约的项目')

if __name__ == '__main__':
    p = PLACE_APPLY()
    p.place_apply(0)

