#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2019-03-12
from swebid_ztb.parse_con import ParseCon


# 封装section[login]
def conf_login():
    login = 'login'
    cf = ParseCon.parse_con()[1]
    con = ParseCon.parse_con()[0]

    if login in con:
        url = cf.get(login, 'log_url')
        user = cf.get(login, 'log_user')
        password = cf.get(login, 'log_password')

        return url, user, password
    else:
        raise Exception('没有找到section[login]')
