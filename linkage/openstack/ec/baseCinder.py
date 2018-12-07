# *_* coding: utf-8 *_*
# __author__: eggnice

from linkage.openstack import cinderApi
from linkage.exceptions import ReturnNone

class baseCinder(object):
    def __init__(self):
        pass

    @staticmethod
    def volume_idToDetail(volume_id):
        """
        通过卷id获取详细信息
        :param volume_id:
        :return: json
        """
        result = cinderApi.volumes_showVolumeDetails(volume_id)
        if result.get('volume'):
            return result.get('volume')
        raise ReturnNone('show volume:%s details return none' % volume_id)

