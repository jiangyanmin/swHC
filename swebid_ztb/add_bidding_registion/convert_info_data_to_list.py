#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/11/8
from swebid_ztb.add_bidding_registion.project_information_info import ProjectInformationInfo
from swebid_ztb.add_bidding_registion.tender_information_info import TenderInformationInfo
from swebid_ztb.parser_excel_info import ParserExcelInfo
from swebid_ztb.add_bidding_registion.tender_confirm_info import TenderConfirmInfo


class ConvertInfoDataToList:
    def __init__(self):
        pass

    @staticmethod
    # 把从excel读取出的用例嵌套列表转换成行读取出来
    def convert_tender_info_to_list():
        data = ParserExcelInfo(r'E:\Project\python\swebid\swebid_ztb\招投标流程测试用例.xlsx', 'TenderInformation', 5, 6)
        # 获取所有用例数据列表
        tender_information_data_list = data.parser_excel_info()
        every_tender_information_data_list = []  # 列表，存储获取每一行用例数据
        for i in range(len(tender_information_data_list)):
            is_law_bid = tender_information_data_list[i][0]
            bid_register_report_no = tender_information_data_list[i][1]
            bid_register_proj_code = tender_information_data_list[i][2]
            bid_register_proj_name = tender_information_data_list[i][3]
            bid_register_owner_name = tender_information_data_list[i][4]
            bid_register_linktel = tender_information_data_list[i][5]
            tender_information_info = TenderInformationInfo(is_law_bid, bid_register_report_no,
                                                            bid_register_proj_code, bid_register_proj_name,
                                                            bid_register_owner_name, bid_register_linktel)
            every_tender_information_data_list.append(tender_information_info)
        return every_tender_information_data_list

    # 把从excel读取出的完善信息用例嵌套列表转换成行读取出来
    @staticmethod
    def convert_project_info_to_list():
        data = ParserExcelInfo(r'E:\Project\python\swebid\swebid_ztb\招投标流程测试用例.xlsx', 'ProjectInformation', 5, 6)
        # 获取所有用例数据列表
        project_information_info_list = data.parser_excel_info()
        every_project_info_list = []  # 列表，存储获取每一行用例数据
        for i in range(len(project_information_info_list)):
            project_type = project_information_info_list[i][0]
            # scanning_copy = project_information_info_list[i][1]
            project_name = project_information_info_list[i][1]
            project_industrial_code = project_information_info_list[i][2]
            project_addr = project_information_info_list[i][3]
            project_fund_source = project_information_info_list[i][4]
            project_information_info = ProjectInformationInfo(project_type, project_name, project_industrial_code,
                                                              project_addr, project_fund_source)
            every_project_info_list.append(project_information_info)
        return every_project_info_list

    @staticmethod
    def convert_confirm_info_to_list():
        data = ParserExcelInfo(r'E:\Project\python\swebid\swebid_ztb\招投标流程测试用例.xlsx', '招标选项确认', 5, 6)
        # 获取所有用例数据列表
        tender_confirm_info_list = data.parser_excel_info()
        every_confirm_info_list = []  # 列表，存储获取每一行用例数据
        for i in range(len(tender_confirm_info_list)):
            is_ebid = tender_confirm_info_list[i][0]
            is_forcebid = tender_confirm_info_list[i][1]
            tender_confirm_info = TenderConfirmInfo(is_ebid, is_forcebid)
            every_confirm_info_list.append(tender_confirm_info)
        return every_confirm_info_list


