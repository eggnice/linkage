#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import re
from linkage.op import baseFipinfosql


class Fip(object):
    def __init__(self, port_id):
        self.port_id = port_id
        ipinfo = baseFipinfosql.getFipinfo_by_port(self.port_id)
        if ipinfo:
            self.id = ipinfo[0].get('ID')
            self.name = ipinfo[0].get('NAME')
            self.proposer = ipinfo[0].get('PORPOSER')
            self.customer_id = ipinfo[0].get('CUSTOMER_ID')
            self.created_time = ipinfo[0].get('CREATED_TIME')
            self.is_delete = ipinfo[0].get('IS_DELETE')
            self.bandwidth_id = ipinfo[0].get('BANDWIDTH_ID')
            self.bandwidth_size = ipinfo[0].get('BANDWIDTH_SIZE')
            self.icp_status = ipinfo[0].get('ICP_STATUS')
            self.status = ipinfo[0].get('STATUS')
            self.modified = ipinfo[0].get('MODIFIED_TIME')
            self.fip_exist = True
        else:
            self.fip_exist = False

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))
