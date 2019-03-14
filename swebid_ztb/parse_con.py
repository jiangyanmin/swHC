#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2019-03-11
from configparser import ConfigParser


# 解析配置文件
class ParseCon:
    def __init__(self):
        pass

    @staticmethod
    def parse_con():
        cf = ConfigParser()
        # self.db_host = ConfigParser.get('db', 'db_host')
        # self.db_port = ConfigParser.get('db', 'db_port')
        # self.db_username = ConfigParser.get('db', 'db_user')
        # self.db_password = ConfigParser.get('db', 'db_password')
        con = cf.read('E:\Project\python\swebid\swebid_ztb\config.ini')
        sec = cf.sections()

        # for i in len(self.sec):
        #     self.opts = self.cf.options(self.sec[i])
        #     for j in len(self.opts):
        #         self.opt = self.cf.get(self.sec[i], self.opts[j])

        return sec, cf

if __name__ == '__main__':
    ti = ParseCon()
    # ti.setUP()
    print(ti.parse_con()[0])









