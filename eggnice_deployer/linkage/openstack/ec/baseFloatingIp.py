# *_* coding: utf-8 *_*
# _author_: utf-8

"""
获取虚拟机vm的公网ip的信息
主要通过sdn的public ip 类获取公网状况信息
"""

from linkage.openstack.sdn.blockFloatingIp import blockFloatingIp


class baseFloatingIp(object):
    def __init__(self, ip):
        self.ip = ip
        self.data = ''

    def __call__(self, *args, **kwargs):
        """返回dict{qos_id:x,qos_policies:x,qos_type:x,floating_port_id:x} + data"""
        self.getIp_info()
        return self.data

    def getIp_info(self):
        """
        获取信息
        """
        floating = blockFloatingIp()
        floating.init_floatingIp(self.ip)
        self.data = floating.floatingipdata
        self.data.update(floating.getqos_info())

