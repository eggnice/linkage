#! /usr/bin/env python
# -*- coding:utf-8 -*-

# bcop sql query

from linkage.utils import utils
from linkage import opconfig


def geticpinfo(icp_public_ip):
    icp_sql = '''SELECT ID, ICP_ID, USER_ID, ICP_CERT_CODE, CASE ICP_STATUS WHEN - 2 THEN '服务台审批不通过'
    WHEN - 1 THEN '服务台审批' WHEN 0 THEN '未申请备案' WHEN 1 THEN '初审中' WHEN 2 THEN '初审未通过' WHEN 5 THEN
    '管局审核中' WHEN 6 THEN '管局审核通过' WHEN 7 THEN '管局审核未通过' WHEN 8 THEN '注销待审核' WHEN 9 THEN
    '注销初审不通过' WHEN 12 THEN '注销初审通过' WHEN 13 THEN '已注销' WHEN 14 THEN '注销失败' WHEN 15 THEN
    '申请失败' WHEN 16 THEN '变更初审中' WHEN 17 THEN '变更未通过' WHEN 18 THEN '变更管局审核中' WHEN 19 THEN
    '变更管局审核未通过' WHEN 25 THEN '二级域名备案启用' WHEN 26 THEN '二级域名备案禁止' ELSE 'undefined'
    END AS 'ICP_STATUS', CASE ICP_TYPE WHEN 1 THEN '首次备案' WHEN 2 THEN '接入备案' WHEN 3 THEN '备案登记' ELSE
    'undefined' END AS 'ICP_TYPE', ICP_REGISTER_TIME, ICP_UPDATE_TIME, ICP_PUBLIC_IP, ICP_DOMAIN, ICP_PROVINCE,
    ICP_CITY, ICP_SUGGESTION, ICP_AUDITOR, ICP_CONTACTOR, ICP_CONTACTOR_PHONE, POOL_ID, CASE ICP_BBFS WHEN 0 THEN
    '自行报备' WHEN 1 THEN '代为报备' ELSE 'UNDEFINED' END AS 'ICP_BBFS', CASE ICP_RETURN_CODE WHEN 0 THEN '备案系统退回'
    WHEN 1 THEN '备案系统管理员核实退回' WHEN 2 THEN '管局审核中' WHEN 3 THEN '管局审核通过' WHEN 4 THEN '管局退回' ELSE
    'UNDEFINED' END AS 'ICP_RETURN_CODE', ICP_RETURN_MSG, IP_ID, ICP_IS_SUCCESS FROM opm_icp_info WHERE
    ICP_PUBLIC_IP like '%%%s%%' ''' % icp_public_ip
    icp_info = utils.execsql(icp_sql, opconfig['OP_CLOUDMASTER_CONFIG'])
    return icp_info
