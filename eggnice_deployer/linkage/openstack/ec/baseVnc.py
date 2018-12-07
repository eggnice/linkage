# *_* coding: utf-8 *_*
# _author: eggnice

from linkage.openstack.ec.baseNova import baseNova
from linkage.exceptions import ReturnNone

class baseVnc(object):
    def __init__(self, uuid):
        self.uuid = uuid
        self.data = {}

    def __call__(self, *args, **kwargs):
        self.get_vncInfo()
        return self.data

    def get_vncInfo(self):
        result = baseNova.post_vnc(self.uuid)
        if result:
            self.data['vnc_url'] = result.get('url')
        else:
            raise ReturnNone('post to get vnc_url return None')

