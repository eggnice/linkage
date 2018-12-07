#! /usr/bin/env python
# _*_ coding:utf-8 _*_

import re
from linkage.op.baseUserInfosql import Getuserinfo
from linkage.op.baseUserInfosql import Newuserinfo
defaultencoding = 'utf-8'


class userInfo(object):

    def __init__(self, _argument):
        self.user_exist = ''
        self.user_id = ''
        self.user_name = _argument
        self.email = _argument
        self.phone = _argument
        self.is_customer = ''
        self.LOGIN_FAILED_COUNT = ''
        self.ucreate_time = ''
        self.customer_id = _argument
        self.boss_cust_id = ''
        self.cust_status = ''
        self.reg_source = ''
        self.IS_HUAWEI = ''
        self.boss_pro_order_code = ''
        self.global_discount = ''
        self.payment_type = ''
        self.contactor = ''
        self.mng_phone = ''
        self.create_time = ''
        self.user_status = ''
        self.nick_name = ''
        self.cust_name = ''
        self.is_first_login = ''
        self.boss_order_id = ''
    """get user information according to user_name"""

    def userInfo_username(self):
        getuserinfo = Getuserinfo(self.user_name)
        result = getuserinfo.getuserinfo_username()
        if result:
            self.user_exist = True
            self.user_id = result[0]['user_id'].encode('utf-8')
            self.user_name = result[0]['user_name'].encode('utf-8')
            self.email = result[0]['email'].encode('utf-8')
            self.phone = result[0]['phone'].encode('utf-8')
            self.is_customer = result[0]['is_customer'].encode('utf-8')
            self.LOGIN_FAILED_COUNT = result[0]['LOGIN_FAILED_COUNT']
            self.ucreate_time = result[0]['create_time']
            self.customer_id = result[0]['customer_id']
            self.boss_cust_id = result[0]['boss_cust_id']
            self.boss_order_id = result[0]['boss_order_id']
            self.cust_status = result[0]['CUST_STATUS'].encode('utf-8')
            self.reg_source = result[0]['reg_source']
            self.IS_HUAWEI = result[0]['IS_HUAWEI']
            self.boss_pro_order_code = result[0]['boss_pro_order_code']
            self.global_discount = result[0]['global_discount']
            self.payment_type = result[0]['reg_source']
            self.contactor = result[0]['contactor']
            self.mng_phone = result[0]['mng_phone']
            self.create_time = result[0]['create_time']
            self.user_status = result[0]['user_status'].encode('utf-8')
            self.nick_name = result[0]['nick_name'].encode('utf-8')
            self.cust_name = result[0]['cust_name'].encode('utf-8')
            self.is_first_login = result[0]['is_first_login']
        else:
            self.user_exist = False
#            print('User is not found')

    """get user information according to mobile"""

    def userInfo_phone(self):
        getuserinfo = Getuserinfo(self.phone)
        result = getuserinfo.getuserinfo_mobiles()
        if result:
            self.user_exist = True
            self.user_id = result[0]['user_id'].encode('utf-8')
            self.user_name = result[0]['user_name'].encode('utf-8')
            self.email = result[0]['email'].encode('utf-8')
            self.phone = result[0]['phone'].encode('utf-8')
            self.is_customer = result[0]['is_customer']
            self.LOGIN_FAILED_COUNT = result[0]['LOGIN_FAILED_COUNT']
            self.ucreate_time = result[0]['create_time']
            self.customer_id = result[0]['customer_id']
            self.boss_cust_id = result[0]['boss_cust_id']
            self.boss_order_id = result[0]['boss_order_id']
            self.cust_status = result[0]['CUST_STATUS'].encode('utf-8')
            self.reg_source = result[0]['reg_source']
            self.IS_HUAWEI = result[0]['IS_HUAWEI']
            self.boss_pro_order_code = result[0]['boss_pro_order_code']
            self.global_discount = result[0]['global_discount']
            self.payment_type = result[0]['payment_type']
            self.contactor = result[0]['contactor']
            self.mng_phone = result[0]['mng_phone']
            self.create_time = result[0]['create_time']
            self.user_status = result[0]['user_status'].encode('utf-8')
            self.nick_name = result[0]['nick_name'].encode('utf-8')
            self.cust_name = result[0]['cust_name'].encode('utf-8')
            self.is_first_login = result[0]['is_first_login']
        else:
            self.user_exist = False
#           print('User is not found')

    """get user information according to email"""

    def userInfo_email(self):
        getuserinfo = Getuserinfo(self.email)
        result = getuserinfo.getuserinfo_email()
        if result:
            self.user_exist = True
            self.user_id = result[0]['user_id'].encode('utf-8')
            self.user_name = result[0]['user_name'].encode('utf-8')
            self.email = result[0]['email'].encode('utf-8')
            self.phone = result[0]['phone'].encode('utf-8')
            self.is_customer = result[0]['is_customer'].encode('utf-8')
            self.LOGIN_FAILED_COUNT = result[0]['LOGIN_FAILED_COUNT']
            self.ucreate_time = result[0]['create_time']
            self.customer_id = result[0]['customer_id']
            self.boss_cust_id = result[0]['boss_cust_id']
            self.boss_order_id = result[0]['boss_order_id']
            self.cust_status = result[0]['CUST_STATUS'].encode('utf-8')
            self.reg_source = result[0]['reg_source']
            self.IS_HUAWEI = result[0]['IS_HUAWEI']
            self.boss_pro_order_code = result[0]['boss_pro_order_code']
            self.global_discount = result[0]['global_discount']
            self.payment_type = result[0]['payment_type']
            self.contactor = result[0]['contactor']
            self.mng_phone = result[0]['mng_phone']
            self.create_time = result[0]['create_time']
            self.user_status = result[0]['user_status'].encode('utf-8')
            self.nick_name = result[0]['nick_name'].encode('utf-8')
            self.cust_name = result[0]['cust_name'].encode('utf-8')
            self.is_first_login = result[0]['is_first_login']
        else:
            self.user_exist = False
#            print('User is not found')

    """get user information according to customer_id"""

    def userInfo_id(self):
        getuserinfo = Getuserinfo(self.customer_id)
        result = getuserinfo.getuserinfo_id()
        if result:
            self.user_exist = True
            self.user_id = result[0]['user_id'].encode('utf-8')
            self.user_name = result[0]['user_name'].encode('utf-8')
            self.email = result[0]['email'].encode('utf-8')
            self.phone = result[0]['phone'].encode('utf-8')
            self.is_customer = result[0]['is_customer']
            self.LOGIN_FAILED_COUNT = result[0]['LOGIN_FAILED_COUNT']
            self.ucreate_time = result[0]['create_time']
            self.customer_id = result[0]['customer_id']
            self.boss_cust_id = result[0]['boss_cust_id']
            self.boss_order_id = result[0]['boss_order_id']
            self.cust_status = result[0]['CUST_STATUS'].encode('utf-8')
            self.reg_source = result[0]['reg_source']
            self.IS_HUAWEI = result[0]['IS_HUAWEI']
            self.boss_pro_order_code = result[0]['boss_pro_order_code']
            self.global_discount = result[0]['global_discount']
            self.payment_type = result[0]['payment_type']
            self.contactor = result[0]['contactor']
            self.mng_phone = result[0]['mng_phone']
            self.create_time = result[0]['create_time']
            self.user_status = result[0]['user_status'].encode('utf-8')
            self.nick_name = result[0]['nick_name'].encode('utf-8')
            self.cust_name = result[0]['cust_name'].encode('utf-8')
            self.is_first_login = result[0]['is_first_login']
        else:
            self.user_exist = False
#            print('User is not found')

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key) or \
                    re.findall('^userInfo_username', key) or \
                    re.findall('^userInfo_mobile', key) or \
                    re.findall('^userInfo_email', key) or \
                    re.findall('^bossagentinfo', key) or \
                    re.findall('^userInfo_id', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))


class userInfoNew(object):
    def __init__(self, _argument1, _argument2, _argument3, _argument4, _argument5):
        self.result = ''
        self.username = _argument1
        self.phone = _argument2
        self.email = _argument3
        self.customer_id = _argument4
        self.phone_new = _argument5

    def userInfo_all(self):
        result = Newuserinfo(self.username, self.phone, self.email, self.customer_id, self.phone_new)
        result = result.getuserinfo_all()
        self.result = result

    def newuserphone(self):
        result = Newuserinfo(self.username, self.phone, self.email, self.customer_id, self.phone_new)
        result = result.newuserinfo_phone()
        self.result = result

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key) or \
                    re.findall('^userInfo_all', key) or \
                    re.findall('^newuserphone', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))


""" get user resgistry information """


class bossloginfo(object):
    def __init__(self, _argument):
        self.bosslog_exit = ''
        self.bosslog_num = ''
        self.bosslog_list = []
        self.op_order_number = _argument
        self.boss_order_id = _argument

    def bossloginfo(self):
        getuserinfo = Getuserinfo(self.op_order_number)
        result = getuserinfo.getbossloginfo()
        if result:
            self.bosslog_exit = True
            self.bosslog_num = len(result)
            self.bosslog_list = result
        else:
            self.bosslog_exit = False
            print("bossagentlog is not found")

    def bosslog_id(self):
        getuserinfo = Getuserinfo(self.boss_order_id)
        result = getuserinfo.getbosslog_id()
        if result:
            self.bosslog_exit = True
            self.bosslog_num = len(result)
            self.bosslog_list = result
        else:
            self.bosslog_exit = False

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key) or \
                    re.findall('^userInfo_username', key) or \
                    re.findall('^userInfo_mobile', key) or \
                    re.findall('^userInfo_email', key) or \
                    re.findall('^bossagentinfo', key) or \
                    re.findall('^userInfo_id', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))
