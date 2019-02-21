#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/11/6
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from swebid_ztb.add_bidding_registion.convert_info_data_to_list import ConvertInfoDataToList
from swebid_ztb.login import Login
import logging
import os
import datetime


class TenderInformation:

    def __init__(self):
        pass

    # def setUP(self):
        # self.ieDriver = webdriver.Ie(executable_path='C:\Program Files\Internet Explorer\IEDriverServer.exe')
        # self.ieDriver.maximize_window()

    # def tearDown(self):
    #     self.ieDriver.quit()
    #     # self.ieDriver.close()

    def tender_information(self):
        for n in range(len(ConvertInfoDataToList.convert_tender_info_to_list())):
            # 邵武
            self.driver_login_tuple = Login.login('http://218.67.123.106/swebid/website/index.jsp#', 'zbdl', 'aa000000')
            # self.driver_login_tuple = Login.login('http://www.zpggzyjyzx.gov.cn/hyebid/website/index.jsp', 'zbdl',
            #                                       'aa000000')
            self.ieDriver = self.driver_login_tuple[0]
            self.login_in = self.driver_login_tuple[1]
            if 'zbdl' in self.login_in:
                # if self.ieDriver.find_element_by_id('userid').get_attribute('value') == '':
                #     self.ieDriver.find_element_by_id('userid').send_keys('zbdl')
                #     self.ieDriver.find_element_by_id('password').clear()
                #     self.ieDriver.find_element_by_id('password').send_keys('aa000000')
                #     self.check_code = self.ieDriver.find_element_by_id('code').get_attribute('value')
                #     self.ieDriver.find_element_by_id('verifyCode').send_keys(self.check_code)
                #     self.ieDriver.find_element_by_xpath('//input[@value="登录"]').click()
                #     WebDriverWait(self.ieDriver, 500, 0.5).until(
                #         EC.presence_of_element_located((By.LINK_TEXT, '进入交易平台'))
                #     )
                #     self.login_in = self.ieDriver.find_element_by_css_selector('span.right').text
                # self.ieDriver.find_element_by_link_text('进入交易平台').click()
                # self.ieDriver.switch_to_default_content()
                for handle in self.ieDriver.window_handles:
                    self.ieDriver.switch_to.window(handle)
                    # 邵武
                    self.ieDriver.get('http://218.67.123.106/swebid/common/skins/outlook/main.jsp')
                    self.ieDriver.maximize_window()
                    sleep(1)
                    # for handle1 in self.ieDriver.window_handles:
                    #     self.ieDriver.switch_to_window(handle1)
                    # self.ieDriver.execute_script(
                    #     'window.open("http://218.67.123.106/swebid/common/skins/outlook/main.jsp")')
                    # self.ieDriver.switch_to_window(self.ieDriver.window_handles[1])
                    # url = self.ieDriver.current_url
                    # handles = self.ieDriver.current_window_handle
                    # print(url)
                    # print(handles)
                    WebDriverWait(self.ieDriver, 500, 0.5).until(
                        EC.presence_of_element_located((By.TAG_NAME, 'frameset')))
                    # frame_top = self.ieDriver.find_element_by_id('topFrame ')
                    # self.ieDriver.switch_to_frame(frame_top)
                    # self.ieDriver.switch_to_frame('topFrame')
                    # frameset1 = self.ieDriver.find_element_by_tag_name('frameset')
                    # self.ieDriver.switch_to_frame(frameset1)
                    # 点击建设工程
                    self.ieDriver.switch_to.frame('topFrame')
                    self.ieDriver.find_element_by_css_selector('div#header li:nth-child(2)>a').click()
                    self.ieDriver.switch_to.default_content()
                    # 点击招标登记
                    self.ieDriver.switch_to.frame('bodyFrame_all')
                    self.ieDriver.switch_to.frame('leftFrame')
                    self.ieDriver.find_element_by_link_text('招标登记').click()
                    self.ieDriver.switch_to.parent_frame()  # 跳出leftframe到bodyFrame_all
                    WebDriverWait(self.ieDriver, 500, 0.5).until(
                        EC.presence_of_element_located((By.ID, 'oa_frame')))
                    # 点击新增
                    self.ieDriver.switch_to.frame('bodyFrame')
                    self.ieDriver.find_element_by_xpath('//input[@value="新增"]').click()
                    # 是否依法招标
                    iframe_lable = self.ieDriver.find_element_by_class_name('eos-popwin-body-iframe')
                    self.ieDriver.switch_to.frame(iframe_lable)  # 进入eos-popwin-body-iframe
                    if ConvertInfoDataToList.convert_tender_info_to_list()[n].get_is_law_bid() == "是":
                        self.ieDriver.find_elements_by_name('isLawBid')[0].click()
                    elif ConvertInfoDataToList.convert_tender_info_to_list()[n].get_is_law_bid() == "否":
                        self.ieDriver.find_elements_by_name('isLawBid')[1].click()
                    else:
                        raise Exception('非法输入值')
                    # 项目报建编号
                    self.ieDriver.find_element_by_name('bidRegister/reportno').clear()
                    self.ieDriver.find_element_by_name('bidRegister/reportno').send_keys(
                        ConvertInfoDataToList.convert_tender_info_to_list()[n].get_bid_register_report_no()
                    )
                    # 招标项目编号
                    self.ieDriver.find_element_by_name('bidRegister/projcode').clear()
                    now_time = str(datetime.datetime.now())
                    project_industrial_code = \
                        now_time + str(ConvertInfoDataToList.convert_tender_info_to_list()[n].get_bid_register_proj_code())
                    self.ieDriver.find_element_by_name('bidRegister/projcode').send_keys(project_industrial_code)
                    print(now_time)
                    # 招标项目名称
                    self.ieDriver.find_element_by_name('bidRegister/projname').clear()
                    self.ieDriver.find_element_by_name('bidRegister/projname').send_keys(
                        now_time + ConvertInfoDataToList.convert_tender_info_to_list()[n].get_bid_register_proj_name()
                    )

                    # self.ieDriver.find_element_by_id('projectname').send_keys(
                    #     now_time + ConvertInfoDataToList.convert_project_info_to_list()[n].get_project_name()
                    # )

                    # 招标人名称
                    self.ieDriver.find_element_by_name('bidRegister/ownername').clear()
                    self.ieDriver.find_element_by_name('bidRegister/ownername').send_keys(
                        ConvertInfoDataToList.convert_tender_info_to_list()[n].get_bid_register_owner_name()
                    )
                    # 联系手机
                    self.ieDriver.find_element_by_name('bidRegister/linktel').clear()
                    self.ieDriver.find_element_by_name('bidRegister/linktel').send_keys(
                        ConvertInfoDataToList.convert_tender_info_to_list()[n].get_bid_register_linktel()
                    )
                    # # 项目信息
                    # 公共资源交易分类
                    s_project_type = self.ieDriver.find_element_by_id('projectType')
                    if ConvertInfoDataToList.convert_project_info_to_list()[n].get_project_type() == "房屋建筑":
                        Select(s_project_type).select_by_value('G01')
                    elif ConvertInfoDataToList.convert_project_info_to_list()[n].get_project_type() == "市政":
                        Select(s_project_type).select_by_value('G02')
                    elif ConvertInfoDataToList.convert_project_info_to_list()[n].get_project_type() == "公路":
                        Select(s_project_type).select_by_value('G03')
                    elif ConvertInfoDataToList.convert_project_info_to_list()[n].get_project_type() == "水运":
                        Select(s_project_type).select_by_value('G06')
                    elif ConvertInfoDataToList.convert_project_info_to_list()[n].get_project_type() == "水利电力":
                        Select(s_project_type).select_by_value('G07')
                    elif ConvertInfoDataToList.convert_project_info_to_list()[n].get_project_type() == "能源电力":
                        Select(s_project_type).select_by_value('G08')
                    elif ConvertInfoDataToList.convert_project_info_to_list()[n].get_project_type() == "广电通信":
                        Select(s_project_type).select_by_value('G09')
                    elif ConvertInfoDataToList.convert_project_info_to_list()[n].get_project_type() == "其他":
                        Select(s_project_type).select_by_value('G99')
                    elif ConvertInfoDataToList.convert_project_info_to_list()[n].get_project_type() == "其他（住建）":
                        Select(s_project_type).select_by_value('G99-0')
                    elif ConvertInfoDataToList.convert_project_info_to_list()[n].get_project_type() == "其他（交通）":
                        Select(s_project_type).select_by_value('G99-1')
                    else:
                        raise Exception('非法输入')
                    # 项目名称
                    self.ieDriver.find_element_by_id('projectname').send_keys(
                        now_time + ConvertInfoDataToList.convert_project_info_to_list()[n].get_project_name()
                    )
                    # 项目行业分类代码
                    # self.ieDriver.find_element_by_xpath(
                    #     '//input[@name="project/industrialcode"]/following-sibling::input[1]').click()
                    # s_project_industrial_code1 = self.ieDriver.find_element_by_name('select1')
                    # Select(s_project_industrial_code1).select_by_index(0)  # 门类
                    # s_project_industrial_code2 = self.ieDriver.find_element_by_name('select2')
                    # Select(s_project_industrial_code2).select_by_index(0)  # 大类
                    # self.ieDriver.find_element_by_css_selector(
                    #     'form[name="form1"]>div>input[value="确 定"]').click()  # 确定
                    self.ieDriver.find_element_by_xpath(
                             '//input[@name="project/industrialcode"]').send_keys('I64')
                    # 项目地址
                    self.ieDriver.find_element_by_name('project/projaddr').send_keys(
                        ConvertInfoDataToList.convert_project_info_to_list()[n].get_project_addr()
                    )
                    # 资金来源
                    self.ieDriver.find_element_by_name('project/fundsource').send_keys(
                        ConvertInfoDataToList.convert_project_info_to_list()[n].get_project_fund_source()
                    )
                    # 批复文件/附件
                    self.ieDriver.find_element_by_xpath('//input[@value="上传文件"]').click()
                    # 文件类型
                    self.ieDriver.switch_to.parent_frame()  # 跳出eos-popwin-body-iframe到bodyFrame_all
                    # 进入所在eos-popwin-body-iframe
                    self.ieDriver.switch_to.frame(self.ieDriver.find_elements_by_tag_name('iframe')[1])
                    s_attach_file = self.ieDriver.find_element_by_name('attachfile/filetype')
                    Select(s_attach_file).select_by_index(1)
                    self.ieDriver.find_elements_by_css_selector('span#filediv>input')[2].click()  # 浏览
                    sleep(3)
                    os.system('上传文件.exe')
                    # self.ieDriver.switch_to.active_element  # 模态窗口
                    # WebDriverWait(self.ieDriver, 100, 0.5).until(EC.alert_is_present())
                    self.ieDriver.switch_to_alert()
                    WebDriverWait(self.ieDriver, 500, 0.5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[value="保存"]')))
                    # self.ieDriver.find_element_by_xpath(
                    #     '//div[@class="file-box"]../../following-sibling::tr/td/input[1]').click()
                    self.ieDriver.find_element_by_css_selector('input[value="保存"]').click()  # 保存
                    sleep(5)
                    # 提交
                    # self.ieDriver.switch_to.parent_frame()   # 跳出frame到bodyFrame_all
                    self.ieDriver.switch_to.default_content()
                    self.ieDriver.switch_to.frame('bodyFrame_all')
                    self.ieDriver.switch_to.frame('bodyFrame')
                    iframe_lable = self.ieDriver.find_element_by_class_name('eos-popwin-body-iframe')
                    self.ieDriver.switch_to.frame(iframe_lable)  # 进入eos-popwin-body-iframe
                    self.ieDriver.find_element_by_css_selector('td>input[value="提交"]').click()
                    self.ieDriver.switch_to.parent_frame()
                    self.ieDriver.switch_to.parent_frame()
                    logging.info('%s该项目招标登记已提交审核' % project_industrial_code)
                    print('%s该项目已提交招标登记' % project_industrial_code)
            else:
                raise Exception('登录失败')
                pass


if __name__ == '__main__':
    ti = TenderInformation()
    # ti.setUP()
    ti.tender_information()
