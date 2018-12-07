#!/usr/bin/env python
# coding=utf-8

"""
检查虚拟机自身的健康度，主要通过ssh方式去虚拟机所在的物理上执行命令检查对应的虚拟属性，
输入vm_id,pm_host,instance_name,sshd,fixed_ip_list
包括虚机自身5个文件是否存在，backing file是否存在，drbd是否正常，qemu是否正常，网卡信息是否正常
"""

from linkage import Utils as util


class baseSelfCheck(object):
    def __init__(self, uuid, pm_host, instance_name, fixed_ip_list, sshd):
        self.vm_id = uuid
        self.pm_host = pm_host
        self.fixed_ip_list = fixed_ip_list
        self.sshd = sshd
        self.vm_self_info = {}
        self.data = {'vm_id': uuid,'vm_name':instance_name,'pm_host':pm_host,
                     'files': None, 'fixed_ips': {},'drbd': False,
                     'qemu': False, 'backing_file': False}

    def __call__(self, *args, **kwargs):
        self.checkHostHealth()
        return self.data

    def checkHostHealth(self):
        """ check_host_health """
        # 判断虚机自身的5个文件是否齐全
        file_name = ['console.log', 'disk', 'disk.config',
                     'disk.info', 'libvirt.xml']
        result_ls_vmfile = util.sshExeCmd(
            self.sshd, 'sudo ls -l /var/lib/nova/instances/%s' % self.vm_id)
        self.data['files'] = {x: True if x in str(result_ls_vmfile) else False for x in file_name}

        # 判断虚机的backing file是否存在
        result_backing_file = util.sshExeCmd(
            self.sshd, 'sudo qemu-img info /var/lib/nova/instances/%s/disk' % self.vm_id)
        for line in result_backing_file:
            if 'backing file:' in line:
                self.data['backing_file'] = True

        # 判断drbd的状态是否正常
        result_drbd = util.sshExeCmd(self.sshd, 'sudo cat /proc/drbd')
        primary_secondary = False
        secondary_primary = False
        for line in result_drbd:
            if 'cs:Connected ro:Primary/Secondary ds:UpToDate/UpToDate' in line:
                primary_secondary = True
            if 'cs:Connected ro:Secondary/Primary ds:UpToDate/UpToDate' in line:
                secondary_primary = True
        if primary_secondary and secondary_primary:
            self.data['drbd'] = True

        # 判断虚机qemu的状态是否正常
        result_ps_qemu = util.sshExeCmd(
            self.sshd, 'sudo ps aux |grep %s |grep -v grep' % self.vm_id)
        if result_ps_qemu:
            self.data['qemu'] = True

        # 获取ovs-appctl vm/port-show的属性并匹配相关属性
        for port in self.fixed_ip_list:
            result_port_ip = util.sshExeCmd(
                self.sshd, "sudo ovs-appctl vm/port-show |grep %s | awk '{print $2}'" % port)
            # 当上面的执行结果有值且port属性为真且result_port_ip第一个值为真时，更新其属性值
            if result_port_ip and port in result_port_ip[0]:
                self.data['fixed_ips'][port] = True
            else:
                self.data['fixed_ips'][port] = False
