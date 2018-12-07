# *_* coding: utf-8 *_*
# _author: eggnice

from datetime import datetime
from linkage import loggers

class tools(object):
    """
    ec的一些工具类使用(模块)单例模式
    """
    def __init__(self):
        pass

    @staticmethod
    def utctime_to_local(u_time):
        if isinstance(u_time, str):
            try:
                u_time = u_time.rstrip('Z')
                u_time = datetime.strptime(u_time, "%Y-%m-%dT%H:%M:%S.%f")
            except ValueError, e:
                u_time = datetime.strptime(u_time, "%Y-%m-%dT%H:%M:%S")
        local_tm = datetime.fromtimestamp(0)
        utc_tm = datetime.utcfromtimestamp(0)
        offset = local_tm - utc_tm
        return u_time + offset

    @staticmethod
    def str_to_unicode(l_ist):
        """
        把list中的str转换为unicode
        :param l_ist: list
        :return :注意这是在list基础上更改所以不需要返回,因为直接更改了list
        """
        for i in range(len(l_ist)):
            if isinstance(l_ist[i], list):
                tools.str_to_unicode(l_ist[i])
            elif isinstance(l_ist[i], str):
                l_ist[i] = l_ist[i].decode('utf-8')

#单例模式运行该工具类, 避免多次实例化
tools = tools()

