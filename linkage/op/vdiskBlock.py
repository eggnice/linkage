#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import re
from linkage.op import baseVdiskinfosql


class Vdisk(object):
    def __init__(self, id):
        self.id = id

        vdiskinfo = baseVdiskinfosql.getVdiskinfo(self.id)

        if vdiskinfo:
            self.name = vdiskinfo[0].get('name')
            self.size = vdiskinfo[0].get('size')
            self.host_id = vdiskinfo[0].get('host_id')
            self.type = vdiskinfo[0].get('type')
            self.created_time = vdiskinfo[0].get('created_time')
            self.proposer = vdiskinfo[0].get('proposer')
            self.vdisk_exist = True
        else:
            self.vdisk_exist = False

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))
