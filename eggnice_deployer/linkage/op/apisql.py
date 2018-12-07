# *_* coding: utf-8 *_*
# _author_: eggnice

from linkage import Utils
from linkage import opconfig

databaseconfig = opconfig['OP_CLOUDMASTER_CONFIG']

def ec_getOrder(uuid):
    """
    通过资源的uuid获取相关的order信息
    return: list[]
    """
    sql = """SELECT
	ooei.RETURN_ID as 'ID',
        ooe.ID as 'EXT_ID',
        CASE ooe.`STATUS`
        WHEN 0 THEN '新建' WHEN 1 THEN '等待审核' WHEN 2 THEN '审核不通过' WHEN 3 THEN '等待开通' WHEN 4 THEN '正在开通'
        WHEN 5 THEN '开通待同步' WHEN 6 THEN '已开通' WHEN 7 THEN '开通失败' WHEN 8 THEN '等待冻结' WHEN 9 THEN '正在冻结'
        WHEN 10 THEN '已冻结' WHEN 11 THEN '冻结失败' WHEN 12 THEN '等待关闭' WHEN 13 THEN '正在关闭' WHEN 29 THEN
        '关闭待删除' WHEN 14 THEN '已关闭' WHEN 15 THEN '关闭失败' WHEN 16 THEN '等待恢复' WHEN 17 THEN '正在恢复'
        WHEN 18 THEN '恢复失败' WHEN 19 THEN '等待生效' WHEN 20 THEN '已取消' WHEN 21 THEN '等待变更' WHEN 22 THEN
        '正在变更' WHEN 23 THEN '变更失败' WHEN 24 THEN '欠费等待续费' WHEN 25 THEN '欠费等待冻结' WHEN 26 THEN
        '欠费正在冻结' WHEN 27 THEN '欠费冻结失败' WHEN 28 THEN '已续订' WHEN 31 THEN '退款同步' WHEN 32 THEN
        '退款同步失败' WHEN 33 THEN '退款同步成功' WHEN 34 THEN '退款' WHEN 35 THEN '退款失败' WHEN 36 THEN '退款成功'
        WHEN 46 THEN '同步EBOSS审批待反馈' ELSE 'UNDEFINED' END AS 'STATUS',
        oo.ORDER_TIME,
        oo.ORDER_ID,
        ooe.EFFECTIVE_TIME,
        ooe.END_TIME,
        osi.`NAME`
        FROM opm_order_ext_instance ooei
        LEFT JOIN opm_order_ext ooe ON ooe.id = ooei.ORDER_EXT_ID
        LEFT JOIN opm_service_info osi ON osi.`ID` = ooe.SERVICE_INFO_ID
        LEFT JOIN opm_order oo ON oo.ORDER_ID = ooe.ORDER_ID
        WHERE ooei.RETURN_ID = '%s'""" % uuid
    return Utils.execsql(sql, databaseconfig) 
