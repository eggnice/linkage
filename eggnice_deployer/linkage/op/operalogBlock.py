#!/usr/bin/python
# coding=utf-8

import re
from linkage.op import baseOperalogSql


class Operationlog(object):
    def __init__(self, user_name, begin_time, end_time):
        self.user_name = user_name
        self.begin_time = begin_time
        self.end_time = end_time
        user_id = baseOperalogSql.getUserId(self.user_name)[0]["ID"]
        operalog = baseOperalogSql.getOperalog(user_id, self.begin_time, self.end_time)
        if operalog:
            self.log_num = len(operalog)
            self.log_list = operalog
            self.log_exist = True
        else:
            self.log_exist = False

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))
