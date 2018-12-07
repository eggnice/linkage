#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from linkage.utils import utils
from linkage import opconfig


def getVdiskinfo(id):
    sql1 = '''SELECT id,name,size,host_id,volume_type type,created_time,proposer,status FROM openstack.os_biz_ebs
                where id = '%s' and is_delete=0''' % id
    vdiskinfo = utils.execsql(sql1, opconfig['OP_OPENSTACK_CONFIG'])
    return vdiskinfo
