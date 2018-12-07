#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from linkage.utils import utils
from linkage import opconfig


def getVlbinfo(vlb_id):
    sql1 = '''SELECT id vlb_id, name, status vlb_status, proposer, private_ip vip, public_ip, subnet_id,
              vip_port_id, created_time FROM openstack.os_biz_lbaas_loadbalance WHERE
              id = '%s' AND is_delete = 0 ''' % vlb_id
    sql2 = '''SELECT name lb_listen_name,PROTOCOL,PROTOCOL_PORT,LB_ALGORITHM,lm.ip,lm.PORT,lm.status,
    lm.vm_host_id,lm.type FROM openstack.os_biz_lbaas_listener ll LEFT JOIN os_biz_lbaas_member lm ON
    ll.pool_id = lm.pool_id WHERE ll.LOADBALANCE_ID = '%s' AND ll.is_delete = 0''' % vlb_id

    lbaas = utils.execsql(sql1, opconfig['OP_OPENSTACK_CONFIG'])
    listen = utils.execsql(sql2, opconfig['OP_OPENSTACK_CONFIG'])
    return lbaas, listen
