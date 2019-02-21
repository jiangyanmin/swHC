#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/11/6


class TenderInformationInfo:
    def __init__(self, is_law_bid, bid_register_report_no, bid_register_proj_code,
                 bid_register_proj_name, bid_register_owner_name, bid_register_linktel
                 ):
        self.is_law_bid = is_law_bid
        self.bid_register_report_no = bid_register_report_no
        self.bid_register_proj_code = bid_register_proj_code
        self.bid_register_proj_name = bid_register_proj_name
        self.bid_register_owner_name = bid_register_owner_name
        self.bid_register_linktel = bid_register_linktel

    def set_is_law_bid(self, is_law_bid):
        self.is_law_bid = is_law_bid
        return self.is_law_bid

    def get_is_law_bid(self):
        return self.is_law_bid

    def set_bid_register_report_no(self, bid_register_report_no):
        self.bid_register_report_no = bid_register_report_no
        return self.bid_register_report_no

    def get_bid_register_report_no(self):
        return self.bid_register_report_no

    def set_bid_register_proj_code(self, bid_register_proj_code):
        self.bid_register_proj_code = bid_register_proj_code
        return self.bid_register_proj_code

    def get_bid_register_proj_code(self):
        return self.bid_register_proj_code

    def set_bid_register_proj_name(self, bid_register_proj_name):
        self.bid_register_proj_name = bid_register_proj_name
        return self.bid_register_proj_name

    def get_bid_register_proj_name(self):
        return self.bid_register_proj_name

    def set_bid_register_owner_name(self, bid_register_owner_name):
        self.bid_register_owner_name = bid_register_owner_name
        return self.bid_register_owner_name

    def get_bid_register_owner_name(self):
        return self.bid_register_owner_name

    def set_bid_register_linktel(self, bid_register_linktel):
        self.bid_register_linktel = bid_register_linktel
        return self.bid_register_linktel

    def get_bid_register_linktel(self):
        return self.bid_register_linktel
