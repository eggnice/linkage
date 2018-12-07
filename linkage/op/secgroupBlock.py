#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from linkage.op import baseSecgroupinfosql


class SecGroup(object):
    def __init__(self, security_id):
        self.security_id = security_id
        sec, vm_host, sg_rule = baseSecgroupinfosql.getSecGroupinfo(self.security_id)

        if sec:
            self.name = sec[0].get('name')
            self.status = sec[0].get('status')
            self.sg_num = sec[0].get('sg_num')
            self.sg_num_used = sec[0].get('sg_num_used')
            self.proposer = sec[0].get('proposer')
            self.created_time = sec[0].get('created_time')
            self.vm_host = vm_host
            self.sg_rule = sg_rule
            self.sg_exist = True
        else:
            self.sg_exist = False

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))
