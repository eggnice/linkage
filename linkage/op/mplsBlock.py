#! /usr/bin/env python
# -*- coding:utf-8 -*-

import re
from linkage.op.baseMplsSql import getmplsinfo


class Mpls(object):
    def __init__(self, mpls_id):
        self.mpls_id = mpls_id
        mpls_info = getmplsinfo(mpls_id)
        if mpls_info:
            self.mpls_name = mpls_info[0].get('MPLS_NAME')
            self.bandwidth = mpls_info[0].get('BANDWIDTH')
            self.ecloud_cidrs = mpls_info[0].get('ECLOUD_CIDRS')
            self.resource_config_id = mpls_info[0].get('RESOURCE_CONFIG_ID')
            self.dest_cidrs = mpls_info[0].get('DEST_CIDRS')
            self.created_time = mpls_info[0].get('CREATED_TIME')
            self.modified_time = mpls_info[0].get('MODIFIED_TIME')
            self.user_id = mpls_info[0].get('USER_ID')
            self.customer_id = mpls_info[0].get('CUSTOMER_ID')
            self.status = mpls_info[0].get('STATUS')
            self.is_delete = mpls_info[0].get('IS_DELETE')
            self.region = mpls_info[0].get('REGION')
            self.router_id = mpls_info[0].get('ROUTER_ID')
            self.mpls_exist = True
        else:
            self.mpls_exist = False
            print('mpls is not found!')

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))
