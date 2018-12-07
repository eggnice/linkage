# *_* coding: utf-8 *_*
#　_author: eggnice

import jinja2
import sys
import threading
from linkage import linkageconfig
from linkage.openstack.ec.built.getTemplateData import getTemplateData
from linkage import loggers
#import time


class builtVm(object):
    def __init__(self, vminstance, order_list):
        """
        输入已经初始化的blockVm实例
        :param vminstance: object
        """
        self.vminstance = vminstance
        self.template_data = getTemplateData(vminstance)
        self.order_part = {'1': lambda :self.get_data('vmdata'),
                           '2': lambda :self.get_data('pmdata'),
                           '3': lambda :self.get_data('networkdata'),
                           '4': lambda :self.get_data('imagedata'),
                           '5': lambda :self.get_data('opdata'),
                           '6': lambda :self.get_data('volumedata'),
                           '7': lambda :self.get_data('actiondata'),
                           '8': lambda :self.get_data('checkdata')
                           }
        self.order_list = order_list
        self.start()

    def get_data(self, name):
        """
        根据模板获取数据
        :param name: 或者数据的模板名
        """
        try:
            method = getattr(self.template_data, 'get_'+name)
            self.__dict__[name]  = method()
        except Exception, e:
            loggers.error(str(e))
            print '获取数据出错了,赶紧找作者祭天:%s' % str(e)
            sys.exit(1)

    def start_threads(self):
        """
        根据输入的order_list使用多线程去调用1-8中的部分
        :param order_list: list
        """
        threads = [threading.Thread(target=self.order_part[one]) for one in self.order_list]
        for one_th in threads:
            one_th.start()
        for onet in threads:
            if onet.isAlive():
                onet.join()

    def start_built_out(self):
        """根据输入的模板序号进行输出"""
        env =  jinja2.Environment(loader=jinja2.FileSystemLoader(linkageconfig['TEMPLATES_DIR']))
        templates = {'1': lambda x: env.get_template('vm_template.txt').render(num=x, v=self.vmdata),
                     '2': lambda x: env.get_template('pm_template.txt').render(num=x, v=self.pmdata),
                     '3': lambda x: env.get_template('network_template.txt').render(num=x, v=self.networkdata),
                     '4': lambda x: env.get_template('image_template.txt').render(num=x, v=self.imagedata),
                     '5': lambda x: env.get_template('op_template.txt').render(num=x, v=self.opdata),
                     '6': lambda x: env.get_template('volume_template.txt').render(num=x, v=self.volumedata),
                     '7': lambda x: env.get_template('action_template.txt').render(num=x, v=self.actiondata),
                     '8': lambda x: env.get_template('check_template.txt').render(num=x, v=self.checkdata)
                     }
        for i in range(len(self.order_list)):
            print templates[self.order_list[i]](str(i+1)+'.')
        self.vminstance.sshd.close()

    def start(self):
        """
        表演开始了
        """
        self.start_threads()
        self.start_built_out()
