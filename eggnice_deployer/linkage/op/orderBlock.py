#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
from linkage.op.baseOrderSql import getOrderInfo
from linkage.op.baseOrderSql import getExtInfo
from linkage.op.baseOrderSql import getArchiveInfo
from linkage.op.baseOrderSql import getLogInfo
from linkage.op.baseOrderSql import getBosslogInfo
from linkage.op.baseOrderSql import getExtInfoById
from linkage.op.baseOrderSql import getPromotionInfo

reload(sys)
sys.setdefaultencoding('utf-8')


class Order(object):
    """get order information according to order_id"""

    def __init__(self, _order_id):
        self.order_exist = ''
        self.order_id = ''
        self.order_type = ''
        self.order_status = ''
        self.parent_id = ''
        self.order_time = ''
        self.proposer = ''
        self.proposer_name = ''
        self.cmp_customer_id = ''
        self.cmp_customer_name = ''
        self.order_memo = ''
        self.order_source = ''
        self.confirm_by = ''
        self.approval_msg = ''
        self.open_type = ''
        self.order_json = ''
        self.confirm_time = ''
        self.total = ''
        self.orderInfo(_order_id)

    def orderInfo(self, _order_id):
        result = getOrderInfo(_order_id)
        if result:
            self.order_exist = True
            self.order_id = result[0]["ORDER_ID"]
            self.order_type = result[0]["ORDER_TYPE"]
            self.order_status = result[0]["ORDER_STATUS"]
            self.parent_id = result[0]["PARENT_ID"]
            self.order_time = result[0]["ORDER_TIME"]
            self.proposer = result[0]["PROPOSER"]
            self.proposer_name = result[0]["PROPOSER_NAME"]
            self.cmp_customer_id = result[0]["CMP_CUSTOMER_ID"]
            self.cmp_customer_name = result[0]["CMP_CUSTOMER_NAME"]
            self.order_memo = result[0]["ORDER_MEMO"]
            self.order_source = result[0]["ORDER_SOURCE"]
            self.confirm_by = result[0]["CONFIRM_BY"]
            self.approval_msg = result[0]["APPROVAL_MSG"]
            self.open_type = result[0]["OPEN_TYPE"]
            self.order_json = result[0]["ORDER_JSON"]
            self.confirm_time = result[0]["CONFIRM_TIME"]
            self.total = result[0]["TOTAL"]
        else:
            self.order_exist = False
            print('"订单" %s "不存在"' % _order_id)
        return result

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key) or re.findall('^orderInfo', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))


class Extbyid(object):
    """get order ext information according to order_id"""

    def __init__(self, _ext_id):
        self.ext_num = ''
        self.ext_list = []
        self.extInfo(_ext_id)

    def extInfo(self, _ext_id):
        result = getExtInfoById(_ext_id)
        if result:
            self.ext_num = len(result)
            self.ext_list = result
        else:
            print('Ext is not found')

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key) or re.findall('^extInfo', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))


class Ext(object):
    """get order ext information according to order_id"""

    def __init__(self, _order_id):
        self.ext_num = ''
        self.ext_list = []
        self.extInfo(_order_id)

    def extInfo(self, _order_id):
        result = getExtInfo(_order_id)
        if result:
            self.ext_num = len(result)
            self.ext_list = result
        else:
            print('Ext is not found')

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key) or re.findall('^extInfo', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))


class Archive(object):
    """get archive information according to ext_id"""

    def __init__(self, _ext_id):
        self.archive_num = ''
        self.archive_list = []
        self.archiveInfo(_ext_id)

    def archiveInfo(self, _ext_id):
        result = getArchiveInfo(_ext_id)
        if result:
            self.archive_num = len(result)
            self.archive_list = result

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key) or re.findall('^archiveInfo', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))


class Log(object):
    """get log information according to ext_id"""

    def __init__(self, _ext_id):
        self.log_num = ''
        self.log_list = []
        self.logInfo(_ext_id)

    def logInfo(self, _ext_id):
        result = getLogInfo(_ext_id)
        if result:
            self.log_num = len(result)
            self.log_list = result
        else:
            print('Log is not found!')

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key) or re.findall('logInfo', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))


class Bosslog(object):
    """get bosslog information according to op_order_num"""

    def __init__(self, _op_order_num):
        self.bosslog_num = ''
        self.bosslog_list = []
        self.bosslogInfo(_op_order_num)

    def bosslogInfo(self, _op_order_num):
        result = getBosslogInfo(_op_order_num)
        if result:
            self.bosslog_num = len(result)
            self.bosslog_list = result
        else:
            print('未找到同步BOSS日志')

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key) or re.findall('^bosslogInfo', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))


class Promotion(object):
    """get promotion information according to order_id"""

    def __init__(self, _order_id):
        self.promotion_exist = ''
        self.promotionInfo(_order_id)

    def promotionInfo(self, _order_id):
        result = getPromotionInfo(_order_id)
        if result:
            self.promotion_exist = True
        else:
            self.promotion_exist = False
            print('此订单 %s 不是促销订单' % _order_id)

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key) or re.findall('^promotionInfo', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))
