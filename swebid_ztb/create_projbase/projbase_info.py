#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/11/21


class ProjOneInfo:
    def __init__(self, projtype, tradetype, orgform, qualifymethod, isallowcoalition,
                 noofbids, bondfrombase, bidcount, prof_category, work_category, bidmid):
        self.projtype = projtype  # 项目类型
        self.tradetype = tradetype  # 招标方式
        self.orgform = orgform  # 招标组织形式
        self.qualifymethod = qualifymethod  # 资格审查方法
        self.isallowcoalition = isallowcoalition  # 是否接受联合体投标
        self.noofbids = noofbids  # 招标次数
        self.bondfrombase = bondfrombase  # 是否要求基本账户缴交投标保证金
        self.bidcount = bidcount  # 标段(包)数量
        self.prof_category = prof_category  # 专业类别
        self.work_category = work_category  # 工程类别
        self.bidmid = bidmid  # 评标办法

    def set_projtype(self, projtype):
        self.projtype = projtype
        return self.projtype

    def get_projtype(self):
        return self.projtype

    def set_tradetype(self, tradetype):
        self.projtype = tradetype
        return self.tradetype

    def get_tradetype(self):
        return self.tradetype

    def set_orgform(self, orgform):
        self.orgform = orgform
        return self.orgform

    def get_orgform(self):
        return self.orgform

    def set_qualifymethod(self, qualifymethod):
        self.qualifymethod = qualifymethod
        return self.qualifymethod

    def get_qualifymethod(self):
        return self.qualifymethod

    def set_isallowcoalition(self, isallowcoalition):
        self.isallowcoalition = isallowcoalition
        return self.isallowcoalition

    def get_isallowcoalition(self):
        return self.isallowcoalition

    def set_noofbids(self, noofbids):
        self.noofbids = noofbids
        return self.noofbids

    def get_noofbids(self):
        return self.noofbids

    def set_bondfrombase(self, bondfrombase):
        self.bondfrombase = bondfrombase
        return self.bondfrombase

    def get_bondfrombase(self):
        return self.bondfrombase

    def set_bidcount(self, bidcount):
        self.bidcount = bidcount
        return self.bidcount

    def get_bidcount(self):
        return self.bidcount

    def set_bidmid(self, bidmid):
        self.bidmid = bidmid
        return self.bidmid

    def get_bidmid(self):
        return self.bidmid

    def set_prof_category(self, prof_category):
        self.prof_category = prof_category
        return self.prof_category

    def get_prof_category(self):
        return self.prof_category

    def set_work_category(self, work_category):
        self.work_category = work_category
        return self.work_category

    def get_work_category(self):
        return self.work_category




