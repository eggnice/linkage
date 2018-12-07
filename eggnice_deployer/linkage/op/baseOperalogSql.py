#!/usr/bin/env python
# -*- coding: utf-8 -*-

# bcop sql query

from linkage.utils import utils
from linkage import opconfig
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def getUserId(username):
    """get user_id according to username"""
    usersql = """ SELECT ID from opm_user_user WHERE USER_NAME = "%s" """ % username
    return utils.execsql(usersql, opconfig['OP_CLOUDMASTER_CONFIG'])


def getOperalog(user_id, begin_time, end_time):
    """get operation log according to user_id"""
    operalogsql = """SELECT ID, `ACTION`, OPERATOR_TIME, CUSTOMER_ID, USER_ID, EXTRA, POOL_ID, RESULT_CODE, COST_TIME,
RESULT_MSG FROM os_biz_operator_log WHERE USER_ID = "%s" AND OPERATOR_TIME BETWEEN "%s" AND "%s" """ \
               % (user_id, begin_time, end_time)
    return utils.execsql(operalogsql, opconfig['OP_OPENSTACK_CONFIG'])
