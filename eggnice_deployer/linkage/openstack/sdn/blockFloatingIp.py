# *_* coding: utf-8 *_*
# __author__: eggnice

from linkage import  loggers
from linkage.exceptions import (LogicError, ReturnNone, InitFloatingIpError)
from linkage.openstack.sdn.baseNeutron import baseNeutron
from linkage.openstack.sdn.blockPort import blockPort

class blockFloatingIp(object):
    def __init__(self):
        """
        针对floatingIp进行相关实例化
        """
        self.ip = ''
        self.ip_id = ''
        self.qosdata = {}
        self.block_port = ''
        self.floatingipdata = {}

    def _write(self, result):
        if result:
            self.ip = result.get('floating_ip_address')
            self.ip_id = result.get('id')
            self.floatingipdata = result

    def init_floatingIp(self, ip):
        """
        :param floatingip: use publicIp to request data
        :return: dict None
        """
        try:
            result = baseNeutron.floating_listIps(ip)
            self._write(result)
            return self.floatingipdata
        except Exception, e:
            loggers.error('init public error:%s' % str(e))
            raise InitFloatingIpError('init public error:%s' % str(e))

    def init_floatingId(self, ip_id):
        pass

    def get_FixedPort_info(self):
        """
        if the ip mount add port message
        :return: json or None(not mount)
        """
        try:
            if self.floatingipdata.get('port_id'):
                self.block_port = blockPort()
                result = self.block_port.init_portId(self.floatingipdata.get('port_id'))
                if result:
                    return self.block_port.portdata
                else:
                    raise Exception('get fixed_port data return None')
            else:
                return None
        except Exception, e:
            pass

    def get_ip_type(self):
        """
        ipTypes:vm, vlb, havip
        :return: string:'VM' or 'VLB' or 'HAVIP'
        """
        if not self.block_port:
            self.get_FixedPort_info()
            return self.block_port.get_port_type()

    def getvmId(self):
        """
        if ip mount object is vm return devece_id(vm_uuid)
        :return: string or None
        """
        if self.get_ipType() == 'VM':
            return self.block_port.portdata.get('device_id')

    def get_umont_data(self):
        pass

    def get_lbvip_data(self):
        pass
    
    def get_havip_data(self):
        pass

    def getqos_info(self): #耗时比较长待优化
        """
        通过list所有port得到floatingIp的外网port,通过该port得到相应的qos_id,调用qoses得到qos_info
        :return: dict:{}
        """
        try:
            port_id = baseNeutron.port_listPort(self.floatingipdata['floating_network_id'],
                                            self.floatingipdata['floating_ip_address'])
            if not port_id:
                raise LogicError('get floating ip has not port_id, logic error')
            self.qosdata['floating_port_id'] = port_id
            qos_id = baseNeutron.getPort(port_id).get('qos')
            self.qosdata['qos_id'] = qos_id
            if not qos_id:
                return self.qosdata
            data = baseNeutron.getQos(qos_id)
            self.qosdata['type'] = data.get('type')
            self.qosdata['policies'] = data.get('policies')
            return self.qosdata
        except Exception, e:
            loggers.error('get qos error:%s' % str(e.args))


