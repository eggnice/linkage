#! /usr/bin/env python
# _*_ coding:utf-8 _*_

# bcop sql query

from linkage.utils import utils
from linkage import opconfig


class Getuserinfo(object):

    def __init__(self, _argument):
        self.username = _argument
        self.phone = _argument
        self.email = _argument
        self.customerid = _argument
        self.op_order_number = _argument
        self.boss_order_id = _argument

    def getuserinfo_username(self):
        """get user information according to user_name"""

        usersql = """ select u.id user_id,u.user_name,u.email,u.phone,case u.IS_CUSTOMER when 0 then '用户' when 1
            then '客户' end 'is_customer',u.LOGIN_FAILED_COUNT,u.create_time ucreate_time,u.password,case u.user_status
            when 1 then '正常' when 2 then '暂停' when 3 then '非法' when 4 then '非法及暂停' when 5 then '锁定' when 6
            then '已注销' end as user_status, case u.type when 1 then '部门管理员' when 2 then '部门普通用户'
            end as type,u.creator,u.modified_by,u.modify_time umodify_time,case inform_type when 0 then '不通知' when 1
            then '短信' when 2 then '邮件' when  3 then '短信+邮件' end as inform_type,u.is_delete,
            case u.is_first_login when 1 then '否' when 2 then '是' end as 'is_first_login' ,u.nick_name,
            c.id customer_id,c.boss_cust_id,case c.cust_status WHEN 1 THEN '正常' WHEN 2 THEN '暂停' WHEN 3 THEN '待审批'
            WHEN 4 THEN '审批未通过' WHEN 5 THEN '欠费' WHEN 6 THEN '已注销' WHEN 7 THEN '等待删除' WHEN 11 THEN
            '注册待归档' WHEN 12 THEN '待基础产品订单同步' WHEN 13 THEN '待基础产品反馈' WHEN 8 THEN '预注销'
            ELSE 'undefined' END AS
            'CUST_STATUS',case c.REG_SOURCE when 0 then '互联网客户' when 1 then 'bboss客户' when 2 then '政企客户'
            when 3 then 'SaaS客户' end as 'reg_source', case c.is_huawei WHEN 0 THEN '四期客户' WHEN 1 THEN '三期客户'
            WHEN 2 THEN '三期无订单老客户' ELSE 'undefied' END as 'IS_HUAWEI',c.boss_pro_order_code,c.global_discount,case
            c.payment_type WHEN 1 THEN '预付费' WHEN 2 THEN '后付费' end as 'payment_type',c.contactor ,
            c.mng_phone,c.name as cust_name,c.email as cust_email,c.mobile as cust_phone,c.province,c.cont_phone,
            c.cont_email,c.cmcc_cust_mng,c.modify_time,c.create_time,c.boss_order_id from opm_user_user u left join
            opm_customer c on u.customer_id = c.id where u.user_name like "%s" """ % self.username.encode('utf-8')
        return utils.execsql(usersql, opconfig['OP_CLOUDMASTER_CONFIG'])

    def getuserinfo_mobiles(self):
        """get user information according to mobile"""
        usersql = """ select u.id user_id,u.user_name,u.email,u.phone,case u.IS_CUSTOMER when 0 then '用户' when
            1 then '客户' end 'is_customer',u.LOGIN_FAILED_COUNT,u.create_time ucreate_time,u.password,case u.user_status
            when 1 then '正常' when 2 then '暂停' when 3 then '非法' when 4 then '非法及暂停' when 5 then '锁定' when 6
            then '已注销' end as user_status, case u.type when 1 then '部门管理员' when 2 then '部门普通用户'
            end as type,u.creator,u.modified_by,u.modify_time umodify_time,case inform_type when 0 then '不通知' when 1
            then '短信' when 2 then '邮件' when  3 then '短信+邮件' end as infrom_type,u.is_delete,case u.is_first_login
            when 1 then '否' when 0 then '是' end as 'is_first_login',u.nick_name,
            c.id customer_id,c.boss_cust_id,case c.cust_status WHEN 1 THEN '正常' WHEN 2 THEN '暂停' WHEN 3 THEN '待审批'
            WHEN 4 THEN '审批未通过' WHEN 5 THEN '欠费' WHEN 6 THEN '已注销' WHEN 7 THEN '等待删除' WHEN 11 THEN
            '注册待归档' WHEN 12 THEN '待基础产品订单同步' WHEN 13 THEN '待基础产品反馈' WHEN 8 THEN '预注销'
            ELSE 'undefined' END AS
            'CUST_STATUS',case c.REG_SOURCE when 0 then '互联网客户' when 1 then 'bboss客户' when 2 then '政企客户'
            when 3 then 'SaaS客户'end as 'reg_source',case c.is_huawei WHEN 0 THEN '四期客户' WHEN 1 THEN '三期客户'
            WHEN 2 THEN '三期无订单老客户' ELSE 'undefied' END as 'IS_HUAWEI',c.boss_pro_order_code,c.global_discount,
            case c.payment_type when 1 then '预付费' when 2 then '后付费' end as 'payment_type' ,c.contactor ,
            c.mng_phone ,c.name as cust_name,c.email as cust_email,c.mobile as cust_phone,c.province,c.cont_phone,
            c.cont_email,c.cmcc_cust_mng,c.modify_time,c.create_time,c.boss_order_id from opm_user_user  u left join
            opm_customer c on u.customer_id = c.id  where u.phone = "%s"
            """ % self.phone.encode('utf-8')
        return utils.execsql(usersql, opconfig['OP_CLOUDMASTER_CONFIG'])

    def getuserinfo_email(self):
        """get user information according to email"""
        usersql = """ select u.id user_id,u.user_name,u.email,u.phone,case u.IS_CUSTOMER when 0 then '用户' when 1
            then '客户' end 'is_customer',u.LOGIN_FAILED_COUNT,u.create_time ucreate_time,u.password,case u.user_status
            when 1 then '正常' when 2 then '暂停' when 3 then '非法' when 4 then '非法及暂停' when 5 then '锁定' when 6
            then '已注销' end as user_status, case u.type when 1 then '部门管理员' when 2 then '部门普通用户'
            end as type,u.creator,u.modified_by,u.modify_time umodify_time,case inform_type when 0 then '不通知'
            when 1 then '短信' when 2 then '邮件' when  3 then '短信+邮件' end as inform_type,u.is_delete,
            case u.is_first_login when 1 then '否' when 0 then '是' end as 'is_first_login',u.nick_name,
            c.id customer_id,c.boss_cust_id,case c.cust_status WHEN 1 THEN '正常' WHEN 2 THEN '暂停' WHEN 3 THEN '待审批'
            WHEN 4 THEN '审批未通过' WHEN 5 THEN '欠费' WHEN 6 THEN '已注销' WHEN 7 THEN '等待删除' WHEN 11 THEN '注册待归档'
            WHEN 12 THEN '待基础产品订单同步' WHEN 13 THEN '待基础产品反馈' WHEN 8 THEN '预注销'
            ELSE 'undefined' END AS 'CUST_STATUS',case
            c.REG_SOURCE when 0 then '互联网客户' when 1 then 'bboss客户' when 2 then '政企客户' when 3 then 'SaaS客户'end
            as 'reg_source', case c.is_huawei WHEN 0 THEN '四期客户' WHEN 1 THEN '三期客户' WHEN 2 THEN
            '三期无订单老客户' ELSE 'undefied' END as 'IS_HUAWEI',c.boss_pro_order_code,c.global_discount,
            case c.payment_type when 1 then '预付费' when 2 then '后付费' end as 'payment_type' , c.contactor ,
            c.mng_phone,c.name as cust_name,c.email as cust_email,c.mobile as cust_phone,c.province,c.cont_phone,
            c.cont_email,c.cmcc_cust_mng,c.modify_time,c.create_time,c.boss_order_id from opm_user_user u left join
            opm_customer c on u.customer_id = c.id where u.email = "%s" """ % self.email.encode('utf-8')
        return utils.execsql(usersql, opconfig['OP_CLOUDMASTER_CONFIG'])

    def getuserinfo_id(self):
        """get user information according to customer_id"""
        usersql = """ select u.id user_id,u.user_name,u.email,u.phone,case u.IS_CUSTOMER when 0 then '用户' when 1
            then '客户' end 'is_customer',u.LOGIN_FAILED_COUNT,u.create_time ucreate_time,u.password,case u.user_status
            when 1 then '正常' when 2 then '暂停' when 3 then '非法' when 4 then '非法及暂停' when 5 then '锁定' when 6
            then '已注销' end as user_status, case u.type when 1 then '部门管理员' when 2 then '部门普通用户'
            end as type,u.creator,u.modified_by,u.modify_time umodify_time,case inform_type when 0 then '不通知'
            when 1 then '短信' when 2 then '邮件' when  3 then '短信+邮件' end as inform_type,u.is_delete,u.nick_name,
            c.id customer_id,c.boss_cust_id,case c.cust_status WHEN 1 THEN '正常' WHEN 2 THEN '暂停'
            WHEN 3 THEN '待审批' WHEN 4 THEN '审批未通过' WHEN 5 THEN '欠费' WHEN 6 THEN '已注销' WHEN 7 THEN '等待删除'
            WHEN 11 THEN '注册待归档' WHEN 12 THEN '待基础产品订单同步' WHEN 13 THEN '待基础产品反馈' WHEN 8 THEN '预注销'
            ELSE 'undefined'
            END AS 'CUST_STATUS',case c.REG_SOURCE when 0 then '互联网客户' when 1 then 'bboss客户'
            when 2 then '政企客户' when 3 then 'SaaS客户'end as 'reg_source',case u.is_first_login
            when 1 then '否' when 0 then '是' end as 'is_first_login',
            case c.is_huawei WHEN 0 THEN '四期客户' WHEN 1 THEN '三期客户' WHEN 2 THEN '三期无订单老客户' ELSE
            'undefied' END as 'IS_HUAWEI',c.boss_pro_order_code,c.global_discount,case c.payment_type when 1 then
            '预付费' when 2 then '后付费' end as 'payment_type' , c.contactor ,c.mng_phone,c.name as cust_name,
            c.email as cust_email,c.mobile as cust_phone,c.province,c.cont_phone,c.cont_email,c.cmcc_cust_mng,
            c.modify_time,c.create_time,c.boss_order_id from opm_user_user u left join opm_customer c
            on u.customer_id = c.id where c.id = "%s" """ % self.customerid.encode('utf-8')

        return utils.execsql(usersql, opconfig['OP_CLOUDMASTER_CONFIG'])

    def getbossloginfo(self):
        """get user information according to op_order_number"""
        usersql = """select * from opm_bossagent_log where op_order_number = "%s" order by id """ % self.op_order_number
        return utils.execsql(usersql, opconfig['OP_CLOUDMASTER_CONFIG'])

    def getbosslog_id(self):
        """get user information according to boss_order_id"""
        usersql = """select * from opm_bossagent_log where boss_order_id = "%s" order by id """ % self.boss_order_id
        return utils.execsql(usersql, opconfig['OP_CLOUDMASTER_CONFIG'])


class Newuserinfo(object):

    def __init__(self, _argument1, _argument2, _argument3, _argument4, _argument5):
        self.username = _argument1
        self.phone = _argument2
        self.email = _argument3
        self.customerid = _argument4
        self.new = _argument5

    def getuserinfo_all(self):
        """ get user information according to customer_id,username,phone,email"""
        usersql = """ select user_name from opm_user_user  where customer_id = '%s' and user_name = '%s'
            and phone = '%s' and email = '%s' """ % (self.customerid.encode('utf-8'),
                                                     self.username.encode('utf-8'),
                                                     self.phone.encode('utf-8'),
                                                     self.email.encode('utf-8'))
        return utils.execsql(usersql, opconfig['OP_CLOUDMASTER_CONFIG'])

    def newuserinfo_phone(self):
        """renew user information according to customer_id,username,phone,email"""
        usersql = """update opm_user_user set PHONE = '%s'  where customer_id = '%s' and user_name = '%s'
            and phone = '%s' and email = '%s' """ % (self.new.encode('%utf-8'),
                                                     self.customerid.encode('utf-8'),
                                                     self.username.encode('utf-8'),
                                                     self.phone.encode('utf-8'),
                                                     self.email.encode('utf-8'))
        return utils.execsql(usersql, opconfig['OP_CLOUDMASTER_CONFIG_WRITE'])
