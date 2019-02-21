#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/12/4
from swebid_ztb.login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from swebid_ztb.create_projbase.convert_projbase_to_list import ConvertProjbaseToList
from selenium.webdriver.support.select import Select
from swebid_ztb.add_bidding_registion.convert_info_data_to_list import ConvertInfoDataToList
import re
import logging
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# 编制文件
class TenderAnnouncement:
    def __init__(self):
        pass

    def tender_announcement(self, case):
        self.case = case  # 第几条用例
        for n in range(len(ConvertProjbaseToList.convert_one_info_to_list())):
            # 邵武
            self.driver_login_tuple = Login.login('http://218.67.123.106/swebid/website/index.jsp#', 'zbdl', 'aa000000')
            self.ieDriver = self.driver_login_tuple[0]
            self.login_in = self.driver_login_tuple[1]
            if 'zbdl' in self.login_in:
                # 邵武
                self.ieDriver.get('http://218.67.123.106/swebid/common/skins/outlook/main.jsp')
                self.ieDriver.maximize_window()
                sleep(1)
                for handle in self.ieDriver.window_handles:
                    self.ieDriver.switch_to.window(handle)
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
                        bid_register_proj_code = str(ConvertInfoDataToList.convert_tender_info_to_list()
                                                     [self.case].get_bid_register_proj_code())
                        auditing_status = self.ieDriver.find_element_by_css_selector(
                            'form[name="listForm"] table.EOS_table tr:nth-child(%s)>'
                            'td:nth-child(5)' % (i + 4)).text  # 审核状态
                        # 如果是用例项目并且招标登记已审核通过
                        if bid_register_proj_code in project_industrial_code and auditing_status in '审核确认':
                            create_element = self.ieDriver.find_elements_by_css_selector(
                                'form[name="listForm"] table.EOS_table tr:nth-child(%s)>'
                                'td:nth-child(6)>input:nth-child(2)' % (i + 4))  # 招标建档
                            create_element[0].click()  # 点击招标建档
                            projtype_element = self.ieDriver.find_elements_by_name('projbase/projtype')
                            self.ieDriver.switch_to.parent_frame()
                            if len(projtype_element) == 0:  # 如果已经招标建档
                                WebDriverWait(self.ieDriver, 500, 0.5).until(
                                    EC.presence_of_element_located((By.TAG_NAME, 'frameset')))
                                # self.ieDriver.switch_to.frame('bodyFrame_all')
                                self.ieDriver.switch_to.frame('bodyFrame')
                                self.ieDriver.switch_to.frame('frmid')
                                self.ieDriver.switch_to.frame('prj_right_work')
                                mouse_ann = self.ieDriver.find_element_by_id('btn_4_id')
                                ActionChains(self.ieDriver).move_to_element(mouse_ann).perform()
                                # 点击招标文件
                                self.ieDriver.find_element_by_css_selector('div#menu1 li:nth-child(1)>a').click()
                                file_element = self.ieDriver.find_elements_by_css_selector(
                                    'form[name="listForm"] table.EOS_table tr')
                                if len(file_element) > 3:  # 如果已经新增过招标文件
                                    file_status = self.ieDriver.find_element_by_css_selector(
                                        'form[name="listForm"] table.EOS_table tr:nth-child(4)>td:nth-child(5)').text
                                    if file_status == '未发布':
                                        # 点击文件
                                        self.ieDriver.find_element_by_css_selector(
                                            'form[name="listForm"] table.EOS_table tr:nth-child(4) a').click()
                                        # 点击编制招标文件
                                        is_ebid = ConvertInfoDataToList.convert_confirm_info_to_list()[
                                            self.case].get_is_ebid()
                                        if is_ebid == '电子标':
                                            self.ieDriver.find_element_by_css_selector('input[value="编制招标文件"]').click()
                                            sleep(12)
                                            # self.ieDriver.switch_to_active_element()
                                            print(self.ieDriver.title)
                                            ActionChains(self.ieDriver).send_keys(Keys.TAB).perform()
                                            ActionChains(self.ieDriver).send_keys(Keys.TAB).perform()
                                            ActionChains(self.ieDriver).send_keys(Keys.TAB).perform()
                                            ActionChains(self.ieDriver).send_keys(Keys.TAB).perform()
                                            print('kk')

                                        # self.ieDriver.find_element_by_css_selector(
                                        #     'form[name="listForm"] table.EOS_table '
                                        #     'tr:nth-child(3)>td:nth-child(6)>input').click()  # 点击发布申请单
                                        # self.ieDriver.find_element_by_css_selector(
                                        #     '.mid_table_btn input[name="生成申请单"]').click()  # 点击生成申请单
                                else:  # 如果还没新增过招标文件
                                    # 点击新增
                                    self.ieDriver.find_element_by_css_selector('input[value="新增"]').click()
                                    # 点击编制招标文件
                                    is_ebid = ConvertInfoDataToList.convert_confirm_info_to_list()[self.case].get_is_ebid()
                                    if is_ebid == '电子标':
                                        self.ieDriver.find_element_by_css_selector('input[value="编制招标文件"]').click()
                            else:  # 如果还未招标建档
                                # self.ieDriver.switch_to.parent_frame()
                                self.ieDriver.switch_to.frame('leftFrame')
                                self.ieDriver.find_element_by_link_text('招标登记').click()
                                self.ieDriver.switch_to.parent_frame()  # 跳出leftframe到bodyFrame_all
                                self.ieDriver.switch_to.frame('bodyframe')
                                sleep(2)
                                continue
                        else:  # 如果不是用例项目或者招标登记未审核通过
                            continue


if __name__ == '__main__':
    ta = TenderAnnouncement()
    ta.tender_announcement(0)



