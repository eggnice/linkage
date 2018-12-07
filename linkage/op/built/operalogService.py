#!/usr/bin/env python
# -*- coding: utf-8 -*-

from linkage.op import operalogBlock
import re
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


def operalogcheck(user_name, begin_time, end_time):
    log = operalogBlock.Operationlog(user_name, begin_time, end_time)
    if log.log_exist:
        for item_log in log.log_list:
            print("%s: %s" % ("ID", item_log["ID"]))
            print("%s: %s" % ("ACTION", item_log["ACTION"]))
            print("%s: %s" % ("OPERATOR_TIME", item_log["OPERATOR_TIME"]))
            print("%s: %s" % ("USER_ID", item_log["USER_ID"]))
            print("%s: %s" % ("EXTRA", item_log["EXTRA"]))
            print("%s: %s" % ("RESULT_CODE", item_log["RESULT_CODE"]))
            print("%s: %s" % ("RESULT_MSG", item_log["RESULT_MSG"]))
            print("#" * 44)
    else:
        print("未找到操作日志")
