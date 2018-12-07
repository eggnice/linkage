# -*- coding: utf-8 -*-

"""
linkage.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of Linkage' exceptions.
"""
#from linkage import loggers

class BaseError(Exception):
    def __init__(self, *args):
        Exception.__init__(self)
        self.args = args

class ConnectionError(BaseError):
    """connection host error"""

class ReturnError(BaseError):
    """http return not 200."""

class ConnectionError(BaseError):
    """A Connection error occurred."""

class ExesqlError(BaseError):
    """connection database or exe sql error"""

class ConnectionKeystoneError(BaseError):
    """request keystone occurre a error"""

class ConnectionGlanceError(BaseError):
    """request glance occurre a error"""

class ConnectionCinderError(BaseError):
    """request cinder occurre a error"""

class ConnectionIdentityError(BaseError):
    """request identity occurre a error"""

class ConnectionNeutronError(BaseError):
    """request neutron occurre a error"""

class ConnectionNovaError(BaseError):
    """request nova occurre a error"""

class ReturnNone(BaseError):
    """function return None"""

class LogicError(BaseError):
    """"""

class GetPmInfoError(BaseError):
    """"""

class GetUserInfoError(BaseError):
    """"""

class GetPortInfoError(BaseError):
    """"""

class GetVolumeInfoError(BaseError):
    """"""

class GetImageInfoError(BaseError):
    """"""

class GetSelfCheckInfoError(BaseError):
    """"""

class GetFloatingIpInfoError(BaseError):
    """"""

class GetActionInfoError(BaseError):
    """"""

class GetVncInfoError(BaseError):
    """"""

class GetFlavorInfoError(BaseError):
    """"""

class InitFloatingIpError(BaseError):
    """"""

class ErrorMessage(BaseError):
    """"""
