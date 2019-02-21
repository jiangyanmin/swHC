#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/11/8
import xlrd
import xlrd.biffh


class ParserExcelInfo:
    def __init__(self, excel_path, sheet_name, field_name_index,
                 test_data_start_nrow, test_data_end_nrow=None):
        self.excel_path = excel_path  # excel文件路径
        self.sheet_name = sheet_name  # 工作表名称
        self.field_name_index = field_name_index  # 用例起始行
        self.test_data_start_nrow = test_data_start_nrow  # 测试数据起始行
        self.test_data_end_nrow = test_data_end_nrow  # 测试数据结束行

    def parser_excel_info(self):
        try:
            test_data_work_book = xlrd.open_workbook(self.excel_path)
        except Exception as e:
            print('无法打开excel文件，路径：%s，错误信息：%s' % (self.excel_path, e))
            raise IOError('Can not open excel,error message:%s' % e)
        if test_data_work_book is not None:
            try:
                test_data_sheet = test_data_work_book.sheet_by_name(self.sheet_name)
            except xlrd.biffh.XLRDError as e:
                print('Can not open sheet:%s,error message:%s' % (self.sheet_name, e))

        if test_data_sheet.nrows <= 0:
            raise Exception('未在工作表找到数据！')
        else:
            test_data_list = []
            total_col_of_test_case = len(test_data_sheet.row(self.field_name_index))  # 返回第6行的单元格对象序列的长度，即总列数
            if self.test_data_end_nrow is None:
                total_row_of_test_case = test_data_sheet.nrows  # 返回测试用例总行数
            else:
                total_row_of_test_case = self.test_data_end_nrow
            for r in range(self.test_data_start_nrow, total_row_of_test_case):
                every_row_test_data_list = []
                for n in range(total_col_of_test_case):
                    cell_data_of_test_case = test_data_sheet.cell_value(r, n)  # 返回测试用例每一个单元格的值
                    every_row_test_data_list.append(cell_data_of_test_case)
                # print(every_row_test_data_list)
                # print('========================')
                test_data_list.append(every_row_test_data_list)
                # print(test_data_list)
        return test_data_list
