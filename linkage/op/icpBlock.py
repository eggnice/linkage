#! /usr/bin/env python
# _*_ coding:utf-8 _*_

import re
from linkage.op.baseIcpSql import geticpinfo


class Icp(object):
    def __init__(self, icp_public_ip):
        self.icp_public_ip = icp_public_ip
        icp_info = geticpinfo(icp_public_ip)
        if icp_info:
            self.id = icp_info[0].get('ID')
            self.icp_id = icp_info[0].get('ICP_ID')
            self.user_id = icp_info[0].get('USER_ID')
            self.customer_id = icp_info[0].get('CUSTOMER_ID')
            self.icp_cert_code = icp_info[0].get('ICP_CERT_CODE')
            self.icp_status = icp_info[0].get('ICP_STATUS')
            self.icp_type = icp_info[0].get('ICP_TYPE')
            self.icp_register_time = icp_info[0].get('ICP_REGISTER_TIME')
            self.icp_update_time = icp_info[0].get('ICP_UPDATE_TIME')
            self.icp_public_ip = icp_info[0].get('ICP_PUBLIC_IP')
            self.icp_domain = icp_info[0].get('ICP_DOMAIN')
            self.icp_province = icp_info[0].get('ICP_PROVINCE')
            self.icp_city = icp_info[0].get('ICP_CITY')
            self.icp_suggestion = icp_info[0].get('ICP_SUGGESTION')
            self.icp_auditor = icp_info[0].get('ICP_AUDITOR')
            self.icp_contactor = icp_info[0].get('ICP_CONTACTOR')
            self.icp_contactor_phone = icp_info[0].get('ICP_CONTACTOR_PHONE')
            self.pool_id = icp_info[0].get('POOL_ID')
            self.icp_bbfs = icp_info[0].get('ICP_BBFS')
            self.icp_icpmm = icp_info[0].get('ICP_ICPMM')
            self.icp_return_code = icp_info[0].get('ICP_RETURN_CODE')
            self.icp_return_msg = icp_info[0].get('ICP_RETURN_MSG')
            self.ip_id = icp_info[0].get('IP_ID')
            self.icp_is_success = icp_info[0].get('ICP_IS_SUCCESS')
            self.icp_exist = True
        else:
            self.icp_exist = False
            print('Icp is not found!')

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))
