#!/usr/bin/env python
# -*- coding: utf-8 -*-
from linkage.op import hscBlock
from linkage.op import icpBlock
from linkage.op import ipsecBlock
from linkage.op import mplsBlock
from linkage.op import secgroupBlock
from linkage.op import vdiskBlock
from linkage.op import vfwBlock
from linkage.op import fipBlock
from linkage.op import vlbBlock
from linkage.op import vmBlock
from linkage.op import portBlock


def hsc_check(id):
    print(u'OP侧资源状态：')
    hsc = hscBlock.Hsc(id)
    if hsc.hsc_exist:
        hsc.__str__()


def icp_check(ip):
    print(u'OP侧资源状态：')
    icp = icpBlock.Icp(ip)
    if icp.icp_exist:
        icp.__str__()


def ipsec_check(id):
    print(u'OP侧资源状态：')
    ipsec = ipsecBlock.Ipsec(id)
    if ipsec.ipsec_exist:
        ipsec.__str__()
        # print u'\n底层资源状态：'
        # sdn_ipsec = ipsecVpnBlock.IpsecVpn(id)
        # sdn_ipsec.__str__()


def mpls_check(id):
    print(u'OP侧资源状态：')
    mpls = mplsBlock.Mpls(id)
    if mpls.mpls_exist:
        mpls.__str__()
        # print u'\n底层资源状态：'


def secgroup_check(id):
    print(u'OP侧资源状态：')
    secgroup = secgroupBlock.SecGroup(id)
    if secgroup.sg_exist:
        secgroup.__str__()
        # print u'\n底层资源状态：'
        # sdn_sg = securityGroupBlock.SecurityGroup(id)
        # sdn_sg.__str__()


def vdisk_check(id):
    print(u'OP侧资源状态：')
    vdisk = vdiskBlock.Vdisk(id)
    if vdisk.vdisk_exist:
        vdisk.__str__()
        # print u'\n底层资源状态：'
        # ec_disk = Volume(id)
        # ec_disk.__str__()


def vfw_check(id):
    print(u'OP侧资源状态：')
    vfw = vfwBlock.Vfw(id)
    if vfw.vfw_exist:
        vfw.__str__()
        # print u'\n底层资源状态：'
        # sdn_fw = Fw(id)
        # sdn_fw.__str__()


def fip_check(ip):
    print u'OP侧资源状态：'
    fip = fipBlock.Fip(ip)
    if fip.fip_exist:
        fip.__str__()


"""for ip_item in fip.attach:
           if ip_item['TYPE'] == 'vm':
               print u'绑定虚拟机详情：'
               vm = vmBlock.Vm(ip_item['RESOURCE_ID'])
               vm.__str__()
               if vm.sec_group[0]['sec_group']:
                   for sg_item in vm.sec_group:
                        print u'\n安全组%s详情：' % sg_item['sec_group']
                        sg = secgroupBlock.SecGroup(sg_item['sec_group'])
                        if sg.sg_exist:
                            sg.__str__()
                if vm.vm_user_id:
                    print u'\n云防火墙详情：'
                    fw = vfwBlock.Vfw(vm.vm_user_id)
                    if fw.vfw_exist:
                        fw.__str__()
            elif ip_item['TYPE'] == 'elb':
                print u'绑定VLB详情：'
                elb = vlbBlock.Vlb(ip_item['RESOURCE_ID'])
                elb.__str__()
    print u'\n底层资源状态：'
    sdn_ip = Fip(ip)
    sdn_ip.__str__()'''"""


def vlb_check(id):
    print(u'OP侧资源状态：')
    vlb = vlbBlock.Vlb(id)
    if vlb.vlb_exist:
        vlb.__str__()
        for vlb_item in vlb.listen:
            if vlb_item['vm_host_id']:
                print(u'vlb绑定虚拟机信息：')
                vm = vmBlock.Vm(vlb_item['vm_host_id'])
                vm.__str__()

                # print u'\n底层资源状态：'
                # sdn_vlb = sdnVlb.Vlb(id)
                # sdn_vlb.__str__()


def vm_check(id):
    print(u'OP侧云主机资源状态：')
    vm = vmBlock.Vm(id)
    if vm.vm_exist:
        print("%s: %s" % ("云主机资源编码:", vm.vm_id))
        print("%s: %s" % ("云主机名称:", vm.name))
        print("%s: %s" % ("VCPU", vm.vcpu))
        print("%s: %s" % ("内存", vm.vmemory))
        print("%s: %s" % ("存储容量", vm.vdisk))
        print("%s: %s" % ("物理机ID", vm.hw_host_id))
        print("%s: %s" % ("云主机状态", vm.status))
        print("%s: %s" % ("操作标志", vm.operation_flag))
        print("%s: %s" % ("资源池", vm.pool_id))
        print("%s: %s" % ("云主机是否删除", vm.is_delete))
        print
        port_check(vm.vm_id)
        # print u'\n底层资源状态：'
        # #VmInforMation.printInfo(id)
        return vm.vcpu


def port_check(resource_id):
    print(u'OP侧云主机绑定网卡信息：')
    port = portBlock.Port(resource_id)
    if port.port_exist:
        print(("%s: %s") % ("绑定网卡数量", port.port_num))
        print("#" * 44)
        for item_port in port.port_list:
            print("%s: %s" % ("网卡ID", item_port["ID"]))
            print("%s: %s" % ("网卡名称", item_port["NAME"]))
            print("%s: %s" % ("网卡状态", item_port["STATUS"]))
            print("%s: %s" % ("网卡私网IP", item_port["PRIVATE_IP"]))
            print("%s: %s" % ("网卡网络ID", item_port["NETWORK_ID"]))
            print("%s: %s" % ("网卡子网ID", item_port["SUBNET_ID"]))
            print("%s: %s" % ("绑定资源ID", item_port["RESOURCE_ID"]))
            print("%s: %s" % ("是否基础子网", item_port["IS_BASIC"]))
            ippb_check_by_port(item_port["ID"])


def ippb_check_by_port(port_id):
    print(u'OP侧网卡绑定公网IP信息：')
    ippb = fipBlock.Fip(port_id)
    if ippb.fip_exist:
        print("%s: %s" % ("公网IP ID", ippb.id))
        print("%s: %s" % ("公网IP", ippb.name))
        print("%s: %s" % ("备案状态", ippb.icp_status))
        print("%s: %s" % ("带宽ID", ippb.bandwidth_id))
        print("%s: %s" % ("带宽大小", ippb.bandwidth_size))
        print("%s: %s" % ("公网IP状态", ippb.status))
        print("#" * 44)
    else:
        print("网卡未绑定公网IP")
