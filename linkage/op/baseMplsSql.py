#! /usr/bin/env python
# _*_ coding:utf-8 _*_

# bcop sql query

from linkage.utils import utils
from linkage import opconfig


def getmplsinfo(mpls_id):
    mpls_sql = '''SELECT MPLS_ID, MPLS_NAME, BANDWIDTH, ECLOUD_CIDRS, RESOURCE_CONFIG_ID, DEST_CIDRS, CREATED_TIME,
    MODIFIED_TIME, USER_ID, CUSTOMER_ID, CASE `STATUS` WHEN 0 THEN '待受理' WHEN 1 THEN '已完工' WHEN 2 THEN '审批不通过'
    WHEN 3 THEN '待退订' WHEN 4 THEN '已退订' WHEN 5 THEN '开通配置中' ELSE 'undefined' END AS 'STATUS', IS_DELETE,
    REGION, ROUTER_ID FROM g_biz_mpls WHERE MPLS_ID ='%s' ''' % mpls_id
    mpls_info = utils.execsql(mpls_sql, opconfig['OP_CLOUDMASTER_CONFIG'])
    return mpls_info
