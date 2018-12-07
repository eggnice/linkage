#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import unittest
from linkage.op import userBlock


class Usertest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUser(self):
        user = userBlock.userInfo('13802883437')
        user.userInfo_phone()
        self.assertEqual(user.cust_status, "注册待归档", 'get userinfo fail')
    def testbosslog(self):
        bosslog = userBlock.bossloginfo('0001406100004921001')
        bosslog.bossloginfo()
        self.assertEqual(bosslog.bosslog_num,6,'get bosslog fail') 
