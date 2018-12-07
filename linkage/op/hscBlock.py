#! /usr/bin/env python
# _*_ coding:utf-8 _*_

import re
from linkage.op.baseHscSql import gethscinfo


class Hsc(object):
    def __init__(self, hsc_id):
        self.hsc_id = hsc_id
        hsc_info = gethscinfo(hsc_id)
        if hsc_info:
            self.resource_config_id = hsc_info[0].get('RESOURCE_CONFIG_ID')
            self.router_id = hsc_info[0].get('ROUTER_ID')
            self.hsc_name = hsc_info[0].get('HSC_NAME')
            self.circle_num = hsc_info[0].get('CIRCLE_NUM')
            self.circle_id = hsc_info[0].get('CIRCLE_ID')
            self.status = hsc_info[0].get('STATUS')
            self.is_delete = hsc_info[0].get('IS_DELETE')
            self.user_id = hsc_info[0].get('USER_ID')
            self.customer_id = hsc_info[0].get('CUSTOMER_ID')
            self.created_time = hsc_info[0].get('CREATED_TIME')
            self.modified_time = hsc_info[0].get('MODIFIED_TIME')
            self.region = hsc_info[0].get('REGION')
            self.ecloud_cidr = hsc_info[0].get('ECLOUD_CIDR')
            self.dest_cidr = hsc_info[0].get('DEST_CIDR')
            self.bandwidth = hsc_info[0].get('BANDWIDTH')
            self.circle_is_delete = hsc_info[0].get('CIRCLE_IS_DELETE')
            self.province_addr = hsc_info[0].get('PROVINCE_ADDR')
            self.city_addr = hsc_info[0].get('CITY_ADDR')
            self.dist_addr = hsc_info[0].get('DIST_ADDR')
            self.addr_detail = hsc_info[0].get('ADDR_DETAIL')
            self.hsc_exist = True
        else:
            self.hsc_exist = False
            print('hsc is not found!')

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))
