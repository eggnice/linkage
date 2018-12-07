#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from linkage.utils import utils
from linkage import opconfig


def getVMInfo(vm_id):
    sql1 = '''SELECT ID, `NAME`, VCPU, VMEMORY, VDISK, HW_HOST_ID, CASE `STATUS` WHEN 1 THEN 'ACTIVE' WHEN 2 THEN
    'BUILD' WHEN 3 THEN 'REBUILD' WHEN 4 THEN 'SUSPENDED' WHEN 5 THEN 'PAUSED' WHEN 6 THEN 'RESIZE' WHEN 7 THEN
    'VERIFY_RESIZE' WHEN 8 THEN 'REVERT_RESIZE' WHEN 9 THEN 'PASSWORD' WHEN 10 THEN 'REBOOT' WHEN 11 THEN 'HARD_REBOOT'
    WHEN 12 THEN 'DELETED' WHEN 13 THEN 'UNKNOWN' WHEN 14 THEN 'ERROR' WHEN 15 THEN 'STOPPED' WHEN 16 THEN 'SHUTOFF'
    WHEN 17 THEN 'MIGRATING' WHEN 18 THEN 'SHELVED' ELSE 'UNDEFINED' END AS 'STATUS', IMAGE_NAME, IMAGE_REF,
    FLAVOR_NAME, FLAVOR_REF, TASK, CASE OPERATION_FLAG WHEN 0 THEN '重装' WHEN 1 THEN '备份恢复' ELSE 'UNDEFINED'
    END AS 'OPERATION_FLAG', PROPOSER, CUSTOMER_ID, POOL_ID, CREATED_BY, CREATED_TIME, MODIFIED_BY, MODIFIED_TIME,
    PWD, IS_DELETE, AVAILABILITY_ZONE FROM os_biz_vm_host WHERE id = '%s' ''' % vm_id
    vminfo = utils.execsql(sql1, opconfig['OP_OPENSTACK_CONFIG'])
    return vminfo