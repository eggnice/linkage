#!/user/bin/env python
# -*- coding: utf-8 -*-

from linkage.op import userBlock
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def username(username):
    user = userBlock.userInfo(username)
    user.userInfo_username()
    usercheck(user)


def phone(phone):
    user = userBlock.userInfo(phone)
    user.userInfo_phone()
    usercheck(user)


def email(email):
    user = userBlock.userInfo(email)
    user.userInfo_email()
    usercheck(user)


def customerid(customerid):
    user = userBlock.userInfo(customerid)
    user.userInfo_id()
    usercheck(user)


def phoneNew(user_name, phone, email, customer_id, phone_new):
    user = userBlock.userInfoNew(user_name, phone, email, customer_id, phone_new)
    user.userInfo_all()
    if user.result:
        """用户存在"""
        user = userBlock.userInfo(phone_new)
        user.userInfo_phone()
        if user.user_exist:
            print "您要修改的新手机号码已经被使用，无法更改。"
        else:
            user = userBlock.userInfoNew(user_name, phone, email, customer_id, phone_new)
            user.newuserphone()
            print "\n修改成功，烦请通知客户记得修改密码或者邮箱以便修改后的信息可以同步其他子系统！\n"
    else:
        print "您需要修改手机号的用户不存在，请重新核对用户信息"


def usercheck(user):
    if user.user_exist:
        """打印用户信息"""
        print(u"<用户信息>")
        print("%s: %s" % ("user_id", user.user_id))
        print("%s: %s" % (u"登录名", user.user_name))
        print("%s: %s" % (u"用户状态", user.user_status))
        print("%s: %s" % (u"是否客户", user.is_customer))
        print("%s: %s" % (u"手机", user.phone))
        print("%s: %s" % (u"邮箱", user.email))
        print("%s: %s" % (u"是否客户", user.is_customer))
        print("%s: %s" % (u"创建时间", user.ucreate_time))
        print("%s: %s" % (u'登录过op', user.is_first_login))

        print(u"\n<客户信息>")
        print("%s: %s" % ("cudtomer_id", user.customer_id))
        print("%s: %s" % ("boss_cust_id", user.boss_cust_id))
        print("%s: %s" % (u"客户名称", user.cust_name))
        print("%s: %s" % (u"客户状态", user.cust_status))
        print("%s: %s" % (u"客户来源", user.reg_source))
        print("%s: %s" % (u"客户折扣信息", user.global_discount))
        print("%s: %s" % (u"付费类型", user.payment_type))
        print("%s: %s" % (u"boss_pro_order_code", user.boss_pro_order_code))
        print("%s: %s" % (u"创建时间", user.create_time))

        print(u"\n<客户经理信息>")
        print("%s: %s" % ("contactor", user.contactor))
        print("%s: %s" % (u"客户经理手机", user.mng_phone))

    else:
        print "user is not found"
    if user.cust_status in [u"注册待归档", u"待基础产品订单同步", u"待基础产品反馈"] and user.boss_pro_order_code:
        print(u"\n<客户状态异常排查>")
        if user.reg_source == u"政企客户":
            bosslog = userBlock.bossloginfo(user.boss_pro_order_code)
            bosslog.bossloginfo()
            if bosslog.bosslog_exit:
                for registry_log in bosslog.bosslog_list:
                    request = registry_log["REQUESR_MSG"]
                    response = registry_log["RESPONSE_MSG"]
                    if registry_log["TYPE"] == "正向客户产品订单/订购关系同步" and registry_log["DIRECTION"] == 0:
                        rspcode = re.findall(r'.*?<RspCode>(.*?)</RspCode>.*?', response)
                        rspdesc = re.findall(r'.*?<RspDesc>(.*?)</RspDesc>.*?', response)
                        print('RspCode: %s' % rspcode[0])
                        print('RspDesc: %s' % rspdesc[0])
                        if rspcode[0] == '0000':
                            print(u"正向客户基础产品订购同步正常")
                        else:
                            print(u"正向客户基础产品订购同步异常")
                            break
                    elif registry_log["TYPE"] == "反向客户产品订单/订购关系同步反馈" and registry_log["DIRECTION"] == 1:
                        rspcode = re.findall(r'.*?<RspCode>(.*?)</RspCode>.*?', response)
                        rspdesc = re.findall(r'.*?<RspDesc>(.*?)</RspDesc>.*?', response)
                        print('RspCode: %s' % rspcode[0])
                        print('RspDesc: %s' % rspdesc[0])
                        if rspcode[0] == '0000':
                            print(u"反向客户产品订单/订购关系同步反馈正常")
                        else:
                            print(u"反向客户产品订单/订购关系同步反馈异常")
                            break
                    elif registry_log["TYPE"] == "归档" and registry_log["DIRECTION"] == 0:
                        status = re.findall(r'.*?<Status>(.*?)</Status>.*?', request)
                        print('status: %s' % status[0])
                        if status[0] == "1":
                            print(u"归档异常")
                            break
            else:
                if not user.boss_order_id and user.boss_cust_id:
                    print(u"基础订购关系同步异常")
                elif not user.boss_cust_id:
                    print(u"正向客户信息同步异常")

        if user.reg_source == u"互联网客户":
            bosslog = userBlock.bossloginfo(user.boss_pro_order_code)
            bosslog.bossloginfo()
            if bosslog.bosslog_exit:
                for registry_log in bosslog.bosslog_list:
                    request = registry_log["REQUESR_MSG"]
                    response = registry_log["RESPONSE_MSG"]
                    if registry_log["TYPE"] == "反向客户产品订单/订购关系同步反馈" and registry_log["DIRECTION"] == 1:
                        rspcode = re.findall(r'.*?<RspCode>(.*?)</RspCode>.*?', response)
                        rspdesc = re.findall(r'.*?<RspDesc>(.*?)</RspDesc>.*?', response)
                        print('RspCode: %s' % rspcode[0])
                        print('RspDesc: %s' % rspdesc[0])
                        if rspcode[0] == '0000':
                            print(u"反向客户基础产品订购同步正常")
                        else:
                            print(u"反向客户基础产品订购同步异常")
                            break
                    elif registry_log["TYPE"] == "正向客户产品订单/订购关系同步" and registry_log["DIRECTION"] == 0:
                        rspcode = re.findall(r'.*?<RspCode>(.*?)</RspCode>.*?', response)
                        rspdesc = re.findall(r'.*?<RspDesc>(.*?)</RspDesc>.*?', response)
                        print('RspCode: %s' % rspcode[0])
                        print('RspDesc: %s' % rspdesc[0])
                        if rspcode[0] == '0000':
                            print(u"正向客户产品订单/订购关系同步反馈正常")
                        else:
                            print(u"正向客户产品订单/订购关系同步反馈")
                            break
                    elif registry_log["TYPE"] == "归档" and registry_log["DIRECTION"] == 0:
                        status = re.findall(r'.*?<Status>(.*?)</Status>.*?', request)
                        print('status: %s' % status[0])
                        if status[0] == "1":
                            print(u"归档异常")
                            break
            else:
                if not user.boss_order_id and user.boss_cust_id:
                    print(u"没有收到基础订购关系同步报文")
                elif not user.boss_cust_id:
                    print(u"正向客户信息同步异常")

        if user.reg_source == u"bboss客户":
            bosslog = userBlock.bossloginfo(user.boss_pro_order_code)
            bosslog.bossloginfo()
            if bosslog.bosslog_exit:
                for registry_log in bosslog.bosslog_list:
                    request = registry_log["REQUESR_MSG"]
                    if registry_log['TYPE'] == "BBOSS正向订购信息同步" and registry_log["DIRECTION"] == 10:
                        action = re.findall(r'.*?<Action>(.*?)</Action>.*?', registry_log["REQUESR_MSG"])
                        if action[0] == "1":
                            if registry_log['BOSS_ORDER_ID']:
                                print(u"正向客户信息注册同步正常")
                            else:
                                print(u"正向客户信息注册同步异常")
                                break
                    if registry_log["TYPE"] == "BBOSS归档" and registry_log["DIRECTION"] == 10:
                        status = re.findall(r'.*?<Status>(.*?)</Status>.*?', registry_log["REQUESR_MSG"])
                        if status[0] == "1":
                            print('status: 1')
                            print(u"归档异常")
                            break
            else:
                if not user.boss_order_id and user.boss_cust_id:
                    print(u"没有收到同步请求")
    if user.reg_source == u"bboss客户":
        bosslog = userBlock.bossloginfo(user.boss_order_id)
        bosslog.bosslog_id()
        if bosslog.bosslog_exit:
            for registry_log in bosslog.bosslog_list:
                request = registry_log["REQUESR_MSG"]
                if registry_log['TYPE'] == "BBOSS正向订购信息同步" and registry_log["DIRECTION"] == 10:
                    action = re.findall(r'.*?<Action>(.*?)</Action>.*?', registry_log["REQUESR_MSG"])
                    if action[0] == "2":
                        print(u"客户异常：收到注销报文，但客户未删除")
                        break
    elif not user.boss_pro_order_code and user.user_exist:
        print(u"\nop异常，没有boss_order_code")
