# *_* coding: utf-8
# _author_: eggnice

import re
from linkage.openstack import glanceApi
from linkage.exceptions import (ReturnNone, ConnectionGlanceError)

class baseGlance(object):
    def __init__(self):
        pass

    @staticmethod
    def getImages(uuid):
        """
        获取和vm_uuid关联的镜像
        :param uuid: string
        :return: list
        """
        result = glanceApi.images_listImages(instance_uuid=uuid)
        if result.get('images'):
            return result.get('images')
        raise ReturnNone('get images return none')

    @staticmethod
    def getOriginalImage(image_id):
        """
        获取image_id对应的image
        :param image_id: image_id
        :return: dict
        """
        try:
            result = glanceApi.images_showImage(image_id)
            return result
        except ConnectionGlanceError, e:
            pattern = re.compile(r'No image found with ID')
            if pattern.search(str(e)):
                return None



