# *_* coding: utf-8 *_*
# __author__: eggnice

"""ec 模块函数入口"""

import sys
import IPy
from linkage import loggers
from linkage.openstack.ec.built.builtArgs import builtArgs
from linkage.openstack.ec.built.builtVm import builtVm
from linkage.exceptions import ErrorMessage
from linkage.openstack.ec.baseNova import baseNova
from linkage.openstack.ec.blockVm import blockVm

def judgeargs(args):
    """
    judge args is vm_uuid or vm_public ip
    or vm_private ip and vm_username to return vm_uuid
    """
    try:
        if len(args) == 1:
            if len(args[0]) <= 15:
                if IPy.IP(args[0]).iptype() == 'PUBLIC':
                    UUID = builtArgs.floatingIp(args[0])
                else:
                    raise ErrorMessage('输入的公网ip错误:%s',args[0])
            else:
                if baseNova.getServerById(args[0]):
                    UUID = args[0]
                else:
                    raise ErrorMessage('输入的uuid查询不到相应的vm：%s' % args[0])
        else:
            if IPy.IP(args[0]).iptype() == 'PRIVATE':
                UUID = builtArgs.fixedIp(args[0], args[1])
            else:
                raise ErrorMessage('输入的私网ip/用户名:%s有误' % (args[0], args[1]))
    except Exception, e:
        loggers.error(str(e))
        print e; sys.exit(1)
    return UUID

def main(args, block):
    try:
        if len(args) == 1 or len(args) == 2:
            UUID = judgeargs(args)
        else:
            print '请输入参数: [VM_UUID], [VM公网IP], [VM私网IP 用户名]'
            sys.exit(1)
        ll = list(block)
        inst = blockVm()
        inst.init_uuid(UUID)
        builtVm(inst, ll)
    except Exception, e:
        loggers.error(str(e))
        print '程序遇到错误请作者进行排查:%s' % str(e); sys.exit(1)

