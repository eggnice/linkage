#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from linkage.utils import utils
from linkage import opconfig


def getVfwinfo(proposer):
    sql1 = '''SELECT id, status, proposer, created_time,f.fw_policy_num policy_num from os_biz_fw f WHERE
              (proposer = '%s' or id = '%s') AND is_delete = 0 ''' % (proposer, proposer)
    sql2 = '''SELECT ID,NAME,SIP,SPORT,DIP,DPORT,PROTOCOL,ACCESS,STATUS,CREATED_TIME,PROPOSER FROM
              openstack.os_biz_fw_rule where is_delete=0 and proposer='%s' ''' % proposer

    fw = utils.execsql(sql1, opconfig['OP_OPENSTACK_CONFIG'])
    fw_rule = utils.execsql(sql2, opconfig['OP_OPENSTACK_CONFIG'])
    return fw, fw_rule
