#!/usr/bin/env python
# -*- coding: utf-8 -*-

from linkage.op import orderBlock, userBlock
import re
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


def ordercheck(order):
    order = orderBlock.Order(order)
    promotion = orderBlock.Promotion(order.order_id)
    if promotion.promotion_exist:
        print("<此订单 %s 为促销订单>" % (order.order_id))

    if order.order_exist:
        print(u"\n<订单信息>")
        print("%s: %s" % ("订单号", order.order_id))
        print("%s: %s" % ("订单类型", order.order_type))
        print("%s: %s" % ("订单状态", order.order_status))
        print("%s: %s" % ("父订单号", order.parent_id))
        print("%s: %s" % ("订购时间", order.order_time))
        print("%s: %s" % ("订单来源", order.order_source))

        print(u"\n<用户信息>")
        user = userBlock.userInfo(order.cmp_customer_id)
        user.userInfo_id()
        print("%s: %s" % ("BOSS_CUST_ID", user.boss_cust_id))
        print("%s: %s" % ("USER_ID", user.user_id))
        print("%s: %s" % ("USER_NAME", user.user_name))
        print("%s: %s" % ("CUSTOMER_ID", user.customer_id))
        print("%s: %s" % ("REG_SOURCE", user.reg_source))

        print(u"\n<订单项信息>")
        ext = orderBlock.Ext(order.order_id)
        print(u'订单项数量：%s' % ext.ext_num)
        print("#" * 44)
        for item_ext in ext.ext_list:
            if item_ext['STATUS'] not in [u'已开通', u'已关闭', u'同步EBOSS审批待反馈']:
                print("%s: %s" % ("订单项ID", item_ext["ID"]))
                print("%s: %s" % ("产品名称", item_ext["NAME"]))
                print("%s: %s" % ("订单项状态", item_ext["STATUS"]))
                print("%s: %s" % ("BOSS_ORDER_ID", item_ext["BOSS_ORDER_ID"]))
                print("%s: %s" % ("资源池", item_ext["CMP_POOL_ID"]))
                orderextcheck(item_ext)
                print("#" * 44)
            else:
                print("%s: %s" % ("订单项ID", item_ext["ID"]))
                print("%s: %s" % ("产品名称", item_ext["NAME"]))
                print("%s: %s" % ("订单项状态", item_ext["STATUS"]))
                print("%s: %s" % ("资源UUID", item_ext["RETURN_ID"]))
                print("%s: %s" % ("资源是否删除", item_ext["IS_DELETE"]))
                print("%s: %s" % ("BOSS_ORDER_ID", item_ext["BOSS_ORDER_ID"]))
                print("%s: %s" % ("ORDER_TIME", item_ext["ORDER_TIME"]))
                print("%s: %s" % ("EFFECTIVE_TIME", item_ext["EFFECTIVE_TIME"]))
                print("%s: %s" % ("END_TIME", item_ext["END_TIME"]))
                print("%s: %s" % ("资源池", item_ext["CMP_POOL_ID"]))
                print("#" * 44)
        return ext.ext_num


def extcheck(ext_id):
    ext = orderBlock.Extbyid(ext_id)
    print(u"\n<订单项信息>")
    print("%s: %s" % ("订单项ID", ext.ext_list[0]["ID"]))
    print("%s: %s" % ("订单ID", ext.ext_list[0]["ORDER_ID"]))
    print("%s: %s" % ("产品名称", ext.ext_list[0]["NAME"]))
    print("%s: %s" % ("订单项状态", ext.ext_list[0]["STATUS"]))
    print("%s: %s" % ("资源UUID", ext.ext_list[0]["RETURN_ID"]))
    print("%s: %s" % ("资源是否删除", ext.ext_list[0]["IS_DELETE"]))
    print("%s: %s" % ("BOSS_ORDER_ID", ext.ext_list[0]["BOSS_ORDER_ID"]))
    print("%s: %s" % ("ORDER_TIME", ext.ext_list[0]["ORDER_TIME"]))
    print("%s: %s" % ("EFFECTIVE_TIME", ext.ext_list[0]["EFFECTIVE_TIME"]))
    print("%s: %s" % ("END_TIME", ext.ext_list[0]["END_TIME"]))
    print("%s: %s" % ("资源池", ext.ext_list[0]["CMP_POOL_ID"]))
    if ext.ext_list[0]["STATUS"] not in [u'已开通', u'已关闭']:
        print(u"\n<异常订单项检查>")
        orderextcheck(ext.ext_list[0])
    elif ext.ext_list[0]["STATUS"] in [u'已开通'] and ext.ext_list[0]["BOSS_ORDER_ID"] is None:
        print
        bbosstimeoutcheck(ext.ext_list[0])

    print(u"\n<客户信息>")
    order = orderBlock.Order(ext.ext_list[0]["ORDER_ID"])
    user = userBlock.userInfo(order.cmp_customer_id)
    user.userInfo_id()
    print("%s: %s" % ("BOSS_CUST_ID", user.boss_cust_id))
    print("%s: %s" % ("USER_ID", user.user_id))
    print("%s: %s" % ("USER_NAME", user.user_name))
    print("%s: %s" % ("CUSTOMER_ID", user.customer_id))
    print("%s: %s" % ("REG_SOURCE", user.reg_source))


def orderextcheck(ext):
    """订单项异常状态判断"""
    log = orderBlock.Log(ext["ID"])
    archive = orderBlock.Archive(ext["ID"])

    # 开通订单检查
    if ext['STATUS'] in [u'新建', u'等待审核', u'审核不通过', u'等待开通', u'正在开通', u'开通待同步', u'开通失败']:
        if ext['RETURN_ID']:
            print('"资源" : %s "开通成功"' % ext['RETURN_ID'])
            if ext['BOSS_ORDER_ID']:
                print('"订购关系" %s "同步成功"' % ext['BOSS_ORDER_ID'])
                if archive.archive_num == "":
                    print(u"未收到开通归档！")
                elif archive.archive_num != "" or archive.archive_list[0]['STATUS'] is not '0' \
                        or archive.archive_list[0]['IS_DONE'] is not 1:
                    print('"归档STATUS:" %s' % archive.archive_list[0]['STATUS'])
                    print('"归档IS_DONE:" %s' % archive.archive_list[0]['IS_DONE'])
                    print(u"开通归档失败!")
            else:
                print(u"开通同步失败！")
                for item_log in log.log_list:
                    if item_log["OPERATION_TYPE"] == u'新建' and item_log["OP_ORDER_NUM"] is not None:
                        bosslog_open = orderBlock.Bosslog(item_log["OP_ORDER_NUM"])
                        for item_bosslog in bosslog_open.bosslog_list:
                            if item_bosslog["TYPE"] == u"BBOSS省集团反向订购关系同步" and \
                                    item_bosslog["DIRECTION"] == 11:
                                response = item_bosslog["RESPONSE_MSG"]
                                if response:
                                    rspCode = re.findall(r'.*?<RspCode>(.*?)</RspCode>.*?', response)
                                    rspDesc = re.findall(r'.*?<RspDesc>(.*?)</RspDesc>.*?', response)
                                    rspDesc_code = str(rspDesc).replace('u\'', '\'')
                                    print('OP_ORDER_NUMBER: %s' % item_bosslog["OP_ORDER_NUMBER"])
                                    print('ORDERNUMBER: %s' % item_bosslog["ORDERNUMBER"])
                                    print('RspCode: %s' % rspCode)
                                    print('RspDesc: %s' % (rspDesc_code.decode("unicode-escape")))
                                    if rspCode and rspCode[0] in ['0133', '0108']:
                                        print(u'BBOSS开通同步失败，请后台尝试订购关系同步！')
                                    else:
                                        print(u'BBOSS同步状态未知，请联系BBOSS确认状态后处理！')
                            elif item_bosslog["TYPE"] == u"正向客户产品订单/订购关系同步反馈" and \
                                    item_bosslog["DIRECTION"] == 0:
                                request = item_bosslog["REQUESR_MSG"]
                                if request:
                                    rspCode = re.findall(r'.*?<RspCode>(.*?)</RspCode>.*?', request)
                                    rspDesc = re.findall(r'.*?<RspDesc>(.*?)</RspDesc>.*?', request)
                                    rspDesc_code = str(rspDesc).replace('u\'', '\'')
                                    print('OP_ORDER_NUMBER: %s' % item_bosslog["OP_ORDER_NUMBER"])
                                    print('ORDERNUMBER: %s' % item_bosslog["ORDERNUMBER"])
                                    print('RspCode: %s' % rspCode)
                                    print('RspDesc: %s' % (rspDesc_code.decode("unicode-escape")))
                                    print(u"订单项开通同步EBOSS失败,请联系EBOSS确认状态后处理！")
                        break
        else:
            print(u"资源开通失败，请联系底层排查！")
            log = orderBlock.Log(ext["ID"])
            for item_log in log.log_list:
                if item_log["IS_SUCCESS"] == 0:
                    print("%s: %s" % ("INSTANCE_ID", item_log["INSTANCE_ID"]))
                    print("%s: %s" % ("FAIL_CODE", item_log["FAIL_CODE"]))
                    print("%s: %s" % ("FAIL_MESSAGE", item_log["FAIL_MESSAGE"]))

    # 退订订单检查
    elif ext['STATUS'] in [u'正在关闭', u'关闭待删除', u'关闭失败']:
        for item_log in log.log_list:
            if item_log["OPERATION_TYPE"] == u'取消' and item_log["OP_ORDER_NUM"] is not None:
                bosslog_close = orderBlock.Bosslog(item_log["OP_ORDER_NUM"])
                for item_bosslog in bosslog_close.bosslog_list:
                    if (item_bosslog["TYPE"] == u"BBOSS省集团反向订购关系同步" and
                            item_bosslog["DIRECTION"] == 11):
                        response = item_bosslog["RESPONSE_MSG"]
                        if response:
                            rspCode = re.findall(r'.*?<RspCode>(.*?)</RspCode>.*?', response)
                            rspDesc = re.findall(r'.*?<RspDesc>(.*?)</RspDesc>.*?', response)
                            rspDesc_code = str(rspDesc).replace('u\'', '\'')
                            print('OP_ORDER_NUMBER: %s' % item_bosslog["OP_ORDER_NUMBER"])
                            print('ORDERNUMBER: %s' % item_bosslog["ORDERNUMBER"])
                            print('RspCode: %s' % rspCode)
                            print('RspDesc: %s' % (rspDesc_code.decode("unicode-escape")))
                            if rspCode and rspCode[0] in ['0133', '0108']:
                                print(u'BBOSS退订同步失败，请尝试二次同步！')
                            elif rspCode and rspCode[0] in ['0000']:
                                print(u'BBOSS退订同步成功！')
                            else:
                                print(u'BBOSS退订同步状态未知，请联系BBOSS确认状态后处理！')
                    elif (item_bosslog["TYPE"] == u"正向客户产品订单/订购关系同步反馈" and
                            item_bosslog["DIRECTION"] == 0):
                        request = item_bosslog["REQUESR_MSG"]
                        if request:
                            rspCode = re.findall(r'.*?<RspCode>(.*?)</RspCode>.*?', request)
                            rspDesc = re.findall(r'.*?<RspDesc>(.*?)</RspDesc>.*?', request)
                            rspDesc_code = str(rspDesc).replace('u\'', '\'')
                            print('OP_ORDER_NUMBER: %s' % item_bosslog["OP_ORDER_NUMBER"])
                            print('ORDERNUMBER: %s' % item_bosslog["ORDERNUMBER"])
                            print('RspCode: %s' % rspCode)
                            print('RspDesc: %s' % (rspDesc_code.decode("unicode-escape")))
                            if rspCode and rspCode[0] in ['0000']:
                                print(u'EBOSS退订同步成功！')
                            else:
                                print(u"订单项退订EBOSS失败,请联系EBOSS确认状态后处理！")
                    elif item_bosslog["TYPE"] == u"归档" and item_bosslog["DIRECTION"] == 0:
                        request = item_bosslog["REQUESR_MSG"]
                        if request:
                            status = re.findall(r'.*?<Status>(.*?)</Status>.*?', request)
                            print('归档status: %s' % status)
                            if status[0] == "0":
                                print('EBOSS归档成功')
                            else:
                                print('EBOSS归档失败')
                    elif item_bosslog["TYPE"] == u"BBOSS归档" and item_bosslog["DIRECTION"] == 12:
                        print('BBOSS归档成功')
                break
        if archive.archive_num < 2:
            print(u"未收到退订归档！")
        for item_log in log.log_list:
            if item_log["OPERATION_TYPE"] == u'取消'and item_log["OP_ORDER_NUM"] is None \
                    and item_log["IS_SUCCESS"] == 0:
                print("%s: %s" % ("INSTANCE_ID", item_log["INSTANCE_ID"]))
                print("%s: %s" % ("FAIL_CODE", item_log["FAIL_CODE"]))
                print("%s: %s" % ("FAIL_MESSAGE", item_log["FAIL_MESSAGE"]))
                print(u"资源删除失败,请联系底层排查！")

    # 暂停订单检查
    elif ext['STATUS'] in [u'等待冻结', u'正在冻结', u'已冻结', u'冻结失败']:
        for item_log in log.log_list:
            if item_log["OPERATION_TYPE"] == u'暂停' and item_log["OP_ORDER_NUM"] is not None:
                bosslog_suspend = orderBlock.Bosslog(item_log["OP_ORDER_NUM"])
                for item_bosslog in bosslog_suspend.bosslog_list:
                    if item_bosslog["TYPE"] == u"反向客户产品订单/订购关系同步反馈" and item_bosslog["DIRECTION"] == 1:
                        request = item_bosslog["REQUESR_MSG"]
                        if request:
                            rspCode = re.findall(r'.*?<RspCode>(.*?)</RspCode>.*?', request)
                            rspDesc = re.findall(r'.*?<RspDesc>(.*?)</RspDesc>.*?', request)
                            rspDesc_code = str(rspDesc).replace('u\'', '\'')
                            print('OP_ORDER_NUMBER: %s' % item_bosslog["OP_ORDER_NUMBER"])
                            print('ORDERNUMBER: %s' % item_bosslog["ORDERNUMBER"])
                            print('RspCode: %s' % rspCode)
                            print('RspDesc: %s' % (rspDesc_code.decode("unicode-escape")))
                            if rspCode and rspCode[0] in ['00']:
                                print(u'暂停同步反馈成功！')
                            else:
                                print(u'暂停同步反馈失败，请排查订单确认状态后处理！')
                    elif item_bosslog["TYPE"] == u"归档" and item_bosslog["DIRECTION"] == 0:
                        request = item_bosslog["REQUESR_MSG"]
                        if request:
                            status = re.findall(r'.*?<Status>(.*?)</Status>.*?', request)
                            print(('归档status: %s') % status)
                            if status[0] == "0":
                                print(('EBOSS暂停归档成功'))
                            else:
                                print(('EBOSS暂停归档失败'))
                break
        for item_log in log.log_list:
            if item_log["OPERATION_TYPE"] == u'暂停' and item_log["OP_ORDER_NUM"] is None \
                    and item_log["IS_SUCCESS"] == 0:
                print("%s: %s" % ("INSTANCE_ID", item_log["INSTANCE_ID"]))
                print("%s: %s" % ("FAIL_CODE", item_log["FAIL_CODE"]))
                print("%s: %s" % ("FAIL_MESSAGE", item_log["FAIL_MESSAGE"]))
                print(u"资源冻结失败,请联系底层排查！")

    # 恢复订单检查
    elif ext['STATUS'] in [u'等待恢复', u'正在恢复', u'恢复失败']:
        for item_log in log.log_list:
            if item_log["OPERATION_TYPE"] == u'恢复' and item_log["OP_ORDER_NUM"] is not None:
                bosslog_recover = orderBlock.Bosslog(item_log["OP_ORDER_NUM"])
                for item_bosslog in bosslog_recover.bosslog_list:
                    if item_bosslog["TYPE"] == u"反向客户产品订单/订购关系同步反馈" and item_bosslog["DIRECTION"] == 1:
                        request = item_bosslog["REQUESR_MSG"]
                        if request:
                            rspCode = re.findall(r'.*?<RspCode>(.*?)</RspCode>.*?', request)
                            rspDesc = re.findall(r'.*?<RspDesc>(.*?)</RspDesc>.*?', request)
                            rspDesc_code = str(rspDesc).replace('u\'', '\'')
                            print('OP_ORDER_NUMBER: %s' % item_bosslog["OP_ORDER_NUMBER"])
                            print('ORDERNUMBER: %s' % item_bosslog["ORDERNUMBER"])
                            print('RspCode: %s' % rspCode)
                            print('RspDesc: %s' % (rspDesc_code.decode("unicode-escape")))
                            if rspCode and rspCode[0] in ['00']:
                                print(u'恢复同步反馈EBOSS成功！')
                            else:
                                print(u'恢复同步反馈EBOSS失败，请排查订单确认状态后处理！')
                    elif item_bosslog["TYPE"] == u"归档" and item_bosslog["DIRECTION"] == 0:
                        request = item_bosslog["REQUESR_MSG"]
                        if request:
                            status = re.findall(r'.*?<Status>(.*?)</Status>.*?', request)
                            print(('归档status: %s') % status)
                            if status[0] == "0":
                                print(('EBOSS恢复归档成功'))
                            else:
                                print(('EBOSS恢复归档失败'))
                break
        for item_log in log.log_list:
            if item_log["OPERATION_TYPE"] == u'恢复' and item_log["OP_ORDER_NUM"] is None \
                    and item_log["IS_SUCCESS"] == 0:
                print("%s: %s" % ("INSTANCE_ID", item_log["INSTANCE_ID"]))
                print("%s: %s" % ("FAIL_CODE", item_log["FAIL_CODE"]))
                print("%s: %s" % ("FAIL_MESSAGE", item_log["FAIL_MESSAGE"]))
                print(u"资源恢复失败,请联系底层排查！")


def bbosstimeoutcheck(ext):
    """BBOSS订单已开通，但同步超时检查"""
    log = orderBlock.Log(ext["ID"])
    for item_log in log.log_list:
        if item_log["OPERATION_TYPE"] == u'新建' and item_log["OP_ORDER_NUM"] is not None:
            bosslog_open = orderBlock.Bosslog(item_log["OP_ORDER_NUM"])
            for item_bosslog in bosslog_open.bosslog_list:
                if item_bosslog["TYPE"] == u"BBOSS省集团反向订购关系同步" and item_bosslog["DIRECTION"] == 11:
                    response = item_bosslog["RESPONSE_MSG"]
                    if response:
                        rspCode = re.findall(r'.*?<RspCode>(.*?)</RspCode>.*?', response)
                        rspDesc = re.findall(r'.*?<RspDesc>(.*?)</RspDesc>.*?', response)
                        rspDesc_code = str(rspDesc).replace('u\'', '\'')
                        print('OP_ORDER_NUMBER: %s' % item_bosslog["OP_ORDER_NUMBER"])
                        print('ORDERNUMBER: %s' % item_bosslog["ORDERNUMBER"])
                        print('RspCode: %s' % rspCode)
                        print('RspDesc: %s' % (rspDesc_code.decode("unicode-escape")))
                        print(u'BBOSS同步超时，请联系BBOSS确认BOSS_ORDER_ID和生效时间！')
            break
        else:
            print(u"不同步BBOSS列表:文件存储，弹性伸缩，HAVIP，模板编排，专线，镜像，防火墙，子网")
