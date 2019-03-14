#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/11/21
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
from swebid_ztb.conf_login import *


class CreateProjbase:
    def __init__(self):
        pass

    def create_projbase(self, case):
        self.case = case  # 第几条用例
        self.url = conf_login()[0]  # 获取conf_login返回的url
        self.user = conf_login()[1]  # 获取conf_login返回的user
        self.password = conf_login()[2]  # 获取conf_login返回的password

        for n in range(len(ConvertProjbaseToList.convert_one_info_to_list())):
            # 邵武
            self.driver_login_tuple = Login.login(self.url, self.user, self.password)  # 登录
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
                            # WebDriverWait(self.ieDriver, 100, 0.5).until(EC.alert_is_present())
                            # alert_save3 = self.ieDriver.switch_to_alert()
                            # alert_save3.text
                            # sleep(2)
                            projtype_element = self.ieDriver.find_elements_by_name('projbase/projtype')
                            if len(projtype_element) == 0:  # 如果已经招标建档，退出本次循环执行下次循环
                                self.ieDriver.switch_to.parent_frame()
                                # self.ieDriver.switch_to.frame('bodyFrame_all')
                                self.ieDriver.switch_to.frame('leftFrame')
                                self.ieDriver.find_element_by_link_text('招标登记').click()
                                self.ieDriver.switch_to.parent_frame()  # 跳出leftframe到bodyFrame_all
                                self.ieDriver.switch_to.frame('bodyframe')
                                sleep(2)
                                continue
                            else:
                                # # logging.NOTSET('%s，该项目已建档' % project_industrial_code)
                                # 项目类型
                                projtype = ConvertProjbaseToList.convert_one_info_to_list()[n].get_projtype()
                                if projtype == '工程类':
                                    projtype_element[0].click()
                                elif projtype == '货物类':
                                    projtype_element[1].click()
                                elif projtype == '服务类':
                                    projtype_element('projbase/projtype')[2].click()
                                else:
                                    raise Exception('"项目类型"输入值非法')
                                # 招标方式
                                s1 = self.ieDriver.find_element_by_name('projbase/tradetype')
                                tradetype = ConvertProjbaseToList.convert_one_info_to_list()[n].get_tradetype()
                                if tradetype == '公开招标':
                                    Select(s1).select_by_visible_text('公开招标')
                                elif tradetype == '邀请招标':
                                    Select(s1).select_by_visible_text('邀请招标')
                                else:
                                    raise Exception('"招标方式"输入值非法')
                                # 招标组织形式
                                s2 = self.ieDriver.find_element_by_name('projbase/orgform')
                                orgform = ConvertProjbaseToList.convert_one_info_to_list()[n].get_orgform()
                                if orgform == '自行招标':
                                    Select(s2).select_by_visible_text('自行招标')
                                elif orgform == '委托招标':
                                    Select(s2).select_by_visible_text('委托招标')
                                elif orgform == '其它':
                                    Select(s2).select_by_visible_text('其它')
                                else:
                                    raise Exception('"招标组织形式"输入值非法')
                                # 资格审查方法
                                qualifymethod = ConvertProjbaseToList.convert_one_info_to_list()[n].get_qualifymethod()
                                if qualifymethod == '无':
                                    self.ieDriver.find_elements_by_name('projbase/qualifymethod')[0].click()
                                elif qualifymethod == '资格预审':
                                    self.ieDriver.find_elements_by_name('projbase/qualifymethod')[1].click()
                                elif qualifymethod == '资格后审':
                                    self.ieDriver.find_elements_by_name('projbase/qualifymethod')[2].click()
                                else:
                                    raise Exception('"资格审查方法"输入值非法')
                                # 是否接受联合体投标
                                allowcoalition = ConvertProjbaseToList.convert_one_info_to_list()[
                                    n].get_isallowcoalition()
                                if allowcoalition == '不接受联合体投标':
                                    self.ieDriver.find_elements_by_name('projbase/isallowcoalition')[0].click()
                                elif allowcoalition == '接受联合体投标':
                                    self.ieDriver.find_elements_by_name('projbase/isallowcoalition')[1].click()
                                else:
                                    raise Exception('"是否接受联合体投标"输入值非法')
                                # 招标次数
                                # self.ieDriver.find_element_by_name('projbase/noofbids').clear()
                                s3 = self.ieDriver.find_element_by_name('projbase/noofbids')
                                noofbids = ConvertProjbaseToList.convert_one_info_to_list()[n].get_noofbids()
                                if noofbids == '第一次':
                                    Select(s3).select_by_visible_text('第一次')
                                elif noofbids == '第二次':
                                    Select(s3).select_by_visible_text('第二次')
                                elif noofbids == '第三次':
                                    Select(s3).select_by_visible_text('第三次')
                                elif noofbids == '第四次':
                                    Select(s3).select_by_visible_text('第四次')
                                elif noofbids == '第五次':
                                    Select(s3).select_by_visible_text('第五次')
                                elif noofbids == '第六次':
                                    Select(s3).select_by_visible_text('第六次')
                                elif noofbids == '第七次':
                                    Select(s3).select_by_visible_text('第七次')
                                elif noofbids == '第八次':
                                    Select(s3).select_by_visible_text('第八次')
                                elif noofbids == '第九次':
                                    Select(s3).select_by_visible_text('第九次')
                                else:
                                    raise Exception('"招标次数"输入值非法')
                                # 是否要求基本账户缴交投标保证金
                                bondfrombase = ConvertProjbaseToList.convert_one_info_to_list()[n].get_bondfrombase()
                                if bondfrombase == '限定使用基本账户':
                                    self.ieDriver.find_elements_by_name('projbase/bondfrombase')[0].click()
                                elif bondfrombase == '不限定为基本账户':
                                    self.ieDriver.find_elements_by_name('projbase/bondfrombase')[1].click()
                                else:
                                    raise Exception('"是否要求基本账户缴交投标保证金"输入值非法')
                                # 审核部门名称
                                self.ieDriver.find_element_by_name('projbase/auditdeptname').clear()
                                self.ieDriver.find_element_by_name('projbase/auditdeptname').send_keys('测试')
                                # 监督部门名称
                                self.ieDriver.find_element_by_name('projbase/supervisedepname').clear()
                                self.ieDriver.find_element_by_name('projbase/supervisedepname').send_keys('测试')
                                # 专业/工程类别
                                # self.ieDriver.find_element_by_name('projbase/class[1]/classvalueid').clear()
                                # self.ieDriver.find_element_by_name('projbase/class[2]/classvalueid').clear()
                                s4 = self.ieDriver.find_element_by_name('projbase/class[1]/classvalueid')
                                s5 = self.ieDriver.find_element_by_name('projbase/class[2]/classvalueid')
                                if ConvertProjbaseToList.convert_one_info_to_list()[n].get_projtype() == '工程类':
                                    # 专业类别
                                    prof_category = ConvertProjbaseToList.convert_one_info_to_list()[
                                        n].get_prof_category()
                                    if prof_category == '房建':
                                        Select(s4).select_by_visible_text('房建')
                                    elif prof_category == '市政':
                                        Select(s4).select_by_visible_text('市政')
                                    elif prof_category == '水利':
                                        Select(s4).select_by_visible_text('水利')
                                    elif prof_category == '农业':
                                        Select(s4).select_by_visible_text('农业')
                                    elif prof_category == '公路交通':
                                        Select(s4).select_by_visible_text('公路交通')
                                    elif prof_category == '环境整治':
                                        Select(s4).select_by_visible_text('环境整治')
                                    elif prof_category == '土地整理':
                                        Select(s4).select_by_visible_text('土地整理')
                                    elif prof_category == '物业':
                                        Select(s4).select_by_visible_text('物业')
                                    elif prof_category == '其他':
                                        Select(s4).select_by_visible_text('其他')
                                    else:
                                        raise Exception('"专业类别"输入值非法')
                                    # 工程类别
                                    work_category = ConvertProjbaseToList.convert_one_info_to_list()[
                                        n].get_work_category()
                                    if work_category == '施工':
                                        Select(s5).select_by_visible_text('施工')
                                    elif work_category == '设计':
                                        Select(s5).select_by_visible_text('设计')
                                    elif work_category == '监理':
                                        Select(s5).select_by_visible_text('监理')
                                    elif work_category == '代理':
                                        Select(s5).select_by_visible_text('代理')
                                    elif work_category == '勘察':
                                        Select(s5).select_by_visible_text('勘察')
                                    elif work_category == '造价':
                                        Select(s5).select_by_visible_text('造价')
                                    elif work_category == '其他':
                                        Select(s5).select_by_visible_text('其他')
                                    else:
                                        raise Exception('"工程类别"输入值非法')
                                else:
                                    pass
                                # 标段(包)数量
                                self.ieDriver.find_element_by_name('projbase/bidcount').clear()
                                self.ieDriver.find_element_by_name('projbase/bidcount').send_keys(
                                    ConvertProjbaseToList.convert_one_info_to_list()[n].get_bidcount())
                                # 评标办法
                                # self.ieDriver.find_element_by_name('projbase/bidmid').clear()
                                s6 = self.ieDriver.find_element_by_name('projbase/bidmid')
                                bid_method = ConvertProjbaseToList.convert_one_info_to_list()[n].get_bidmid()
                                if bid_method == '最低价法':
                                    Select(s6).select_by_visible_text('最低价法')
                                elif bid_method == '综合评价法(无技术方案评分)':
                                    Select(s6).select_by_visible_text('综合评价法(无技术方案评分)')
                                elif bid_method == '综合评估法 标准施工[2015]':
                                    Select(s6).select_by_visible_text('综合评估法 标准施工[2015]')
                                elif bid_method == '综合评标法—监理':
                                    Select(s6).select_by_visible_text('综合评标法—监理')
                                elif bid_method == '水利施工[2017] 综合评价法':
                                    Select(s6).select_by_visible_text('水利施工[2017] 综合评价法')
                                elif bid_method == '水利施工[2017] 经评审的最低投标价中标法':
                                    Select(s6).select_by_visible_text('水利施工[2017] 经评审的最低投标价中标法')
                                elif bid_method == '水利勘察设计[2017] 综合评估法':
                                    Select(s6).select_by_visible_text('水利勘察设计[2017] 综合评估法')
                                elif bid_method == '水利勘察设计[2017] 经评审的最低投标价中标法':
                                    Select(s6).select_by_visible_text('水利勘察设计[2017] 经评审的最低投标价中标法')
                                elif bid_method == '水利监理[2017] 综合评分法':
                                    Select(s6).select_by_visible_text('水利监理[2017] 综合评分法')
                                elif bid_method == '水利监理[2017] 经评审的最低投标价中标法':
                                    Select(s6).select_by_visible_text('水利监理[2017] 经评审的最低投标价中标法')
                                elif bid_method == '经评审的最低投标价中标法(不含技术文件) 标准施工[2015]':
                                    Select(s6).select_by_visible_text('经评审的最低投标价中标法(不含技术文件) 标准施工[2015]')
                                elif bid_method == '记名投票法 标准设计[2013]':
                                    Select(s6).select_by_visible_text('记名投票法 标准设计[2013]')
                                elif bid_method == '合理低价法 施工招标':
                                    Select(s6).select_by_visible_text('合理低价法 施工招标')
                                elif bid_method == '(泉州版2018房建市政监理)-综合评估法(删除监理大纲和总监答辩)':
                                    Select(s6).select_by_visible_text('(泉州版2018房建市政监理)-综合评估法(删除监理大纲和总监答辩)')
                                elif bid_method == '(2018福建省市政基础设施工程)标准设计-综合评估法':
                                    Select(s6).select_by_visible_text('(2018福建省市政基础设施工程)标准设计-综合评估法')
                                elif bid_method == '(2018福建省市政基础设施工程)标准设计-记名投票法':
                                    Select(s6).select_by_visible_text('(2018福建省市政基础设施工程)标准设计-记名投票法')
                                elif bid_method == '(2018福建省建筑工程)标准设计-综合评估法':
                                    Select(s6).select_by_visible_text('(2018福建省建筑工程)标准设计-综合评估法')
                                elif bid_method == '(2018福建省建筑工程)标准设计-排序法':
                                    Select(s6).select_by_visible_text('(2018福建省建筑工程)标准设计-排序法')
                                elif bid_method == '(2018福建省建筑工程)标准设计-记名投票法':
                                    Select(s6).select_by_visible_text('(2018福建省建筑工程)标准设计-记名投票法')
                                elif bid_method == '(2018福建省标准工程)勘察-综合评估法':
                                    Select(s6).select_by_visible_text('(2018福建省标准工程)勘察-综合评估法')
                                elif bid_method == '(2018福建省标准工程)勘察-简易评估法':
                                    Select(s6).select_by_visible_text('(2018福建省标准工程)勘察-简易评估法')
                                elif bid_method == '(2018房建市政)标准监理-综合评估法':
                                    Select(s6).select_by_visible_text('(2018房建市政)标准监理-综合评估法')
                                elif bid_method == '(2018房建市政)标准监理-简易评标法':
                                    Select(s6).select_by_visible_text('(2018房建市政)标准监理-简易评标法')
                                elif bid_method == '(2017房建市政)工程施工-综合评估法(B类，有技术标)':
                                    Select(s6).select_by_visible_text('(2017房建市政)工程施工-综合评估法(B类，有技术标)')
                                elif bid_method == '(2017房建市政)工程施工-综合评估法(B类，无技术标)':
                                    Select(s6).select_by_visible_text('(2017房建市政)工程施工-综合评估法(B类，无技术标)')
                                elif bid_method == '(2017房建市政)工程施工-综合评估法(A类，有技术标)':
                                    Select(s6).select_by_visible_text('(2017房建市政)工程施工-综合评估法(A类，有技术标)')
                                elif bid_method == '(2017房建市政)工程施工-综合评估法(A类，无技术标)':
                                    Select(s6).select_by_visible_text('(2017房建市政)工程施工-综合评估法(A类，无技术标)')
                                elif bid_method == '(2017房建市政)工程施工-经评审的最低投标价中标法(B类)':
                                    Select(s6).select_by_visible_text('(2017房建市政)工程施工-经评审的最低投标价中标法(B类)')
                                elif bid_method == '(2017房建市政)工程施工-经评审的最低投标价中标法(A类)':
                                    Select(s6).select_by_visible_text('(2017房建市政)工程施工-经评审的最低投标价中标法(A类)')
                                elif bid_method == '(2017房建市政)工程施工-简易评标法':
                                    Select(s6).select_by_visible_text('(2017房建市政)工程施工-简易评标法')
                                elif bid_method == '(2013建筑工程标准设计) -综合评估法':
                                    Select(s6).select_by_visible_text('(2013建筑工程标准设计) -综合评估法')
                                elif bid_method == '(2013建筑工程标准设计) -排序法':
                                    Select(s6).select_by_visible_text('(2013建筑工程标准设计) -排序法')
                                elif bid_method == '(2013建筑工程标准勘察)-综合评估法':
                                    Select(s6).select_by_visible_text('(2013建筑工程标准勘察)-综合评估法')
                                elif bid_method == '(2013建筑工程标准勘察)-简易评估法':
                                    Select(s6).select_by_visible_text('(2013建筑工程标准勘察)-简易评估法')
                                else:
                                    raise Exception('"评标办法"输入值非法')
                                # 确定
                                self.ieDriver.find_element_by_css_selector('input[value="确定"]').click()
                                self.ieDriver.switch_to.parent_frame()
                                self.ieDriver.switch_to.parent_frame()
                                # # 建档第二步
                                WebDriverWait(self.ieDriver, 500, 0.5).until(
                                    EC.presence_of_element_located((By.TAG_NAME, 'frameset')))
                                # 项目备案编号
                                self.ieDriver.switch_to.frame('bodyFrame_all')
                                self.ieDriver.switch_to.frame('bodyFrame')
                                WebDriverWait(self.ieDriver, 500, 0.5).until(
                                    EC.presence_of_element_located((By.NAME, 'projbase/reviewCode')))
                                self.ieDriver.find_element_by_name('projbase/reviewCode').clear()
                                self.ieDriver.find_element_by_name('projbase/reviewCode').send_keys(r'/')
                                # 招标人选择按钮
                                self.ieDriver.find_element_by_xpath('//td[contains(text(),"招标人")]/input').click()
                                iframe1 = self.ieDriver.find_elements_by_tag_name('iframe')[0]
                                self.ieDriver.switch_to.frame(iframe1)
                                self.ieDriver.find_element_by_id('group1_1_checkbox').click()
                                self.ieDriver.find_element_by_css_selector(
                                    'table.mid_table_btn input[value="选择"]').click()
                                self.ieDriver.switch_to.parent_frame()
                                self.ieDriver.switch_to.frame('bodyFrame_all')
                                self.ieDriver.switch_to.frame('bodyFrame')
                                # 分类
                                # js_kind = 'document.getElementById("returnName1").innerHTML="盾构设备(B010101)" '
                                # self.ieDriver.execute_script(js_kind)
                                self.ieDriver.find_elements_by_xpath('//input[@value="选择"]')[2].click()
                                WebDriverWait(self.ieDriver, 500, 0.5).until(
                                    EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
                                iframe_kind = self.ieDriver.find_elements_by_tag_name('iframe')[0]
                                self.ieDriver.switch_to.frame(iframe_kind)
                                iframe_kind_one = self.ieDriver.find_element_by_id('ifm1')
                                self.ieDriver.switch_to.frame(iframe_kind_one)
                                self.ieDriver.find_elements_by_css_selector(
                                    'span#codeTree_container>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)>'
                                    'div:nth-child(1)>img')[0].click()
                                self.ieDriver.find_element_by_css_selector(
                                    'span#codeTree_container>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)>'
                                    'div:nth-child(2)>div:nth-child(3)>div:nth-child(1)>img:nth-child(4)').click()
                                self.ieDriver.switch_to.parent_frame()
                                self.ieDriver.find_element_by_css_selector('input[value=">>>"]').click()
                                sleep(3)
                                self.ieDriver.find_element_by_css_selector('input[value="保存"]').click()
                                self.ieDriver.switch_to.parent_frame()
                                self.ieDriver.switch_to.frame('bodyFrame_all')
                                self.ieDriver.switch_to.frame('bodyFrame')
                                # 本次招标合同估算价
                                self.ieDriver.find_element_by_name('null').clear()
                                self.ieDriver.find_element_by_name('null').send_keys('10')
                                # 标段(包)内容
                                self.ieDriver.find_element_by_xpath('//td/a[contains(text(),"标段(包)内容")]').click()
                                frame_bid = self.ieDriver.find_element_by_tag_name('iframe')
                                self.ieDriver.switch_to.frame(frame_bid)
                                self.ieDriver.find_element_by_name('bid/buildcontent').send_keys('测试')
                                self.ieDriver.find_element_by_css_selector('tr.form_bottom input[value="保存"]').click()
                                # self.ieDriver.switch_to.alert.text
                                WebDriverWait(self.ieDriver, 100, 0.5).until(EC.alert_is_present())
                                alert_save = self.ieDriver.switch_to_alert()
                                alert_save.accept()
                                sleep(2)
                                # ActionChains(self.ieDriver).send_keys(Keys.ENTER)
                                self.ieDriver.switch_to.parent_frame()
                                self.ieDriver.switch_to.frame('bodyFrame_all')
                                self.ieDriver.switch_to.frame('bodyFrame')
                                # 投标人资格条件
                                self.ieDriver.find_element_by_xpath('//td/a[contains(text(),"投标人资格条件")]').click()
                                frame_condition = self.ieDriver.find_element_by_tag_name('iframe')
                                self.ieDriver.switch_to.frame(frame_condition)
                                self.ieDriver.find_element_by_name('bid/tpcondition').send_keys('测试')
                                self.ieDriver.find_element_by_css_selector('tr.form_bottom input[value="保存"]').click()
                                WebDriverWait(self.ieDriver, 100, 0.5).until(EC.alert_is_present())
                                alert_save2 = self.ieDriver.switch_to_alert()
                                alert_save2.accept()
                                sleep(2)
                                # self.ieDriver.switch_to.alert.accept()
                                self.ieDriver.switch_to.parent_frame()
                                self.ieDriver.switch_to.frame('bodyFrame_all')
                                self.ieDriver.switch_to.frame('bodyFrame')
                                # 招标文件费用
                                self.ieDriver.find_element_by_name('evas[1]/signupcost').send_keys('0')
                                # 获取开标日期
                                # open_date = self.ieDriver.execute_script(
                                #     'document.getElementsByName("refs[1]/opendate1")[0].getAttribute("value")')
                                open_date = self.ieDriver.find_element_by_name('refs[1]/opendate1').get_attribute(
                                    'value')
                                split_date = re.split(r'\s+', open_date)
                                # 招标公告  开始日期
                                self.ieDriver.find_element_by_id('refs[1]/pubbgdate_input').send_keys(split_date[0])
                                # 报名
                                self.ieDriver.find_element_by_id('refs[1]/signupstartdate_show_id').send_keys(
                                    '%s 08:00' % split_date[0])
                                self.ieDriver.find_element_by_id('refs[1]/signupendtdate_show_id').send_keys(
                                    '%s 23:59' % split_date[0])
                                # 投标人提问截止时间
                                self.ieDriver.find_element_by_id('refs[1]/qaeddate_show_id').send_keys(
                                    '%s 23:59' % split_date[0])
                                # 开标方式
                                s = self.ieDriver.find_element_by_name('refs[1]/openmode')
                                Select(s).select_by_visible_text('网上开标（支持投标人在线远程签到解标及现场签到解标）')
                                # 保存
                                self.ieDriver.find_element_by_xpath(
                                    '//input[@value="返回招标项目列表"]/../input[@value="保存"]').click()
                                if i in range(4):
                                    WebDriverWait(self.ieDriver, 100, 0.5).until(EC.alert_is_present())
                                    alert_save2 = self.ieDriver.switch_to_alert()
                                    alert_save2.accept()
                                    sleep(2)
                                print('%s该项目已完成建档' % project_industrial_code)
                                break  # 如果找到用例的待招标建就档建之后终止循环
                        else:
                            continue  # 如果没有找到当前用例的项目就就继续执行下次循环直到找到
                    logging.info('没有待建档的项目')
                    print('没有待建档的项目')
                    # raise Exception('没有待建档的项目')

if __name__ == '__main__':
    c = CreateProjbase()
    c.create_projbase(0)






