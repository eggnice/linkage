#! /usr/bin/env python
# -*- coding:utf-8 -*-

# bcop sql query

from linkage.utils import utils
from linkage import opconfig


def gethscinfo(hsc_id):
    hsc_sql = '''SELECT h.HSC_ID, h.RESOURCE_CONFIG_ID, h.ROUTER_ID, h.HSC_NAME, h.CIRCLE_NUM, h.CIRCLE_ID, CASE
    `STATUS` WHEN 0 THEN '待受理' WHEN 1 THEN '已完工' WHEN 2 THEN '审核不通过' WHEN 3 THEN '待退订' WHEN 4 THEN
    '已退订' WHEN 5 THEN '开通配置中' ELSE 'undefined' END AS 'STATUS', h.IS_DELETE, h.USER_ID, h.CUSTOMER_ID,
    h.CREATED_TIME, h.MODIFIED_TIME, h.REGION, hc.CIRCLE_ID, hc.ECLOUD_CIDR, hc.DEST_CIDR, hc.BANDWIDTH, hc.IS_DELETE
    AS CIRCLE_IS_DELETE, hc.PROVINCE_ADDR, hc.CITY_ADDR, hc.DIST_ADDR, hc.ADDR_DETAIL, hc.USER_ID, hc.CUSTOMER_ID
    FROM g_biz_hsc h LEFT JOIN g_biz_hsc_circle hc ON h.HSC_ID = hc.HSC_ID WHERE h.HSC_ID = "%s"''' % hsc_id
    hsc_info = utils.execsql(hsc_sql, opconfig['OP_CLOUDMASTER_CONFIG'])
    return hsc_info
