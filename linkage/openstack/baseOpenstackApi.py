# *_* coding: utf-8 *_*
# __author__: eggnice

"""base openstack tools init token"""

from functools import wraps
from linkage import loggers
import os
import datetime
from linkage import Utils
from linkage import ecconfig
from linkage import linkageconfig
from linkage.exceptions import (ConnectionError, ReturnError, ConnectionKeystoneError,
                                ConnectionGlanceError,ConnectionCinderError,ConnectionIdentityError,
                                ConnectionNeutronError,ConnectionNovaError)


class baseOpenstackApi(object):
    """baseopenstackapi class init token_id and tenant_id save them at token.txt
       调用openstack基础,使用密码方式得到token_id,tenant_id"""
    NOVA_HOST = ecconfig['NOVA_HOST']
    GLANCE_HOST = ecconfig['GLANCE_HOST']
    CINDER_HOST = ecconfig['CINDER_HOST']
    NEUTRON_HOST = ecconfig['NEUTRON_HOST']
    KEYSTONE_HOST = ecconfig['KEYSTONE_HOST']
    httpglance = 'http://%s' % GLANCE_HOST
    httpcinder = 'http://%s' % CINDER_HOST
    httpnova = 'http://%s' % NOVA_HOST
    httpneutron = 'http://%s' % NEUTRON_HOST
    httpkeystone = 'http://%s' % KEYSTONE_HOST

    def __init__(self):
        self.TENANT_NAME = ecconfig['TENANT_NAME']
        self.USER_NAME = ecconfig['USER_NAME']
        self.PASSWORD = ecconfig['PASSWORD']
        self.TOKEN_FILE = linkageconfig['TOKEN_FILE']
        if not os.path.isfile(self.TOKEN_FILE):
            dir = '/'.join(self.TOKEN_FILE.split('/')[:-1])
            try:
                os.makedirs(dir)
            except:
                pass
            os.mknod(self.TOKEN_FILE)
        with open(self.TOKEN_FILE, 'r') as f:
            mess = [onel.rstrip('\n') for onel in f.readlines()]
        if len(mess) is 3:
            try:
                expires_time = datetime.datetime.strptime(mess[0].strip('Z'), '%Y-%m-%dT%H:%M:%S')
            except ValueError:
                expires_time = datetime.datetime.strptime(mess[0].strip('Z'), '%Y-%m-%dT%H:%M:%S.%f')
            if expires_time > datetime.datetime.utcnow() + datetime.timedelta(minutes=5):
                baseOpenstackApi.tenant_id = mess[1]
                baseOpenstackApi.token_id = mess[2]
            else:
                self._get_token()
        else:
            self._get_token()

    def _get_token(self):
            try:
                data = self.connKeystone(api='/v2.0/tokens',tenant_name=self.TENANT_NAME,
                                     user_name=self.USER_NAME,password=self.PASSWORD)
                expires_time = data['access']['token']['expires'].strip('Z')
                baseOpenstackApi.token_id = data['access']['token']['id']
                baseOpenstackApi.tenant_id = data['access']['token']['tenant']['id']
                self.rewrite_tokenfile(expires_time, self.tenant_id, self.token_id)
            except Exception, e:
                loggers.error(str(e.args))
                raise ConnectionKeystoneError(str(e.args))

    def rewrite_tokenfile(self, expires_time, tenant_id, token_id):
        """write expires_time,tenant_id,token_id to file"""
        with open(self.TOKEN_FILE, 'w') as f:
            f.write(expires_time+'\n'+tenant_id+'\n'+token_id)

    def connKeystone(self, api, **kwargs):
        """connect keystone for user return TOKEN_ID,tennat,expires_time"""
        method = "POST"
        url = self.httpkeystone + api
        json = {"auth": {"tenantName":kwargs.pop('tenant_name'),
                         "passwordCredentials":{"username":kwargs.pop('user_name'),
                                                "password":kwargs.pop('password')}}}
        headers = {"Content-Type": 'application/json'}
        try:
            return Utils.httpConnect(method=method, url=url, headers=headers, json=json, **kwargs)
        except Exception, e:
            loggers.error(str(e.args))
            raise ConnectionKeystoneError(str(e.args))


class openstackapi(baseOpenstackApi):
    """
    openstack api include nava,cinder,neutron,identity,实例化时调用父类进行token和相关参数初始化，主要是为子类提供方法
    :param Method: reqeust method
    :param api: api of openstack
    :param data: body data for request
    :param json: body josn for request
    :param [other]: see Utils.request method
    :return json or text: request by api, if json other text
    """
    def dec(func):
        """inner method"""
        @wraps(func)
        def indec(*args, **kwargs): #此处的arg[0]是子类的self
            method = str(args[1]).upper()
            api = args[2]
            kwargs.setdefault('headers', {'X-Auth-Token': args[0].token_id})
            if not kwargs.get('headers').has_key('X-Auth-Token'):
                kwargs['headers'].update({'X-Auth-Token': args[0].token_id})
            return func(args[0], method, api, **kwargs)
        return indec

    @dec
    def connGlance(self, Method, api, **kwargs):
        """ to connGlance with api"""
        url = self.httpglance + api
        headers = kwargs.pop('headers')
        try:
            return Utils.httpConnect(method=Method, url=url, headers=headers, **kwargs)
        except Exception, e:
            loggers.error(str(e.args))
            raise ConnectionGlanceError(str(e.args))

    @dec
    def connCinder(self, Method, api, **kwargs):
        """ connCinder """
        url = self.httpcinder + api
        headers = kwargs.pop('headers')
        try:
            return Utils.httpConnect(method=Method, url=url, headers=headers, **kwargs)
        except Exception, e:
            loggers.error(str(e.args))
            raise ConnectionCinderError(str(e.args))

    # connect Identity return what has get from api
    @dec
    def connIdentity(self, Method, api, **kwargs):
        """ connIdentity """
        url = self.httpkeystone + api
        headers = kwargs.pop('headers')
        try:
            return Utils.httpConnect(method=Method, url=url, headers=headers, **kwargs)
        except Exception, e:
            loggers.error(str(e.args))
            raise ConnectionIdentityError(str(e.args))

    # connect neutron return what has get from api
    @dec
    def connNeutron(self, Method, api, **kwargs):
        """ connNeutron """
        url = self.httpneutron + api
        headers = kwargs.pop('headers')
        try:
            return Utils.httpConnect(method=Method, url=url, headers=headers, **kwargs)
        except Exception, e:
            loggers.error(str(e.args))
            raise ConnectionNeutronError(str(e.args))

    # connect nova return what has get from api
    @dec
    def connNova(self, Method, api, **kwargs):
        """ connNova """
        url = self.httpnova + api
        headers = kwargs.pop('headers')
        try:
            return Utils.httpConnect(method=Method, url=url, headers=headers, **kwargs)
        except Exception, e:
            loggers.error(str(e.args))
            raise ConnectionNovaError(str(e.args))
