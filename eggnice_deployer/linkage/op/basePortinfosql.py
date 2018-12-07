#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from linkage.utils import utils
from linkage import opconfig


def getPortInfo(resource_id):
    sql1 = '''SELECT ID, `NAME`, CASE `STATUS` WHEN 0 THEN '绑定公网IP' WHEN 1 THEN '未绑定公网IP' ELSE 'UNDEFINED'
    END AS 'STATUS', MAC_ADDRESS, PRIVATE_IP, NETWORK_ID, SUBNET_ID, RESOURCE_ID, PROPOSER, CUSTOMER_ID, POOL_ID,
    CREATED_BY, CREATED_TIME, CASE IS_BASIC WHEN 0 THEN '私有网络' WHEN 1 THEN '基础网络' ELSE 'UNDEFINED'
    END AS 'IS_BASIC', CASE SOURCE WHEN 0 THEN '单独创建' WHEN 1 THEN '一体化订购' ELSE 'UNDEFINED' END AS 'SOURCE',
    IS_DELETE FROM os_biz_port_vm_attach WHERE RESOURCE_ID  = '%s' ''' % resource_id
    portinfo = utils.execsql(sql1, opconfig['OP_OPENSTACK_CONFIG'])
    return portinfo
