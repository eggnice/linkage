#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import re
from linkage.op import baseVfwinfosql


class Vfw(object):
    def __init__(self, proposer):
        self.proposer = proposer

        fw, fw_rule = baseVfwinfosql.getVfwinfo(self.proposer)
        if fw:
            self.id = fw[0].get('id')
            self.proposer = fw[0].get('proposer')
            self.status = fw[0].get('status')
            self.created_time = fw[0].get('created_time')
            self.policy_num = fw[0].get('policy_num')
            self.vfw_exist = True
            self.fw_rule = fw_rule
        else:
            self.vfw_exist = False

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))
