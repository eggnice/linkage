#! /usr/bin/env python
# _*_ coding:utf-8 _*_

import re
from linkage.op.baseIpsecSql import getipsecinfo


class Ipsec(object):
    def __init__(self, id):
        self.id = id
        ipsec_info = getipsecinfo(id)
        if ipsec_info:
            self.name = ipsec_info[0].get('NAME')
            self.status = ipsec_info[0].get('STATUS')
            self.subnet_id = ipsec_info[0].get('SUBNET_ID')
            self.router_id = ipsec_info[0].get('ROUTER_ID')
            self.pool_id = ipsec_info[0].get('POOL_ID')
            self.customer_id = ipsec_info[0].get('CUSTOMER_ID')
            self.proposer = ipsec_info[0].get('PROPOSER')
            self.created_by = ipsec_info[0].get('GREATED_BY')
            self.created_time = ipsec_info[0].get('GREATED_TIME')
            self.modified_by = ipsec_info[0].get('MODIFIED_BY')
            self.modified_time = ipsec_info[0].get('MODIFIED_TIME')
            self.is_delete = ipsec_info[0].get('IS_DELETE')
            self.ikepolicy_id = ipsec_info[0].get('IKEPOLICY_ID')
            self.ipsecpolicy_id = ipsec_info[0].get('IPSECPOLICY_ID')
            self.peer_address = ipsec_info[0].get('PEER_ADDRESS')
            self.peer_id = ipsec_info[0].get('PEER_ID')
            self.peer_cidrs = ipsec_info[0].get('PEER_CIDRS')
            self.auth_mode = ipsec_info[0].get('AUTH_MODE')
            self.route_mode = ipsec_info[0].get('ROUTE_MODE')
            self.mtu = ipsec_info[0].get('MTU')
            self.initiator = ipsec_info[0].get('INITIATOR')
            self.psk = ipsec_info[0].get('PSK')
            self.ipsec_exist = True
        else:
            self.ipsec_exist = False
            print('Ipsec vpn is not found!')

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))
