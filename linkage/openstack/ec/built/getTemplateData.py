# -*- coding: utf-8 -*-
"""
__mktime__ = '2018/7/3'
__author__ = 'dengyuxian'
__filename__ = 'getTemplateData'
"""
import sys
from linkage.openstack.ec.tools import tools


class getTemplateData(object):
    def __init__(self, bv_inst):
        self.bv = bv_inst

    def extract_data(self, tmp, keys, i):
        """
        根据key值提取dict的value
        :param tmp:  要提取的json
        :param keys: key值
        :param i: 如果tmp是list，i是提取的位置
        :return: value
        """
        try:
            keys = keys.split('/')
            for k in keys:
                if isinstance(tmp, dict):
                    v = tmp.get(k)
                elif isinstance(tmp, list):
                    v = tmp[i].get(k)
                else:
                    return 'None'
                tmp = v
        except ValueError as e:
            print str(e.args)
            return 'None'
        return tmp

    def get_actiondata(self):
        """
        云主机的操作信息，一定会存在crate云主机的信息
        :return: list，只有一层list
        """
        result = list()
        result1 = list()
        tmp = self.bv.getAction_info
        for i in range(len(tmp)):
            value1 = self.extract_data(tmp, 'request_id', i)
            value10 = self.extract_data(tmp, 'action', i)
            value11 = self.extract_data(tmp, 'start_time', i)
            if value11 is not 'None':
                value11 = tools.utctime_to_local(str(value11))
            value12 = self.extract_data(tmp, 'message', i)
            var = locals()
            result1 = [var[key] for key in sorted(var) if key.startswith('value')]
            result.append(result1)
            result1 = []
        tools.str_to_unicode(result)
        return result

    def get_checkdata(self):
        result = list()
        result1 = list()
        result2 = list()
        tmp = self.bv.getCheck_info
        value1 = self.extract_data(tmp, 'qemu', 0)
        result.append(value1)
        for v, k in tmp.get('fixed_ips').items():
            value10 = v
            value11 = k
            result1.append([value10, value11])
        value12 = self.extract_data(tmp, 'files/console.log', 0)
        value13 = self.extract_data(tmp, 'files/disk.config', 0)
        value14 = self.extract_data(tmp, 'files/disk', 0)
        value15 = self.extract_data(tmp, 'files/disk.info', 0)
        value16 = self.extract_data(tmp, 'files/libvirt.xml', 0)
        value17 = self.extract_data(tmp, 'backing_file', 0)
        var = locals()
        result2 = [var[key] for key in sorted(var) if key.startswith('value')][3:]
        result.append(result1)
        result.append(result2)
        tools.str_to_unicode(result)
        return result

    def get_imagedata(self):
        result = list()
        result1 = list()
        result2 = list()
        result3 = list()
        result4 = list()
        result5 = list()
        tmp = self.bv.getImage_info
        value1 = self.extract_data(tmp, 'id', 0)
        value11 = self.extract_data(tmp, 'name', 0)
        value12 = self.extract_data(tmp, 'status', 0)
        value13 = self.extract_data(tmp, 'image.os_type', 0)
        value14 = self.extract_data(tmp, 'os_distro', 0)
        value15 = self.extract_data(tmp, 'size', 0)
        value16 = self.extract_data(tmp, 'created_at', 0)
        if value16 is not 'None':    
            value16 = tools.utctime_to_local(str(value16))
        value17 = self.extract_data(tmp, 'updated_at', 0)
        if value17 is not 'None':
            value17 = tools.utctime_to_local(str(value17))
        var1 = locals()
        result1 = [var1[key] for key in sorted(var1) if key.startswith('value')]
        for i in range(1, len(tmp)):
            if tmp[i].get('image_type') == 'backup':
                value2 = self.extract_data(tmp, 'id', i)
                value20 = self.extract_data(tmp, 'name', i)
                value21 = self.extract_data(tmp, 'status', i)
                value22 = self.extract_data(tmp, 'size', i)
                value23 = self.extract_data(tmp, 'base_image_ref', i)
                value24 = self.extract_data(tmp, 'created_at', i)
                if value24 is not 'None':
                    value24 = tools.utctime_to_local(str(value24))
                value25 = self.extract_data(tmp, 'updated_at', i)
                if value25 is not 'None':
                    value25 = tools.utctime_to_local(str(value25))
                var2 = locals()
                result2 = [var2[key] for key in sorted(var2) if key.startswith('value')][8:]
                result3.append(result2)
                result2 = []
            elif tmp[i].get('image_type') == 'snapshot':
                value2 = self.extract_data(tmp, 'id', i)
                value20 = self.extract_data(tmp, 'name', i)
                value21 = self.extract_data(tmp, 'status', i)
                value22 = self.extract_data(tmp, 'size', i)
                value23 = self.extract_data(tmp, 'base_image_ref', i)
                value24 = self.extract_data(tmp, 'created_at', i)
                if value24 is not 'None':
                    value24 = tools.utctime_to_local(str(value24))
                value25 = self.extract_data(tmp, 'updated_at', i)
                if value25 is not 'None':
                    value25 = tools.utctime_to_local(str(value25))
                var3 = locals()
                result4 = [var3[key] for key in sorted(var3) if key.startswith('value')][8:]
                result5.append(result4)
                result4 = []
        if len(result3) == 0:
            result3.append(['None'])
        if len(result5) == 0:
            result5.append(['None'])
        result.append(result1)
        result.append(result3)
        result.append(result5)
        tools.str_to_unicode(result)
        return result

    def get_networkdata(self):
        result = list()
        result1 = list()
        result2 = list()
        result3 = list()
        result4 = list()
        result5 = list()
        result6 = list()
        tmp1 = self.bv.getPort_info
        tmp2 = self.bv.getFloatingIp_info
        for i in range(len(tmp1)):
            value1 = self.extract_data(tmp1, 'id', i)
            value10 = self.extract_data(tmp1, 'ip', i)
            value11 = self.extract_data(tmp1, 'cidr', i)
            value12 = self.extract_data(tmp1, 'qos', i)
            value13 = self.extract_data(tmp1, 'subnet_id', i)
            value14 = self.extract_data(tmp1, 'subnet_name', i)
            var1 = locals()
            result1 = [var1[key] for key in sorted(var1) if key.startswith('value')][:6]
            for ii in range(len(tmp2)):
                if tmp2[ii].get('port_id') == tmp1[i].get('id'):
                    value2 = self.extract_data(tmp2, 'id', ii)
                    value20 = self.extract_data(tmp2, 'floating_ip_address', ii)
                    value21 = self.extract_data(tmp2, 'status', ii)
                    value22 = self.extract_data(tmp2, 'type', ii)
                    value23 = self.extract_data(tmp2, 'policies/ratelimit', ii)
                    value24 = self.extract_data(tmp2, 'router_id', ii)
                    value25 = self.extract_data(tmp2, 'floating_port_id', ii)
                    value26 = self.extract_data(tmp2, 'floating_network_id', ii)
                    var2 = locals()
                    result2 = [var2[key] for key in sorted(var2) if key.startswith('value')][6:]
            if len(result2) == 0:
                result2 = ['None']
            for j in range(len(tmp1[i].get('security_groups'))):
                value3 = self.extract_data(tmp1[i].get('security_groups'), 'security_group_rules/security_group_id', j)
                value30 = self.extract_data(tmp1[i].get('security_groups'), 'name', j)
                result3.append(value3)
                result3.append(value30)
                for k in range(len(tmp1[i].get('security_groups')[j].get('security_group_rules'))):
                    value4 = self.extract_data(tmp1[i].get('security_groups')[j].get('security_group_rules'), 'id', k)
                    value40 = self.extract_data(tmp1[i].get('security_groups')[j].get('security_group_rules'), 'direction', k)
                    value41 = self.extract_data(tmp1[i].get('security_groups')[j].get('security_group_rules'), 'protocol', k)
                    port_min = self.extract_data(tmp1[i].get('security_groups')[j].get('security_group_rules'), 'port_range_min', k)
                    port_max = self.extract_data(tmp1[i].get('security_groups')[j].get('security_group_rules'), 'port_range_max', k)
                    if port_min == port_max:
                        value42 = port_min    
                    else:
                        value42 = str(port_min) + '~' + str(port_max)
                    value43 = self.extract_data(tmp1[i].get('security_groups')[j].get('security_group_rules'), 'remote_ip_prefix', k)
                    value44 = self.extract_data(tmp1[i].get('security_groups')[j].get('security_group_rules'), 'ethertype', k)
                    var3 = locals()
                    result5 = [var3[key] for key in sorted(var3) if key.startswith('value')][-6:]
                    result6.append(result5)
                    result5 = []
                if len(tmp1[i].get('security_groups')[j].get('security_group_rules')) == 0:
                    result5 = ['None']
                    result6.append(result5)
                    result5 = []
                result3.append(result6)
                result6 = []
                result4.append(result3)
                result3 = []
            if len(tmp1[i].get('security_groups')) == 0:
                result3 = ['None', 'None']
                result4.append(result3)
                result3 = []
            result1.append(result2)
            result2 = []
            result1.append(result4)
            result4 = []
            result.append(result1)
            result1 = []
        tools.str_to_unicode(result)
        return result

    def get_opdata(self):
        result = list()
        result1 = list()
        result2 = list()
        tmp = self.bv.getOp_info
        value1 = self.extract_data(tmp, 'ORDER_ID', 0)
        value10 = self.extract_data(tmp, 'STATUS', 0)
        value11 = self.extract_data(tmp, 'EXT_ID', 0)
        value12 = self.extract_data(tmp, 'ORDER_TIME', 0)
        value13 = self.extract_data(tmp, 'EFFECTIVE_TIME', 0)
        value14 = self.extract_data(tmp, 'END_TIME', 0)
        value15 = self.extract_data(tmp, 'NAME', 0)
        var1 = locals()
        result1 = [var1[key] for key in sorted(var1) if key.startswith('value')]
        value2 = self.extract_data(tmp, 'op_user_id', 0)
        value20 = self.extract_data(tmp, 'user_name', 0)
        value21 = self.extract_data(tmp, 'nick_name', 0)
        value22 = self.extract_data(tmp, 'user_status', 0)
        value23 = self.extract_data(tmp, 'ucreate_time', 0)
        value24 = self.extract_data(tmp, 'umodify_time', 0)
        value25 = self.extract_data(tmp, 'IS_HUAWEI', 0)
        value26 = self.extract_data(tmp, 'inform_type', 0)
        value27 = self.extract_data(tmp, 'LOGIN_FAILED_COUNT', 0)
        value28 = self.extract_data(tmp, 'user_id', 0)
        value29 = self.extract_data(tmp, 'tenant_id', 0)
        var2 = locals()
        result2 = [var2[key] for key in sorted(var2) if key.startswith('value')][7:]
        result.append(result1)
        result.append(result2)
        tools.str_to_unicode(result)
        return result

    def get_pmdata(self):
        tmp = self.bv.getPm_info
        value1 = self.extract_data(tmp, 'pm_nova_compute_state', 0)
        value10 = self.extract_data(tmp, 'pm_libvirtd_state', 0)
        value11 = self.extract_data(tmp, 'pm_host', 0)
        value12 = self.extract_data(tmp, 'pm_manage_ip', 0)
        value13 = self.extract_data(tmp, 'pm_service_ip', 0)
        value14 = self.extract_data(tmp, 'pm_store_ip', 0)
        value15 = self.extract_data(tmp, 'vm_qga_status', 0)
        var = locals()
        result = [var[key] for key in sorted(var) if key.startswith('value')]
        tools.str_to_unicode(result)
        return result

    def get_vmdata(self):
        result = list()
        result1 = list()
        result2 = list()
        tmp1 = self.bv.vmdata  # dict类型
        tmp2 = self.bv.getFlavor_info  # dict类型
        tmp3 = self.bv.getVncUrl
        value1 = self.extract_data(tmp1, 'id', 0)
        value10 = self.extract_data(tmp1, 'name', 0)
        value11 = self.extract_data(tmp1, 'status', 0)
        value12 = self.extract_data(tmp1, 'OS-EXT-STS:task_state', 0)
        value13 = self.extract_data(tmp1, 'OS-EXT-STS:power_state', 0)
        value14 = self.extract_data(tmp1, 'created', 0)
        if value14 is not None:
            value14 = tools.utctime_to_local(str(value14))
        value15 = self.extract_data(tmp3, 'vnc_url', 0)
        value16 = self.extract_data(tmp1, 'OS-EXT-SRV-ATTR:instance_name', 0)
        value17 = self.extract_data(tmp1, 'key_name', 0)
        value18 = self.extract_data(tmp1, 'system_disk_type', 0)
	var1 = locals()
        result1 = [var1[key] for key in sorted(var1) if key.startswith('value')]
        value2 = self.extract_data(tmp2, 'id', 0)
        value20 = self.extract_data(tmp2, 'name', 0)
        value21 = self.extract_data(tmp2, 'ram', 0)
        value22 = self.extract_data(tmp2, 'vcpus', 0)
        value23 = self.extract_data(tmp2, 'disk', 0)
        value24 = self.extract_data(tmp2, 'swap', 0)
        var2 = locals()
        result2 = [var2[key] for key in sorted(var2) if key.startswith('value')][-6:]
        result.append(result1)
        result.append(result2)
        tools.str_to_unicode(result)
        return result

    def get_volumedata(self):
        result = list()
        result1 = list()
        tmp1 = self.bv.getVolume_info  # 云主机挂载的硬盘
        tmp2 = self.bv.vmdata
        if len(tmp1) == 0:
            result.append('None')
        else:
            for i in range(len(tmp1)):
                value1 = self.extract_data(tmp1, 'id', 0)
                value10 = self.extract_data(tmp1, 'status', 0)
                value11 = self.extract_data(tmp1, 'name', 0)
                value12 = self.extract_data(tmp1, 'size', 0)
                value13 = self.extract_data(tmp1, 'type', 0)
                value14 = self.extract_data(tmp1, 'created_at', 0)
                if value14 is not 'None':
                    value14 = tools.utctime_to_local(str(value14))
                value15 = self.extract_data(tmp1, 'mount_status', 0)
                value16 = self.extract_data(tmp1, 'attached_mode', 0)
                value17 = self.extract_data(tmp2, 'os-extended-volumes:volumes_attached/id', 0)
                value18 = self.extract_data(tmp1, 'cluster', 0)
                var = locals()
                result1 = [var[key] for key in sorted(var) if key.startswith('value')]
                result.append(result1)
                result1 = []
        tools.str_to_unicode(result)
        return result

