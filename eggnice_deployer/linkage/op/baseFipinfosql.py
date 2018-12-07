#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from linkage.utils import utils
from linkage import opconfig


def getFipinfo_by_port(ippb_id):
    sql1 = '''SELECT ippb.ID, ippb.`NAME`, ippb.CREATED_TIME, ippb.PROPOSER, ippb.CUSTOMER_ID,
ippb.IS_DELETE, bw.ID AS 'BANDWIDTH_ID',
    bw.BANDWIDTH_SIZE,case ippb.ICP_STATUS WHEN 0 THEN  '未申请' WHEN 1 THEN 'IP备案中' WHEN 2 THEN 'IP备案成功'
    WHEN 3 THEN 'IP备案失败' WHEN 4 THEN 'ICP备案中' WHEN 5 THEN 'ICP备案成功' WHEN 6 THEN 'ICP备案失败 ' WHEN 7
    THEN '注销成功' WHEN 8 THEN '注销失败' ELSE 'UNDEFINED' END AS 'ICP_STATUS', case ippb.`STATUS` WHEN 0
    THEN '未绑定' WHEN 1 THEN '绑定' ELSE 'UNDEFINED' END AS 'STATUS', ippb.MODIFIED_TIME
    FROM os_biz_ippb ippb LEFT JOIN os_biz_bandwidth bw on bw.PUBLIC_IP = ippb.`NAME`
    where ippb.ID = "%s" AND bw.IS_DELETE =0''' % (ippb_id)
    ipinfo = utils.execsql(sql1, opconfig['OP_OPENSTACK_CONFIG'])
    return ipinfo
