#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/12/4


class TenderConfirmInfo:
    def __init__(self, is_ebid, is_forcebid):
        self.is_ebid = is_ebid
        self.is_forcebid = is_forcebid

    def set_is_ebid(self, is_ebid):
        self.is_ebid = is_ebid
        return self.is_ebid

    def get_is_ebid(self):
        return self.is_ebid

    def set_is_forcebid(self, is_forcebid):
        self.is_forcebid = is_forcebid
        return self.is_forcebid

    def get_is_forcebid(self):
        return self.is_forcebid



