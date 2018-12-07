# *_* coding: utf-8 *_*
# __author__: eggnice

from linkage.openstack import novaApi
from linkage.exceptions import ReturnNone

class baseNova(object):
    """
    novaApi的上一层主要是防止block直接操作baseapi层
    """
    def __init__(self):
        pass

    @staticmethod
    def getServerByIp(fixed_ip, user_id):
        result = novaApi

    @staticmethod
    def getServerById(uuid):
        """
        :param uuid:
        :return: dict:{}
        """
        result = novaApi.servers_showServerDetails(uuid).get('server')
        return result if result else None
        #raise ReturnNone('get servers details by id:%s return none or servers' % uuid)

    @staticmethod
    def get_actions(uuid):
        """
        :param uuid:
        :return: list:[]
        """
        result = novaApi.servers_listActions(uuid).get('instanceActions')
        return result if result else None

    @staticmethod
    def post_vnc(uuid):
        """
        :param uuid:
        :return: dict
        """
        result = novaApi.servers_vncAction(uuid).get('console')
        return result if result else None

    @staticmethod
    def get_flavor(flavor_id):
        """
        :param flavor_id:
        :return: dict or none
        """
        result = novaApi.flavors_showDetails(flavor_id).get('flavor')
        return result if result else None

