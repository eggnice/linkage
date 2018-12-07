#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from linkage.utils import utils
from linkage import opconfig


def getSecGroupinfo(security_id):
    sql1 = '''SELECT id,name,status,SECRULE_NUM sg_num,USED_SECRULE_NUM sg_num_used,proposer,created_time
                FROM openstack.os_biz_secgroup s
                where s.is_delete =0 and s.id ='%s' ''' % security_id
    sql2 = '''SELECT vm_host_id FROM openstack.os_biz_vm_secgroup_rel where SECGROUP_ID='%s' ''' % security_id
    sql3 = '''SELECT ID,PROTOCOL,DIP,DPORT,INOROUT,SIP,ETHER_TYPE FROM openstack.os_biz_secgroup_rule where
                is_delete=0 and secgroup_id='%s' ''' % security_id
    sec = utils.execsql(sql1, opconfig['OP_OPENSTACK_CONFIG'])
    vm_host = utils.execsql(sql2, opconfig['OP_OPENSTACK_CONFIG'])
    sec_rule = utils.execsql(sql3, opconfig['OP_OPENSTACK_CONFIG'])
    return sec, vm_host, sec_rule
