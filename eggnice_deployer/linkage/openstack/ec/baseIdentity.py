# *_* coding: utf-8 *_*
# __author__: eggnice

from linkage.exceptions import ReturnNone
from linkage.openstack import identityApi

class baseIdentity(object):
    """
    identityapi的上一层
    """
    def __init__(self, user_id):
        self.user_id =user_id

    @staticmethod
    def userDetails(user_id):
        result = identityApi.users_showUserDetails(user_id)
        if result.get('user'):
            return result.get('user')
        else:
            return None
   
    def getTenant_id(self):
        result = baseIdentity.userDetails(self.user_id)
        tenant_id = result.get('default_project_id')
        return tenant_id



