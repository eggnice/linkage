#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from linkage.op import orderBlock
from linkage.op.built import orderService

class Ordertest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrder(self):
        self.assertEqual(orderBlock.Order("CIDC-O-03a8fe7e3fc6446d86ff89a443b12329").cmp_customer_id,
                         "CIDC-C-0000002292", 'get orderInfo fail')

    def testExt(self):
        self.assertEqual(orderBlock.Ext("CIDC-O-03a8fe7e3fc6446d86ff89a443b12329").ext_num, 2, 'get orderextInfo fail')

    def testArchive(self):
        self.assertEqual(orderBlock.Archive("23b0e3510a674b7e8dc30f716d521612").archive_num, 2, 'get orderarchiveInfo fail')

    def testLog(self):
        self.assertEqual(orderBlock.Log("23b0e3510a674b7e8dc30f716d521612").log_num, 5, 'get logInfo fail')


    def testOrderService(self):
        self.assertEqual(orderService.ordercheck("CIDC-O-aa33cfcc775049698b137335122e9f52"), 4, 'order check fail')
