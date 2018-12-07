# *_* coding: utf-8 *_*
# _author: eggnice

from linkage.openstack.ec.baseNova import baseNova

class baseFlavor(object):
    def __init__(self, flavor_id):
        self.flavor_id = flavor_id
        self.data = ''

    def __call__(self, *args, **kwargs):
        self.get_flavor_info()
        return self.data

    def get_flavor_info(self):
        self.data = baseNova.get_flavor(self.flavor_id)
