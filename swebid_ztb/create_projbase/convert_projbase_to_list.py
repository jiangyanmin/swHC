#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/11/21
from swebid_ztb.parser_excel_info import ParserExcelInfo
from swebid_ztb.create_projbase.projbase_info import ProjOneInfo


class ConvertProjbaseToList:
    def __init__(self):
        pass

    @staticmethod
    # 把从excel读取出的用例嵌套列表转换成行读取出来
    def convert_one_info_to_list():
        data = ParserExcelInfo('招投标流程测试用例.xlsx', '招标建档（第一步）', 5, 6)
        # 获取所有用例数据列表
        one_data_list = data.parser_excel_info()
        every_one_data_list = []  # 列表，存储获取每一行用例数据
        for i in range(len(one_data_list)):
            projtype = one_data_list[i][0]
            tradetype = one_data_list[i][1]
            orgform = one_data_list[i][2]
            qualifymethod = one_data_list[i][3]
            isallowcoalition = one_data_list[i][4]
            noofbids = one_data_list[i][5]
            bondfrombase = one_data_list[i][6]
            bidcount = one_data_list[i][7]
            prof_category = one_data_list[i][8]
            work_category = one_data_list[i][9]
            bidmid = one_data_list[i][10]
            one_info = ProjOneInfo(projtype, tradetype, orgform, qualifymethod, isallowcoalition,
                 noofbids, bondfrombase, bidcount, prof_category, work_category, bidmid)
            every_one_data_list.append(one_info)
        return every_one_data_list
