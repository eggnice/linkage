# *_* coding: utf-8 *_* 
# __author__: eggnice
"""此对象主要是调用底层api进行数据传递,并且判断数据,如果数据为空抛出异常"""

import re
from linkage.openstack import neutronApi
from linkage.exceptions import ReturnNone

class baseNeutron(object):
    def __init__(self):
        pass

    @staticmethod
    def floating_listIps(floatingIp):
        """
        通过/floating?floating_ip_address=x获取对应ip的信息
        :param floatingIp: 公网ip
        :return: dict or None
        """
        result = neutronApi.floatingips_listIps(floating_ip_address=floatingIp).get('floatingips')
        return result[0] if result else None

    @staticmethod 
    def listVmPorts(device_id, tenant_id):
        """
        通过vm的uuid和用户id获取该vm上的ports_id
        :param device_id: vm uuid
        :param tenant_id: tenant_id
        :return: list [{subnet_id:xx,id: xx,ip:xx},]
        """
        data = []
        result = neutronApi.port_listPort(userTenantId=tenant_id, device_id=device_id).get('ports')
        if result:
            for onePort in result:
                one = {}
                one['subnet_id'] = onePort['fixed_ips'][0]['subnet_id']
                one['ip'] = onePort['fixed_ips'][0]['ip_address']
                one['id'] = onePort['id']
                data.append(one)
            return data
        raise ReturnNone('get vm port return None')

    @staticmethod
    def getSecurity_group(group_id):
        """
        调用/v2.0/security-groups 返回信息
        :param group_id: string
        :return: dict {name:xx,security_group:{},}
        """
        result = neutronApi.security_showGroups(group_id, fields=['name','security_group_rules'])
        if result.get('security_group'):
            return result.get('security_group')

    @staticmethod
    def getSub_name(subnet_id):
        """
        根据subnet_id 返回subnet_name
        :param subnet_id:
        :return: tuple(name, cidr)
        """
        result = neutronApi.subnets_showDetails(subnet_id, fields=['name', 'cidr']).get('subnet')
        if result:
            return result.get('name'), result.get('cidr')
        raise ReturnNone('get subnet:%s return none' % subnet_id)

    @staticmethod
    def getPort(port_id):
        """
        根据port_id 调用/v2.0/ports/{port_id}
        :param port_id: string
        :return: result:json
        """
        try:
            return neutronApi.port_showDetails(port_id).get('port')
        except Exception, e:
            if re.compile(r'Port .*? could not be found').search(str(e)):
                raise ReturnNone('Return None')

    @staticmethod
    def port_listPort(net_id, ip):
        """
        列出全部network_id的port,找到对应公网ip对应的port
        :param net_id:
        :param ip:
        :return: string:port_id or None
        """
        result = neutronApi.port_listPort(network_id=net_id, fields=['id', 'fixed_ips'])
        for one in result.get('ports'):
            if one['fixed_ips'][0]['ip_address'] == ip:
                return one['id']
        return None

    @staticmethod
    def getQos(qos_id):
        """
        /v2.0/qoses/[qos_id]返回qos_id对应的信息
        :param qos_id: string
        :return: dict
        """
        return neutronApi.qoses_showDosPoliciesDetails(qos_id).get('qos')

    @staticmethod
    def list_user_ports(fixed_ip, tenant_id):
	result = neutronApi.port_listPort(tenant_id=tenant_id)
        vm_name = []
        ports = []
        for one in result.get('ports'):
            if one['fixed_ips'][0]['ip_address'] == fixed_ip:
                vm_name = one['name']
        for one in result.get('ports'):
            if one['name'] == vm_name:
		ports.append(one['id'])
        return ports


     
