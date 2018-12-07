# *_* coding: utf-8 *_*
# __author__: eggnice

from linkage.openstack.baseOpenstackApi import openstackapi
from linkage.openstack.baseCinderApi import cinderapi
from linkage.openstack.baseIdentityApi import identityapi
from linkage.openstack.baseNeutronApi import neutronapi
from linkage.openstack.baseNovaApi import novaapi
from linkage.openstack.baseGlanceApi import glanceapi

connopenstack = openstackapi()
cinderApi = cinderapi(connopenstack.tenant_id)
identityApi = identityapi()
neutronApi = neutronapi()
novaApi = novaapi(connopenstack.tenant_id)
glanceApi = glanceapi()
