# *_* coding: utf-8 *_*
# _author: eggnice

from linkage.openstack.ec.baseNova import baseNova

class baseAction(object):
    """
    获取实例的相关操作(nova),return list:[{},]
    """
    def __init__(self, uuid):
        self.uuid = uuid
        self.data = ''

    def __call__(self, *args, **kwargs):
        self.get_Actiondata()
        return self.data

    def get_Actiondata(self):
        result = baseNova.get_actions(self.uuid)
        keys = ['start_time', 'action', 'request_id', 'message']
        self.data = [{key: one[key] for key in keys} for one in result]
