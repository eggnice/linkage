#!/usr/bin/python
# coding=utf-8

import re
from linkage.op import basePortinfosql


class Port(object):
    def __init__(self, resource_id):
        self.resource_id = resource_id
        portinfo = basePortinfosql.getPortInfo(self.resource_id)
        if portinfo:
            self.port_num = len(portinfo)
            self.port_list = portinfo
            self.port_exist = True
        else:
            self.port_exist = False
            print("'资源' %s: '未绑定端口'" % resource_id)

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))
