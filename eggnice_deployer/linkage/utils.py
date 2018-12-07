# coding=utf-8
# --edit by lambda--

import os
import time
import shutil
import paramiko
import httplib
import urllib
import re
import json
import pymysql
import pymysql.cursors
import xlwt
import xlrd
from linkage import linkageconfig
from xlutils.copy import copy
import requests
import re
from linkage import loggers
from linkage.exceptions import ConnectionError, ReturnError, ExesqlError


class utils():
    """public utils for linkage"""
    def __init__(self):
        self.sessionsdict = {}

    def httpConnect(self, method, url, **kwargs):
        """Constructs a :class:`Request <Request>`, prepares it and sends it.
        Returns :class:`Response <Response>` object.

        :param method: method for the new :class:`Request` object.
        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary or bytes to be sent in the query
            string for the :class:`Request`.
        :param data: (optional) Dictionary, bytes, or file-like object to send
            in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the
            :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the
            :class:`Request`.
        :param cookies: (optional) Dict or CookieJar object to send with the
            :class:`Request`.
        :param files: (optional) Dictionary of ``'filename': file-like-objects``
            for multipart encoding upload.
        :param auth: (optional) Auth tuple or callable to enable
            Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param allow_redirects: (optional) Set to True by default.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol or protocol and
            hostname to the URL of the proxy.
        :param stream: (optional) whether to immediately download the response
            content. Defaults to ``False``.
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``.
        :param cert: (optional) if String, path to ssl client cert file (.pem).
            If Tuple, ('cert', 'key') pair.
        :rtype: requests.Response.json or requests.Response.text
        """
        kwargs.update(timeout=10)
        pattern = re.compile(r'//.+?/', re.I)
        ip_port = pattern.search(url).group()
        try:
            if ip_port not in self.sessionsdict:
                self.sessionsdict['ip_port'] = requests.Session()
            resp = self.sessionsdict['ip_port'].request(method, url, **kwargs)
        except Exception, e:
            loggers.error(str(e.args))
            raise ConnectionError(str(e.args))
        if resp.status_code is 200:
            try:
                return resp.json()
            except Exception:
                return resp.text
        else:
            loggers.error('return code not 200')
            raise ReturnError(resp.content)
            
    @staticmethod
    def sshConnect(Host, Username, Passwd, Port=22):
        '''ssh connect which return ssh object'''
        try:
            ssh_ob = paramiko.SSHClient()
            ssh_ob.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_ob.connect(Host, Port, username=Username, password=Passwd, timeout=50)
            return ssh_ob
        except BaseException as err:
            raise Exception('SSHconnerr:ssh %s@%s: %s' % (Username, Host, err))

    @staticmethod
    def sshClose(ssh_ob):
        '''close ssh connect object'''
        if ssh_ob:
            ssh_ob.close()

    @staticmethod
    def sshExeCmd(ssh_ob, Cmd, timeout=25):
        '''use ssh object to execute shell'''
        stdin, stdout, stderr = ssh_ob.exec_command(Cmd, bufsize=-1, timeout=timeout)
        return stdout.readlines()
        # return stdout.readlines(), stderr.readlines()

    @staticmethod
    def sshExeCmdwithError(ssh_ob, Cmd):
        """在远程ssh的主机执行命令,包含错误结果"""
        stdin, stdout, stderr = ssh_ob.exec_command(Cmd)
        return stdout.readlines(), stderr.readlines()

    @staticmethod
    def checkip(ip):
        '''check ip format or not'''
        p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
        if p.match(ip):
            return True
        else:
            return False

    @staticmethod
    def execsql(sql, databaseconf):
        '''connect mysql return result'''
        try:
            conn = pymysql.connect(**databaseconf)
            with conn.cursor() as cursor:
                    cursor.execute(sql)
                    return cursor.fetchall()
        except Exception, e:
            raise ExesqlError(str(e.args)+'Connecterr:mysql -u%s -p%s -h%s -D%s have error'
                                                                             % (databaseconf['user'],
                                                                                databaseconf['password'],
                                                                                databaseconf['host'],
                                                                                databaseconf['db']))
        finally:
            if not databaseconf.get('autocommit'):
                if conn or cursor:
                    cursor.close()
                    conn.commit()
                    conn.close()


class fontclours():
    ''' font colour'''

    def __init__(self):
        self.HIGH = '\033[1m'
        self.FLASH = '\033[5m'
        self.BLUE = '\033[34m'
        self.PURPLE = '\033[35m'
        self.GREEN = '\033[32m'
        self.RED = '\033[31m'
        self.YELLOW = '\033[33m'
        self.BLACK = '\033[30m'
        self.WHITE = '\033[37m'
        self.BROWN = '\033[33m'
        self.CYAN = '\033[36m'
        self.FLASH_RED = '\033[5;31m'
        self.END = '\033[0m'

    def setfont(self, name, font):
        self.name = font


class SheetExitException(Exception):
    'error for index sheet'
    def __init__(self, err):
        Exception.__init__(self, err)


class wexcel():
    'method for write excel'
    def __init__(self, filename, save_path=None):
        self.filename = ''.join([filename, '.xls'])
        self.workbook = xlwt.Workbook(encoding='utf-8')
        if not save_path:
            save_path = os.getcwd()
        self.path = save_path + '/'
        if not os.path.isdir(self.path):
            raise Exception('%s is not a dir' % self.path)

    def addsheet(self, sheetname):
        try:
            self.workbook.sheet_index(sheetname)
            raise SheetExitException('the %s sheet is exit' % sheetname)
        except SheetExitException:
            raise
        except Exception as err:
            if err.message == 'Formula: unknown sheet name %s' % sheetname:
                return self.workbook.add_sheet(sheetname, cell_overwrite_ok=True)

    def getsheet(self, sheetname):
        return self.workbook.sheet_index(sheetname)

    def write(self, sheet, r, c, data, style=None):
        if style:
            sheet.write(r, c, data, style)
        else:
            sheet.write(r, c, data)

    def save(self):
        self.workbook.save(self.filename)
        dest = self.path + self.filename
#        shutil.copyfile(self.filename, dest)
        shutil.move(self.filename, dest)


def exetime(button=True):
    'a decorator to writedown a function run time'
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not button:
                data = func(*args, **kwargs)
                return data
            totime = time.time()
            data = func(*args, **kwargs)
            runtime = time.time() - totime
            with open(linkageconfig['RUNTIMEFILE'], 'a') as f:
                mess = '%s ---func:%s ---runtime:%s\n' % (time.strftime("%Y-%m-%d %H:%M:%S",
                                                          time.localtime()), func.__name__, runtime)
                f.write(mess)
            return data
        return wrapper
    return decorator


