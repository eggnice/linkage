#! /usr/bin/env python
# -*- coding:utf-8 -*-

# bcop sql query

from linkage.utils import utils
from linkage import opconfig


def getipsecinfo(id):
    ipsec_sql = '''SELECT s.ID, s.`NAME`, CASE s.`STATUS` WHEN 0 THEN 'ACTIVE' WHEN 1 THEN 'BUILD' WHEN 2 THEN 'DOWN'
    WHEN 3 THEN 'ERROR' WHEN 4 THEN 'PENDING_CREATE' WHEN 5 THEN 'PENDING_UPDATE' WHEN 6 THEN 'PENDING_DELETE'
    ELSE  'undefined' END AS 'STATUS', s.SUBNET_ID, s.ROUTER_ID, s.POOL_ID, s.CUSTOMER_ID,
    s.PROPOSER, s.CREATED_BY, s.CREATED_TIME, s.MODIFIED_BY, s.IS_DELETE, c.IKEPOLICY_ID, c.IPSECPOLICY_ID,
    c.PEER_ADDRESS, c.PEER_ID, c.PEER_CIDRS, c.AUTH_MODE, c.ROUTE_MODE, c.mtu, c.INITIATOR, c.psk, c.MODIFIED_TIME FROM
    os_biz_ipsec_vpn_service s LEFT JOIN os_biz_ipsec_siteconn c on c.VPNSERVICE_ID = s.ID WHERE s.id = "%s" ''' % id
    ipsec_info = utils.execsql(ipsec_sql, opconfig['OP_OPENSTACK_CONFIG'])
    return ipsec_info
