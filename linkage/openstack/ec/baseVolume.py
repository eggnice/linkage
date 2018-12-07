# *_* coding=utf-8 *_*
# _author_: eggnice

"""
模块说明：获取volume相关属性，volumer_id
通过volume_id，调用cinder api获取卷信息，
"""

from linkage.openstack.ec.baseCinder import baseCinder
from linkage.exceptions import ReturnNone
from linkage import loggers


class baseVolume(object):
    """根据volume_id获取volume(快存储)的相关信息"""
    def __init__(self, volume_id):
        self.data = {'id': volume_id}
        self.volume_id = volume_id

    def __call__(self, *args, **kwargs):
        self.getVolumeInfo(self.volume_id)
        return self.data

    def getVolumeInfo(self, volume_id):
        """
        调用cinder_api,获取相关属性
        :param volume_id:
        :return:
        """
        # 调用cinder api获取volume的属性
        try:
            result = baseCinder.volume_idToDetail(volume_id)
            if result.get('attachments'):
                self.data['mount_status'] = True
                self.data['device'] = result['attachments'][0]['device']
                self.data['attached_mode'] = result['metadata']['attached_mode']
            else:
                self.data['mount_status'] = False
            self.data['name'] = result['name']
            self.data['size'] = result['size']
            self.data['created_at'] = result['created_at']
            self.data['status'] = result['status']
            self.data['type'] = result['volume_type']
            self.data['cluster'] = result['os-vol-host-attr:host']
        except ReturnNone, e:
            loggers.info('get volumes return none')
            return None
