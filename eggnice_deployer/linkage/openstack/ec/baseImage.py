# *_* coding: utf-8
# _author_: eggnice

"""
根据云主机的uuid获取和该云主机有关的镜像信息
类方法主要是通过glance api请求数据，得到和该云主机有关的images
"""

from linkage.openstack.ec.baseGlance import baseGlance
from linkage import loggers
from linkage.exceptions import (ReturnNone, LogicError)


class baseImage(object):
    """根据uuid获取虚机的image信息，再判断是backup还是snapshot
    返回list[{id:x,create_at:x,update_at,image.os_type:x,size:x,os_distro:x,image_type:x
    nmae:x}]"""

    def __init__(self, uuid, original_image_id):
        """
        user类的基本属性
        :param uuid: 虚机uuid
        """
        self.vm_id = uuid
        self.original_image_id = original_image_id
        self.data = []
        self.keys = ['id', 'created_at', 'updated_at', 'image.os_type', 'size', 'name',
                     'os_type', 'status']

    def __call__(self, *args, **kwargs):
        self.get_imageInfo()
        return self.data

    def get_imageInfo(self):
        """ image_info"""
        try:
            original_image = baseGlance.getOriginalImage(self.original_image_id)
            if not original_image.has_key('os_type'):
		self.keys[6] = 'os_distro'
	    if not original_image and not isinstance(original_image, dict):
                raise LogicError('can not find original image by:%s' % self.original_image_id)
            self.data.append({key: original_image[key] for key in self.keys})
            images_list = baseGlance.getImages(self.vm_id)
            self.keys = self.keys + ['image_type', 'base_image_ref']
            for one in images_list:
                self.data.append({key: one[key] for key in self.keys})
        except ReturnNone, e:
            loggers.info(str(e))
            return None
