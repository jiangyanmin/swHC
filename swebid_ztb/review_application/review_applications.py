#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/11/8
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from swebid_ztb.add_bidding_registion.convert_info_data_to_list import ConvertInfoDataToList
from time import sleep
import logging
from swebid_ztb.login import Login


class ReviewApplications:
    def __init__(self):
        pass

    # def setUp(self):
    #     self.ieDriver = webdriver.Ie(executable_path='C:\Program Files\Internet Explorer\IEDriverServer.exe')
    #     self.ieDriver.maximize_window()
    #
    # def tearDown(self):
    #     self.ieDriver.quit()
    #     # self.ieDriver.close()

    def bidding_register_review(self, n):
        self.n = n  # 定义第几条用例
        # 邵武
        # 邵武
        self.driver_login_tuple = Login.login('http://218.67.123.106/swebid/website/index.jsp#', 'testlzx', 'aa000000')

        self.ieDriver = self.driver_login_tuple[0]
        self.login_in = self.driver_login_tuple[1]
        if '测试lzx' in self.login_in:
            # self.ieDriver.find_element_by_link_text('进入交易平台').click()
            self.ieDriver.get('http://218.67.123.106/swebid/common/skins/outlook/main.jsp')
            self.ieDriver.maximize_window()
            sleep(1)
            WebDriverWait(self.ieDriver, 500, 0.5).until(
                EC.presence_of_element_located((By.TAG_NAME, 'frameset')))
            self.ieDriver.switch_to.frame('topFrame')
            # 点击平台首页
            self.ieDriver.find_element_by_css_selector('li#current>a').click()
            self.ieDriver.switch_to.default_content()
            self.ieDriver.switch_to.frame('bodyFrame_all')
            frame1 = self.ieDriver.find_element_by_css_selector('div#dv>iframe')
            self.ieDriver.switch_to.frame(frame1)
            # 点击招标登记
            self.ieDriver.find_elements_by_css_selector('div.knr2>a')[0].click()
            # 点击审核
            total_pending = self.ieDriver.find_elements_by_css_selector(
                'form[name="listForm"] table.EOS_table tr')  # 全部待审
            for i in range(len(total_pending)-3):  # <TR sizcache="6" nodeIndex="1">
                project_industrial_code = self.ieDriver.find_element_by_css_selector(
                    'form[name="listForm"] table.EOS_table tr:nth-child(%s)>td:nth-child(1)' % (i + 4)).text
                code = str(ConvertInfoDataToList.convert_tender_info_to_list()[self.n].get_bid_register_proj_code())
                if code in project_industrial_code:
                    self.ieDriver.find_element_by_css_selector(
                        'form[name="listForm"] table.EOS_table tr:nth-child(%s) input[value="审核"]' % (i + 4)).click()
                    self.ieDriver.switch_to.parent_frame()
                    iframe2 = self.ieDriver.find_element_by_css_selector(
                        'table.eos-dialog iframe.eos-popwin-body-iframe')
                    self.ieDriver.switch_to.frame(iframe2)
                    # 同意
                    self.ieDriver.find_element_by_id('auditstatus_2').click()
                    # 确定
                    self.ieDriver.find_element_by_xpath('//form[@id="dataform"]/table[5]//input[@value="确定"]').click()
                    sleep(3)
                    self.ieDriver.switch_to_default_content()
                    self.ieDriver.switch_to_default_content()
                    self.ieDriver.switch_to_default_content()
                    logging.info('%s，该项目招标登记已审核通过' % project_industrial_code)
                    print('%s，该项目招标登记已审核通过' % project_industrial_code)
                    break  # 如果找到当前用例的待审核记录就审核之后终止循环
                else:
                    continue  # 如果没有找到当前用例的待审核记录就继续执行下次循环直到找到
            logging.info('没有待审核的招标登记')
            print('没有待审核的招标登记')
        else:
            raise Exception('登录失败')

    def place_apply_review(self, n):
        self.n = n
        self.driver_login_tuple = Login.login('http://218.67.123.106/swebid/website/index.jsp#', 'testlzx', 'aa000000')
        self.ieDriver = self.driver_login_tuple[0]
        self.login_in = self.driver_login_tuple[1]
        if '测试lzx' in self.login_in:
            # self.ieDriver.find_element_by_link_text('进入交易平台').click()
            self.ieDriver.get('http://218.67.123.106/swebid/common/skins/outlook/main.jsp')
            self.ieDriver.maximize_window()
            sleep(1)
            WebDriverWait(self.ieDriver, 500, 0.5).until(
                EC.presence_of_element_located((By.TAG_NAME, 'frameset')))
            self.ieDriver.switch_to.frame('topFrame')
            # 点击平台首页
            self.ieDriver.find_element_by_css_selector('li#current>a').click()
            sleep(2)
            self.ieDriver.switch_to.default_content()
            self.ieDriver.switch_to.frame('bodyFrame_all')
            frame1 = self.ieDriver.find_element_by_css_selector('div#dv>iframe')
            self.ieDriver.switch_to.frame(frame1)
            # 点击场地预约
            self.ieDriver.find_elements_by_css_selector('div.knr2>a')[1].click()
            total_apply = self.ieDriver.find_elements_by_css_selector(
                'form[name="listForm"] table.EOS_table tr')  # 全部待审
            for i in range(len(total_apply)-3):
                project_name = self.ieDriver.find_element_by_css_selector(
                    'form[name="listForm"] table.EOS_table tr:nth-child(%s)>td:nth-child(1)>a' % (i + 3)).text
                name = str(ConvertInfoDataToList.convert_tender_info_to_list()[self.n].get_bid_register_proj_name())
                if name in project_name:
                    # 点击审核
                    self.ieDriver.find_element_by_css_selector(
                        'form[name="listForm"] table.EOS_table tr:nth-child(%s) input[value="审核"]' % (i + 3)).click()
                    # 点击确认
                    self.ieDriver.switch_to.parent_frame()
                    iframe_qr = self.ieDriver.find_element_by_class_name('eos-popwin-body-iframe')
                    self.ieDriver.switch_to.frame(iframe_qr)
                    self.ieDriver.find_elements_by_name('bookdatil/status')[0].click()
                    # 点击审核
                    self.ieDriver.find_element_by_xpath('//tr[@class="form_bottom"]//input[@value="审核"]').click()
                    logging.info('%s该项目场地预约已审核通过' % project_name)
                    print('%s该项目场地预约已审核通过' % project_name)
                    break  # 如果找到当前用例的待审核记录就审核之后终止循环
                else:
                    continue  # 如果没有找到当前用例的待审核记录就继续执行下次循环直到找到
            logging.info('没有待审核的场地预约')
            print('没有待审核的场地预约')

    def tender_confirm(self, n):
        self.n = n  # 定义第几条用例
        self.driver_login_tuple = Login.login('http://218.67.123.106/swebid/website/index.jsp#', 'testlzx', 'aa000000')
        self.ieDriver = self.driver_login_tuple[0]
        self.login_in = self.driver_login_tuple[1]
        if '测试lzx' in self.login_in:
            # self.ieDriver.find_element_by_link_text('进入交易平台').click()
            self.ieDriver.get('http://218.67.123.106/swebid/common/skins/outlook/main.jsp')
            self.ieDriver.maximize_window()
            sleep(1)
            WebDriverWait(self.ieDriver, 500, 0.5).until(
                EC.presence_of_element_located((By.TAG_NAME, 'frameset')))
            self.ieDriver.switch_to.frame('topFrame')
            # 点击平台首页
            self.ieDriver.find_element_by_css_selector('li#current>a').click()
            self.ieDriver.switch_to.default_content()
            self.ieDriver.switch_to.frame('bodyFrame_all')
            frame1 = self.ieDriver.find_element_by_css_selector('div#dv>iframe')
            self.ieDriver.switch_to.frame(frame1)
            # 点击招标选项确认
            self.ieDriver.find_elements_by_css_selector('div.knr2>a')[2].click()
            self.ieDriver.switch_to.frame('myTab')
            total_confirm = self.ieDriver.find_elements_by_css_selector(
                'form[name="listForm"] table.EOS_table tr')  # 全部待审
            for i in range(len(total_confirm) - 2):  # 减去表头和页数
                project_industrial_code = self.ieDriver.find_element_by_css_selector(
                    'form[name="listForm"] table.EOS_table tr:nth-child(%s)>td:nth-child(2)' % (i + 2)).text
                if str(ConvertInfoDataToList.convert_tender_info_to_list()[
                           self.n].get_bid_register_proj_code()) in project_industrial_code:
                    # 点击“办理”
                    self.ieDriver.find_element_by_css_selector(
                        'form[name="listForm"] table.EOS_table tr:nth-child(%s) input[value="办理"]' % (i + 2)).click()
                    is_ebid = ConvertInfoDataToList.convert_confirm_info_to_list()[self.n].get_is_ebid()
                    is_forcebid = ConvertInfoDataToList.convert_confirm_info_to_list()[self.n].get_is_forcebid()
                    self.ieDriver.switch_to.parent_frame()
                    self.ieDriver.switch_to.parent_frame()
                    iframe_confirm = self.ieDriver.find_elements_by_tag_name('iframe')[1]
                    self.ieDriver.switch_to.frame(iframe_confirm)
                    is_ebid_element = self.ieDriver.find_elements_by_css_selector(
                            'table#objTable input[name="HT_IMPLEMENT_PLAN/isebid"]')
                    is_forcebid_element = self.ieDriver.find_element_by_name('projbase/isforcebid')
                    # 本招标项目采用：
                    if is_ebid == '电子标':
                        is_ebid_element[0].click()
                    elif is_ebid == '非电子标':
                        is_ebid_element[1].click()
                    else:
                        raise Exception('非法输入')
                    # 依法必须进行的招标项目确认
                    if is_forcebid == '是':
                        is_forcebid_element.click()
                    # elif is_forcebid == '否':
                    #     pass
                    # else:
                    #     raise Exception('非法输入')
                    self.ieDriver.find_element_by_css_selector('form[name="queryForm"] input[value="确定"]').click()
                    WebDriverWait(self.ieDriver, 100, 0.5).until(EC.alert_is_present())
                    alert_save = self.ieDriver.switch_to_alert()
                    alert_save.accept()
                    logging.info('%s项目已招标选项确认' % project_industrial_code)
                    print('%s该项目已招标选项确认' % project_industrial_code)
                    break  # 如果找到当前用例的待审核记录就审核之后终止循环
                else:
                    continue  # 如果没有找到当前用例的待审核记录就继续执行下次循环直到找到
            logging.info('没有待招标选项确认的项目')
            print('没有待招标选项确认的项目')

if __name__ == '__main__':
    t = ReviewApplications()
    # t.setUp()
    # t.bidding_register_review(0)
    t.place_apply_review(0)
    # t.tender_confirm(0)

