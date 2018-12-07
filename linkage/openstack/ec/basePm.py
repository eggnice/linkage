#!/usr/bin/env python
# coding=utf-8

"""
获取虚拟机的pm信息,输入参数应该包括pm_host（来源初始blockVM的信息）,实例化后的sshd
主要是通过ssh到虚拟机所在的主机，通过命令获取信息，包括管业存网卡、nova-computer和libvirt服务状态
"""

import re
from linkage import Utils


class basePm(object):
    def __init__(self, sshd, pm_host, instance_name):
        self.sshd = sshd
        self.instance_name = instance_name
        self.pm_info = {'pm_manage_ip': None, 'pm_store_ip': None, 'pm_service_ip': None, 'pm_nova_compute_state': None,
                        'pm_libvirtd_state': None, 'vm_qga_status': 'off', 'pm_host': pm_host}

    def __call__(self, *args, **kwargs):
        self.setPmInfo()
        return self.pm_info

    def setPmInfo(self):
        """ set_pm_info """
        ip_result_list = Utils.sshExeCmd(self.sshd, 'sudo ip addr')
        for row in ip_result_list:
            if row.strip().startswith('inet '):
                if 'bond0' in row:
                    self.pm_info['pm_manage_ip'] = re.split(r' |/', row.strip())[1]
                elif 'bond2' in row:
                    self.pm_info['pm_store_ip'] = re.split(r' |/', row.strip())[1]
                elif 'bond1' in row:
                    self.pm_info['pm_service_ip'] = re.split(r' |/', row.strip())[1]

        # 获取计算节点属性
        pm_nova_compute_result = Utils.sshExeCmd(
            self.sshd, 'sudo systemctl status openstack-nova-compute.service |grep "Active: active"')
        if not pm_nova_compute_result:
            # 如果属性为flase是旱，指定属性为not running,否则为running
            self.pm_info['pm_nova_compute_state'] = 'not running'
        else:
            self.pm_info['pm_nova_compute_state'] = 'running'

        # 获取libvirtd的属性
        pm_libvirtd_result = Utils.sshExeCmd(
            self.sshd, 'sudo systemctl status libvirtd.service |grep "Active: active"')
        if not pm_libvirtd_result:
            # 如果属性为flase是旱，指定属性为not running,否则为running
            self.pm_info['pm_libvirtd_state'] = 'not running'
        else:
            self.pm_info['pm_libvirtd_state'] = 'running'

        #获取虚拟qga进程属性
        pm_qga_result = Utils.sshExeCmd(
            self.sshd, 'sudo virsh qemu-agent-command %s \'{"execute": "guest-info"}\'' % self.instance_name
        )
        if pm_qga_result:
            self.pm_info['vm_qga_status'] = 'running'
