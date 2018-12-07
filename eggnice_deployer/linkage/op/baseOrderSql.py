#!/usr/bin/env python
# -*- coding: utf-8 -*-

# bcop sql query

from linkage.utils import utils
from linkage import opconfig
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def getOrderInfo(order_id):
    """get order information according to order_id"""
    ordersql = """ SELECT ORDER_ID, CASE ORDER_TYPE WHEN 1 THEN '新建' WHEN 2 THEN '取消' WHEN 3 THEN '暂停' WHEN
     4 THEN '恢复' WHEN 5 THEN '变更' WHEN 6 THEN '续订' WHEN 7 THEN '试用创建' WHEN 8 THEN '试用转商用' WHEN 9 THEN
     '成员开通' WHEN 10 THEN 'PAAS、SAAS取消' WHEN 12 THEN '内部优惠审批订单'
     ELSE 'UNDEFINED' END AS 'ORDER_TYPE', CASE ORDER_STATUS WHEN 1 THEN
     '支付成功' WHEN 2 THEN '等待支付' WHEN 3 THEN '已经取消' WHEN 4 THEN '已关闭' ELSE 'UNDEFINED' END AS
     'ORDER_STATUS', PARENT_ID, ORDER_TIME, PROPOSER, PROPOSER_NAME, CMP_CUSTOMER_ID, CMP_CUSTOMER_NAME, ORDER_MEMO,
      ORDER_SOURCE, CONFIRM_BY, APPROVAL_MSG, CASE OPEN_TYPE WHEN 0 THEN '离线开通' WHEN 1 THEN '在线开通' WHEN 2
      THEN 'ITIL流程' ELSE 'UNDEFINED' END AS 'OPEN_TYPE', ORDER_JSON, CONFIRM_TIME, TOTAL FROM opm_order WHERE
      ORDER_ID = "%s" """ % order_id
    return utils.execsql(ordersql, opconfig['OP_CLOUDMASTER_CONFIG'])


def getExtInfo(order_id):
    """get ext information according to order_id"""
    extsql = """ SELECT ext.ID, ext.ORDER_ID, CASE ITEM_TYPE WHEN 1 THEN '新建' WHEN 2 THEN '取消' WHEN 3 THEN '暂停'
     WHEN 4 THEN '恢复' WHEN 5 THEN '变更' WHEN 6 THEN '续订' WHEN 7 THEN '试用创建' WHEN 8 THEN '试用转商用' WHEN 9
      THEN '成员开通' WHEN 10 THEN 'PAAS、SAAS取消'  WHEN 12 THEN '内部优惠审批订单'
      ELSE 'UNDEFINED' END AS 'ITEM_TYPE', REL_ITEM_ID, CASE `STATUS`
      WHEN 0 THEN '新建' WHEN 1 THEN '等待审核' WHEN 2 THEN '审核不通过' WHEN 3 THEN '等待开通' WHEN 4 THEN '正在开通'
      WHEN 5 THEN '开通待同步' WHEN 6 THEN '已开通' WHEN 7 THEN '开通失败' WHEN 8 THEN '等待冻结' WHEN 9 THEN '正在冻结'
       WHEN 10 THEN '已冻结' WHEN 11 THEN '冻结失败' WHEN 12 THEN '等待关闭' WHEN 13 THEN '正在关闭' WHEN 29 THEN
       '关闭待删除' WHEN 14 THEN '已关闭' WHEN 15 THEN '关闭失败' WHEN 16 THEN '等待恢复' WHEN 17 THEN '正在恢复'
       WHEN 18 THEN '恢复失败' WHEN 19 THEN '等待生效' WHEN 20 THEN '已取消' WHEN 21 THEN '等待变更' WHEN 22 THEN
       '正在变更' WHEN 23 THEN '变更失败' WHEN 24 THEN '欠费等待续费' WHEN 25 THEN '欠费等待冻结' WHEN 26 THEN
       '欠费正在冻结' WHEN 27 THEN '欠费冻结失败' WHEN 28 THEN '已续订' WHEN 31 THEN '退款同步' WHEN 32 THEN
       '退款同步失败' WHEN 33 THEN '退款同步成功' WHEN 34 THEN '退款' WHEN 35 THEN '退款失败' WHEN 36 THEN '退款成功'
       WHEN 46 THEN '同步EBOSS审批待反馈'
        ELSE 'UNDEFINED' END AS 'STATUS', CASE OPEN_TYPE WHEN 0 THEN '离线开通' WHEN 1 THEN '在线开通' WHEN 2 THEN
        'ITIL流程' ELSE 'UNDEFINED' END AS 'OPEN_TYPE', ext.CUSTOMER_REMARK, service.`NAME`, template.CMP_POOL_ID,
        ext.DURATION, ext.ORDER_TIME, ext.EFFECTIVE_TIME, ext.END_TIME, ext.AUTO_RENEWAL, ext.PRICE, ext.CONFIRM_BY,
        ext.CONFIRM_TIME, ext.APPROVAL_MSG, ext.BOSS_ORDER_ID, ext.PRODUCT_ORDER_ID, ext.OP_ORDER_NUM,
        instance.RETURN_ID, CASE instance.IS_DELETE WHEN 0 THEN 'FALSE' WHEN 1 THEN 'TRUE' ELSE
        'UNDEFINDE' END AS 'IS_DELETE' FROM opm_order_ext ext LEFT JOIN opm_resource_template template ON
        ext.POOL_TEMPLATE_ID = template.ID LEFT JOIN opm_service_info service ON ext.SERVICE_INFO_ID = service.ID
        LEFT JOIN opm_order_ext_instance instance ON ext.id = instance.ORDER_EXT_ID WHERE
        ext.ORDER_ID = "%s" """ % order_id
    return utils.execsql(extsql, opconfig['OP_CLOUDMASTER_CONFIG'])


def getExtInfoById(ext_id):
    """get ext information according to ext_id"""
    extsql2 = """ SELECT ext.ID, ext.ORDER_ID, CASE ITEM_TYPE WHEN 1 THEN '新建' WHEN 2 THEN '取消' WHEN 3 THEN '暂停'
         WHEN 4 THEN '恢复' WHEN 5 THEN '变更' WHEN 6 THEN '续订' WHEN 7 THEN '试用创建' WHEN 8 THEN '试用转商用' WHEN 9
          THEN '成员开通' WHEN 10 THEN 'PAAS、SAAS取消'  WHEN 12 THEN '内部优惠审批订单'
          ELSE 'UNDEFINED' END AS 'ITEM_TYPE', REL_ITEM_ID, CASE `STATUS`
          WHEN 0 THEN '新建' WHEN 1 THEN '等待审核' WHEN 2 THEN '审核不通过' WHEN 3 THEN '等待开通' WHEN 4 THEN '正在开通'
          WHEN 5 THEN '开通待同步' WHEN 6 THEN '已开通' WHEN 7 THEN '开通失败' WHEN 8 THEN '等待冻结' WHEN 9 THEN '正在冻结'
           WHEN 10 THEN '已冻结' WHEN 11 THEN '冻结失败' WHEN 12 THEN '等待关闭' WHEN 13 THEN '正在关闭' WHEN 29 THEN
           '关闭待删除' WHEN 14 THEN '已关闭' WHEN 15 THEN '关闭失败' WHEN 16 THEN '等待恢复' WHEN 17 THEN '正在恢复'
           WHEN 18 THEN '恢复失败' WHEN 19 THEN '等待生效' WHEN 20 THEN '已取消' WHEN 21 THEN '等待变更' WHEN 22 THEN
           '正在变更' WHEN 23 THEN '变更失败' WHEN 24 THEN '欠费等待续费' WHEN 25 THEN '欠费等待冻结' WHEN 26 THEN
           '欠费正在冻结' WHEN 27 THEN '欠费冻结失败' WHEN 28 THEN '已续订' WHEN 31 THEN '退款同步' WHEN 32 THEN
           '退款同步失败' WHEN 33 THEN '退款同步成功' WHEN 34 THEN '退款' WHEN 35 THEN '退款失败' WHEN 36 THEN '退款成功'
           WHEN 46 THEN '同步EBOSS审批待反馈'
            ELSE 'UNDEFINED' END AS 'STATUS', CASE OPEN_TYPE WHEN 0 THEN '离线开通' WHEN 1 THEN '在线开通' WHEN 2 THEN
            'ITIL流程' ELSE 'UNDEFINED' END AS 'OPEN_TYPE', ext.CUSTOMER_REMARK, service.`NAME`, template.CMP_POOL_ID,
            ext.DURATION, ext.ORDER_TIME, ext.EFFECTIVE_TIME, ext.END_TIME, ext.AUTO_RENEWAL, ext.PRICE, ext.CONFIRM_BY,
            ext.CONFIRM_TIME, ext.APPROVAL_MSG, ext.BOSS_ORDER_ID, ext.PRODUCT_ORDER_ID, ext.OP_ORDER_NUM,
            instance.RETURN_ID, CASE instance.IS_DELETE WHEN 0 THEN 'FALSE' WHEN 1 THEN 'TRUE' ELSE
            'UNDEFINDE' END AS 'IS_DELETE' FROM opm_order_ext ext LEFT JOIN opm_resource_template template ON
            ext.POOL_TEMPLATE_ID = template.ID LEFT JOIN opm_service_info service ON ext.SERVICE_INFO_ID = service.ID
            LEFT JOIN opm_order_ext_instance instance ON ext.id = instance.ORDER_EXT_ID WHERE
            ext.ID = "%s" """ % ext_id
    return utils.execsql(extsql2, opconfig['OP_CLOUDMASTER_CONFIG'])


def getArchiveInfo(ext_id):
    """get archive information according to ext_id"""
    archivesql = """ SELECT ID, PRODUCT_ORDER_ID, CASE `STATUS` WHEN 0 THEN '成功' WHEN 1 THEN '失败' ELSE 'UNDEFINED'
     END AS 'STATUS', ARCHIVE_TIME, IS_DONE, CREATE_TIME, ORDER_EXT_ID, CASE TYPE WHEN 0 THEN 'BOSS正向订购'
      WHEN 1 THEN 'BOSS反向订购' WHEN 2 THEN 'BOSS正向客户' WHEN 3 THEN 'BBOSS反向订购' WHEN 4 THEN 'BBOSS正向客户'
       ELSE 'UNDEFINED' END AS 'TYPE' FROM opm_boss_archive WHERE ORDER_EXT_ID = "%s" """ % ext_id
    return utils.execsql(archivesql, opconfig['OP_CLOUDMASTER_CONFIG'])


def getLogInfo(ext_id):
    """get log information according to ext_id"""
    logsql = """ SELECT ID, ORDER_EXT_ID, CASE OPERATION_TYPE WHEN 1 THEN '新建' WHEN 2 THEN '取消' WHEN 3 THEN
     '暂停' WHEN 4 THEN '恢复' WHEN 5 THEN '变更' WHEN 6 THEN '续订' WHEN 7 THEN '试用创建' WHEN 8 THEN '试用转商用'
      WHEN 9 THEN '成员开通' WHEN 10 THEN 'PAAS、SAAS取消' ELSE 'UNDEFINED' END AS 'OPERATION_TYPE', OP_ORDER_NUM,
       PRODUCT_ORDER_ID, INSTANCE_ID, IS_SUCCESS, FAIL_CODE, FAIL_MESSAGE, REOPEN_JSON, CREATE_TIME, IS_SECONDARY,
        RELOAD_COUNT, IS_DONE FROM opm_order_ext_log WHERE ORDER_EXT_ID = "%s" """ % ext_id
    return utils.execsql(logsql, opconfig['OP_CLOUDMASTER_CONFIG'])


def getBosslogInfo(op_order_num):
    """get bossagent log information according to ext_id"""
    bosslogsql = """SELECT TYPE, ORDERNUMBER, BOSS_ORDER_ID, OP_ORDER_NUMBER, REQUESR_MSG, RESPONSE_MSG, IS_SUCCESS,
    DIRECTION, DATE, ERROR_DESC FROM opm_bossagent_log WHERE OP_ORDER_NUMBER = "%s" """ % op_order_num
    return utils.execsql(bosslogsql, opconfig['OP_CLOUDMASTER_CONFIG'])


def getPromotionInfo(order_id):
    """get promotion information according to order_id"""
    promotionsql = """SELECT PROMOTION_ID, STATUS, ORDER_ID FROM opm_promotion_flow WHERE ORDER_ID = "%s" """ % order_id
    return utils.execsql(promotionsql, opconfig['OP_CLOUDMASTER_CONFIG'])
