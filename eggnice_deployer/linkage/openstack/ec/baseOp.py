#!/usr/bin/env python
# coding=utf-8

"""
获取虚拟机用户信息，输入user_name（来源baseVm）,并且调用op的userBlock
通过调用api方式请求
"""

from linkage.openstack.ec.baseIdentity import baseIdentity
from linkage.op.baseUserInfosql import Getuserinfo
from linkage.op.apisql import ec_getOrder


class baseOp(object):
    """根据user_name(用户名)获取user(用户)的相关信息"""

    def __init__(self, user_id, uuid):
        """
        user类的基本属性
        :param user_id: 用户名
        """
        self.user_id = user_id
        self.uuid = uuid
        self.user_name = ''
        self.user_info = {'user_id': self.user_id}

    def __call__(self, *args, **kwargs):
        self.getOpInfo()
        return self.user_info

    def getOpInfo(self):
        """
        通过identity的api获取identity的所有属性，返回结果为dict
        :param _user_name:
        :return:
        """
        user_mess = baseIdentity.userDetails(self.user_id)
        if not user_mess:
            self.user_info = ''
            return None
        self.user_info['user_name'] = user_mess.get('username')
        self.user_info['tenant_id'] = user_mess.get('default_project_id')
        op_info = Getuserinfo(self.user_info['user_name'])
        data = op_info.getuserinfo_username()
        if not data:
            raise Exception('Op返回了空数据请排查op部分')
        data = data[0]
        keys = ['LOGIN_FAILED_COUNT', 'ucreate_time', 'user_status', 'umodify_time', 'inform_type',
                'nick_name', 'IS_HUAWEI']
        self.user_info['op_user_id'] = data['user_id']
        self.user_info.update({key: data[key] for key in keys})
        self.user_info.update(ec_getOrder(self.uuid)[0])
