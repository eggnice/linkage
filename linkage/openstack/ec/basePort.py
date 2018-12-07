# *_* coding=utf-8 *_*
# _author_: eggnice

"""
获取vm网卡信息
"""

from linkage.openstack.sdn.baseNeutron import baseNeutron
from linkage.openstack.sdn.blockPort import blockPort


class basePort(object):
    def __init__(self, one_port_mess):
        "{id:xx,ip:xx,subnet_name:xx,subnet_id:xx,cidr:xx,security_groups:xx,qos:xx}"
        self.port_id = one_port_mess['id']
        self.data = one_port_mess

    def __call__(self, *args, **kwargs):
        self.getPortInfo()
        return self.data

    def getPortInfo(self):
        """
        通过实例化snd的port模块获取port_id属性
        """
        self.data['subnet_name'], self.data['cidr'] = baseNeutron.getSub_name(self.data['subnet_id'])
        port = blockPort()
        port. init_portId(self.port_id)
        self.data['security_groups'] = port.getSecurityRules()
        self.data['qos'] = port.portdata.get('qos', False)

