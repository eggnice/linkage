# *_* coding: utf-8 *_*
# _author: eggnice

import sys
from linkage.openstack.sdn.blockFloatingIp import blockFloatingIp
from linkage.openstack.sdn.baseNeutron import baseNeutron
from linkage.openstack.ec.baseIdentity import baseIdentity
from linkage.openstack.sdn.blockPort import blockPort

class builtArgs(object):
    def __init__(self):
        self.ip_type = {'VM': lambda :self.blockFloating.block_port.portdata.get('device_id'),
                        'LBVIP': lambda :self.out_lbvip(),
                        'HAVIP': lambda :self.out_havip()
                       }
	self.blockFloating = None

    def out_lbvip(self):
        """
        输出lbvip信息并退出
        """

    def out_havip(self):
        """
        输出havip信息并退出
        """

    def out_floating(self):
        """
        输出公网ip信息并退出
        """
        pass

    def floatingIp(self, floating_ip):
        """
        如果ip没挂载输出ip信息.判断挂载:VM(返回UUID),VLB(输出相关信息并退出),
        HAVIP(输出相关信息并退出)
        :param ip: str
        :return: UUID(str) or None
        """
        self.blockFloating = blockFloatingIp() #实例化blcok
        if self.blockFloating.init_floatingIp(floating_ip):
            if self.blockFloating.floatingipdata.get('port_id'):
                return self.ip_type[self.blockFloating.get_ip_type()]()
            else:
                self.out_floating() #此处需要完善,当公网Ip没有挂载的情况
        else:
            raise Exception('不存在该公网ip:%s' % floating_ip)

    def fixedIp(self, fixed_ip, user_name):
        """
        用户名下对应ip对应的VM数量如果为１返回UUID,大于1(存在vpc，输出相关信息)
        :param fixed_ip: str
        :param user_name: str
        :return: UUID or None
        """
        result = baseIdentity(user_name)
        if result:
            tenant_id = result.getTenant_id()
        else:
            raise Exception('该用户不存在:%s' % user_name)
        ports = baseNeutron.list_user_ports(fixed_ip, tenant_id)
        if len(ports) > 1:
            print '用户存在{0}个该私网ip:{1},请更换输入参数'.format(len(ports),fixed_ip)
            sys.exit(1)
        elif len(ports) == 1:
            self.blockPort = blockPort()
            self.blockPort.init_portId(ports[0])
            return self.ip_type[self.blockPort.get_port_type()]
        raise Exception('用户账户下私网ip不存在:%s/%s' % (user_name, fixed_ip))

builtArgs = builtArgs()
