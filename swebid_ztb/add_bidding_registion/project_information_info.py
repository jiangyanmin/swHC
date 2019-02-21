#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/11/6


class ProjectInformationInfo:
    def __init__(self, project_type, project_name, project_industrial_code,
                 project_addr, project_fund_source):
        self.project_type = project_type
        self.project_name = project_name
        # self.province = province
        # self.city = city
        # self.area = area
        self.project_industrial_code = project_industrial_code
        self.project_addr = project_addr
        self.project_fund_source = project_fund_source

    def set_project_type(self, project_type):
        self.project_type = project_type
        return self.project_type

    def get_project_type(self):
        return self.project_type

    def set_project_name(self, project_name):
        self.project_name = project_name
        return self.project_name

    def get_project_name(self):
        return self.project_name

    # def set_province(self, province):
    #     self.province = province
    #     return self.province
    #
    # def get_province(self):
    #     return self.province
    #
    # def set_city(self, city):
    #     self.city = city
    #     return self.city
    #
    # def get_city(self):
    #     return self.city
    #
    # def set_area(self, area):
    #     self.area = area
    #     return self.area
    #
    # def get_area(self):
    #     return self.area

    def set_project_industrial_code(self, project_industrial_code):
        self.project_industrial_code = project_industrial_code
        return self.project_industrial_code

    def get_project_industrial_code(self):
        return self.project_industrial_code

    def set_project_addr(self, project_addr):
        self.project_addr = project_addr
        return self.project_addr

    def get_project_addr(self):
        return self.project_addr

    def set_project_fund_source(self, project_fund_source):
        self.project_fund_source = project_fund_source
        return self.project_fund_source

    def get_project_fund_source(self):
        return self.project_fund_source

