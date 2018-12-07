# *_* coding: utf-8 *_*
# __author__: eggnice

from linkage import Utils
from linkage import ecconfig
from linkage import loggers
from linkage.openstack.ec.basePm import basePm
from linkage.openstack.ec.baseOp import baseOp
from linkage.openstack.ec.baseVolume import baseVolume
from linkage.openstack.ec.baseImage import baseImage
from linkage.openstack.ec.basePort import basePort
from linkage.openstack.ec.baseFloatingIp import baseFloatingIp
from linkage.openstack.ec.baseSelfCheck import baseSelfCheck
from linkage.openstack.ec.baseAction import baseAction
from linkage.openstack.ec.baseCinder import baseCinder
from linkage.openstack.ec.baseVnc import baseVnc
from linkage.openstack.ec.baseFlavor import baseFlavor
from linkage.openstack.ec.baseNova import baseNova
from linkage.openstack.ec.baseIdentity import baseIdentity
from linkage.openstack.sdn.baseNeutron import baseNeutron
from linkage.exceptions import (GetPmInfoError, LogicError, GetUserInfoError, ReturnNone,
                                GetPortInfoError,  GetVolumeInfoError, GetImageInfoError,
                                GetSelfCheckInfoError, GetFloatingIpInfoError, GetActionInfoError,
                                GetVncInfoError, GetFlavorInfoError)

class blockVm(object):
    "one Vm instance self.data: {'vm': {}}"
    def __init__(self):
        self.uuid = ''
        self.pm_host = ''
        self.user = ''
        self.instance_name = ''
        self.sshd = ''
        self.originalImage_id = ''
        self.domain_name = ''
        self.system_disk_type = ''
        self.volumes = []
        self.floatingips = {}
        self.vmdata = {}
        self.pmdata = {}
        self.checkdata = {}
        self.portdata = []
        self.volumesdata = []
        self.imagesdata = []
        self.opdata = {}
    
   # def __del__(self):
   #     print '*******have call __del__'
   #     self.sshd.close()

    def init_usip(self, fixed_id, user_id): #需要优化的问题,用户加私网ip无法确认一台vm存在两个vpc情况
        """
        用私网ip和用户id初始化该实例数据
        :param fixed_id: private_ip bond on vm
        :param user_id: private_ip user
        :return: json or None
        """
        try:
            self.data = {}
            result = baseNova.getServerByIp(fixed_id, user_id)
            self._write(result.get('servers')[0])
            return result.get('servers')[0]
        except Exception, e:
            raise LogicError('init blockvm error:%s' % str(e))

    def init_uuid(self, uuid):
        """
        用虚拟机的uuid初始化该实例数据
        :param uuid:
        :return: json or None
        """
        try:
            result = baseNova.getServerById(uuid=uuid)
	    self._write(result)
	    return result
        except ReturnNone:
            return None
        except Exception, e:
            loggers.error('init vm instance error:%s' % str(e))
            raise LogicError('init vm instance error:%s' % str(e))

    def _write(self, result):
        """
        针对调用api返回的结果进行提取几个重要信息
        return: None
        """
        self.uuid = result.get('id')
        self.pm_host = result.get('OS-EXT-SRV-ATTR:host')
        self.user_id = result.get('user_id')
        self.instance_name = result.get('name')
        if result['image']:
	    self.originalImage_id = result.get('image').get('id')
            self.system_disk_type = '本地盘'
        else:
            self.system_disk_type = '云硬盘'
            ebs_volume_id = result['os-extended-volumes:volumes_attached'].pop(0).get('id')
            self.ebs_system_data = baseCinder.volume_idToDetail(ebs_volume_id)
            self.originalImage_id = self.ebs_system_data['volume_image_metadata']['image_id']
	self.volumes = result.get('os-extended-volumes:volumes_attached')
        self.domain_name = result.get('OS-EXT-SRV-ATTR:instance_name')
        self.sshd = self._getPm_sshd()
        self.ports, self.floatingips = self._getIps(result)
        result['system_disk_type'] = self.system_disk_type 
        self.vmdata = result

    def _getPm_sshd(self):
        """
        返回sshd的句柄
        :return: sshd对象
        """
        sshd = Utils.sshConnect(self.pm_host, ecconfig['PM_USER'], ecconfig['PM_PASSWORD'], int(ecconfig['PM_PORT']))
        return sshd

    def _getIps(self, result):
        """
        获取云主机私网信息
        :param result: vm detail
        :return: tuple ({subnet: ip},{})
        """
        ports = {}
        public_ips = {}
        if result.get('addresses'):
            for subnet, v in result.get('addresses').items():
                for car in v:
                    if car['OS-EXT-IPS:type'] == 'floating':
                        public_ips[subnet] = car['addr']
                    elif car['OS-EXT-IPS:type'] == 'fixed':
                        ports[subnet] = car['addr']
            return ports, public_ips
        else:
            raise LogicError('vm has not base network,logic error')

    @property
    def getPm_info(self):
        """
        查询云主机物理机信息(必有信息)
        :return: dict
        """
        if self.pm_host:
            try:
                pm = basePm(self.sshd, self.pm_host, self.domain_name)
                self.pmdata =  pm()
                return self.pmdata
            except Exception, e:
                raise GetPmInfoError('get pm info error:%s' % str(e))
        raise LogicError('vm can not find pm, logic error')

    @property
    def getOp_info(self): #user 信息有待完善
        """
        获取云主机op侧用户信息和订单信息(必有信息)
        :return: dict {user:xx, order:xx, action:xx}
        """
        if self.user_id:
	    try:
		self.opdata = baseOp(self.user_id, self.uuid)()
                return self.opdata
            except Exception, e:
                raise GetUserInfoError('get op info error:%s' %str(e))
        raise LogicError('vm can not find op user, logic error')

    @property
    def getPort_info(self):
        """
        获取云私网信息(必有信息)
        :return: list: [{},]
        """
        data = []
        try:
            if self.ports:
                ports = baseNeutron.listVmPorts(self.uuid, self.vmdata.get('tenant_id'))
                for one in ports:
                    data.append(basePort(one)())
                self.portdata = data
                return self.portdata
            else:
                raise LogicError('vm has not port info, logic error')
        except Exception, e:
            raise GetPortInfoError('get port info error:%s' % str(e))

    @property
    def getVolume_info(self):
        """
        获取云主机挂在卷信息(可选信息)
        :return:list [{},], None
        """
        try:
            self.volumesdata = [one() for one in [baseVolume(one['id']) for one in
                                            self.volumes if self.volumes]]
            return self.volumesdata
        except Exception, e:
            raise GetVolumeInfoError('get volume info error:%s' % str(e))

    @property
    def getImage_info(self):
        """
        获取云主机快照信息(可选信息)
        :return: list:[{},] or None
        """
        try:
            self.imagesdata = baseImage(self.uuid, self.originalImage_id)()
            return self.imagesdata
        except Exception, e:
            raise GetImageInfoError('get image error:%s' %str(e))

    @property
    def getCheck_info(self):
        """
        登录所在物理机获取云主机相关检查信息
        :return: dict or None
        """
        try:

           self.checkdata = baseSelfCheck(self.uuid, self.pm_host, self.instance_name,
                                          self.ports.values(), self.sshd)()
           if self.system_disk_type == '云硬盘':
               self.checkdata['backing_file'] = 'ebs系统盘不需要检查该项'
           return self.checkdata
        except Exception, e:
            raise GetSelfCheckInfoError('get check_info error:%s' %str(e))

    @property
    def getFloatingIp_info(self):
        """
        获取云主机挂载公网ip信息(可选信息)
        :return: list: [{},] or None
        """
        try:
            self.floatingipdata = [baseFloatingIp(ip)() for ip in self.floatingips.values()]
            return self.floatingipdata
        except Exception, e:
            loggers.error('get floating ip message error:%s' % str(e))
            raise GetFloatingIpInfoError('get floating ip message error:%s' % str(e))

    @property
    def getAction_info(self):
        """
        获取云主机的操作信息
        """
        try:
            self.actiondata = baseAction(self.uuid)()
            return self.actiondata
        except Exception, e:
            loggers.error('get action info error:%s' % str(e))
            raise GetActionInfoError('get action info error:%s' % str(e))

    @property
    def getVncUrl(self):
        """
        获取云主机的vnc登录url
        """
        try:
            self.vncdata = baseVnc(self.uuid)()
            return self.vncdata
        except Exception, e:
            loggers.error('get vnc info error:%s' % str(e))
            raise GetVncInfoError('get vnc info error:%s' % str(e))

    @property
    def getFlavor_info(self):
        """
        获取云主机规格信息
        :return: dist or None
        """
        try:
            if self.vmdata:
                self.flavordata = baseFlavor(self.vmdata['flavor']['id'])()
		if self.system_disk_type == '云硬盘':
                    self.flavordata['disk'] = self.ebs_system_data['size']
                return self.flavordata
        except Exception, e:
            loggers.error('get flavor info error:%s' % str(e))
            raise GetFlavorInfoError('get flavor info error:%s' % str(e))

