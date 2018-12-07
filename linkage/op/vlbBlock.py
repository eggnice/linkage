#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import re
from linkage.op import baseVlbinfosql


class Vlb(object):
    def __init__(self, vlb_id):
        self.vlb_id = vlb_id

        lbaas, listen = baseVlbinfosql.getVlbinfo(self.vlb_id)
        if lbaas:
            self.public_ip = lbaas[0].get('public_ip')
            self.subnet_id = lbaas[0].get('subnet_id')
            self.vip_port_id = lbaas[0].get('vip_port_id')
            self.name = lbaas[0].get('name')
            self.vlb_status = lbaas[0].get('vlb_status')
            self.vip = lbaas[0].get('vip')
            self.proposer = lbaas[0].get('proposer')
            self.created_time = lbaas[0].get('created_time')
            self.listen = listen
            self.vlb_exist = True
        else:
            self.vlb_exist = False

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))
