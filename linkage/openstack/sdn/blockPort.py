# *_* coding: utf-8 *_*
# __author__: eggnice
from linkage import loggers
from linkage.exceptions import (LogicError, ReturnNone, InitFloatingIpError)
from linkage.openstack.sdn.baseNeutron import baseNeutron
from linkage.exceptions import ReturnNone


class blockPort(object):
    """
    针对端口实例化对象
    """
    def __init__(self):
        """
        通过port_id实例化对象
        :param port_id:string
        :param oneport:dict {ip:xx, sub_name:xx,sub_id:xx,cidr:xx}
        """
        self.port_id = ''
        self.portdata = '' 

    def _write(self, result):
        self.portdata = result

    def init_portId(self, port_id):
        """
        初始化port的detail数据,写入实例
        :param port_id: 端口号
        :return: json or raise ReturnNone
        """
        try:
            self._write(baseNeutron.getPort(port_id))
            return self.portdata
        except ReturnNone, e:
            return None

    def getSecurityRules(self):
        """
        返回该网卡上的安全组信息(必有信息)
        :return: list [{name:xx,security_group:{}},]
        """
        groupslist = self.portdata['security_groups']
        return [baseNeutron.getSecurity_group(one_group) for one_group in groupslist]

    def get_port_type(self):
        try:
            if self.portdata.get('device_id'):
                return 'VM'
            elif self.portdata['name'] and self.portdata['name'].startswith('loadbalancer'):
                return 'LBVIP'
            else:
                return 'HAVIP'
            raise Exception('对ip分类(vm,lbvip,havip)有问题')
        except Exception, e:
            loggers.error(str(e))
            raise LogicError(str(e))



