#!/usr/bin/python
# coding=utf-8

import re
from linkage.op import baseVminfosql


class Vm(object):
    def __init__(self, vm_id):
        self.vm_id = vm_id
        vminfo = baseVminfosql.getVMInfo(self.vm_id)
        if vminfo:
            self.name = vminfo[0].get('NAME')
            self.vcpu = vminfo[0].get('VCPU')
            self.vmemory = vminfo[0].get('VMEMORY')
            self.vdisk = vminfo[0].get('VDISK')
            self.hw_host_id = vminfo[0].get('HW_HOST_ID')
            self.status = vminfo[0].get('STATUS')
            self.image_name = vminfo[0].get('IMAGE_NAME')
            self.image_ref = vminfo[0].get('IMAGE_REF')
            self.flavor_name = vminfo[0].get('FLAVOR_NAME')
            self.flavor_ref = vminfo[0].get('FLAVOR_REF')
            self.tack = vminfo[0].get('TASK')
            self.operation_flag = vminfo[0].get('OPERATION_FLAG')
            self.proposer = vminfo[0].get('PROPOSER')
            self.customer_id = vminfo[0].get('CUSTOMER_ID')
            self.pool_id = vminfo[0].get('POOL_ID')
            self.created_by = vminfo[0].get('CREATED_BY')
            self.created_time = vminfo[0].get('CREATED_TIME')
            self.modified_by = vminfo[0].get('MODIFIED_BY')
            self.modified_time = vminfo[0].get('MODIFIED_TIME')
            self.pwd = vminfo[0].get('PWD')
            self.is_delete = vminfo[0].get('IS_DELETE')
            self.availability_zone = vminfo[0].get('AVAILABILITY_ZONE')
            self.vm_exist = True
        else:
            self.vm_exist = False
            print('Vm is not exist!')

    def __str__(self):
        for key in dir(self):
            if re.findall('^set', key) or re.findall('^__', key):
                continue
            else:
                print('%s: %s' % (key, eval('self.' + key)))
