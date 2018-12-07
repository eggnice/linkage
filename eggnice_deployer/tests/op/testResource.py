#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import unittest
from linkage.op import vmBlock, vlbBlock, fipBlock, vfwBlock, vdiskBlock, secgroupBlock
from linkage.op import mplsBlock, hscBlock, ipsecBlock, icpBlock
from linkage.op.built import resourceService

class Resourcetest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVm(self):
        self.assertEqual(vmBlock.Vm("92ab01c7-cc65-4f94-a7ac-7226d744050a").name,
                         "test0410", 'get vmInfo fail')

    def testVlb(self):
        self.assertEqual(vlbBlock.Vlb('940b0dd3-774f-4637-a19f-bbe73b9321a5').name, 'lalb01', 'get vlb info fail')

    #def testVip(self):
        #self.assertEqual(vipBlock.Vip('112.35.0.216').name, '112.35.0.216', 'get vip info fail')

    def testVfw(self):
        self.assertEqual(vfwBlock.Vfw('CIDC-U-e34ef8b6e5e24b60a8dffca6e44554c4').id,
                         '635400b1-4466-40cc-94c3-f207180501fb', 'get Vfw info fail')

    def testVdisk(self):
        self.assertEqual(vdiskBlock.Vdisk('b23b3ff2-4b27-4c8a-bb35-d725ebf07f88').host_id,
                         'f17305d5-fc29-49b2-aad8-ebbf10d82dee', 'get vdisk fail')

    def testSecgroup(self):
        self.assertEqual(secgroupBlock.SecGroup('2aa12f73-8f3a-41fb-a3e4-e99e348de304').name, 'default',
                         'get secgroup fail')

    def testMpls(self):
        self.assertEqual(mplsBlock.Mpls('2093193f4ea84162b8566d0511ccd09b').mpls_name, 'vpn01', 'get mpls fail')

    def testHsc(self):
        self.assertEqual(hscBlock.Hsc('013a42ee596f49c3bcb6caa97255f6f5').hsc_name, 'ddd', 'get hsc fail')

    def testIpsec(self):
        self.assertEqual(ipsecBlock.Ipsec('0a86e36e-d06b-4d53-b5a1-f0a0e207f76b').name, 'cjl_test1', 'get ipsec fail')

    def testIcp(self):
        self.assertEqual(icpBlock.Icp('112.35.27.163').icp_id, '1723563086943343749', 'get icp fail')

    def testResource(self):
        self.assertEqual(resourceService.vm_check("92ab01c7-cc65-4f94-a7ac-7226d744050a"), 1, 'get vm fail')

