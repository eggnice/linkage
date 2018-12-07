#!/usr/bin/python
# coding=utf-8
# --- edit by lambda ---
import sys
import os
import types


class conf(dict):
    '''to set process config default is config.py'''
    def __init__(self):
        self.root_path = '/apps/conf/linkage/instance/'
        # self.from_object('config')
        # print self.root_path

    def import_string(self, import_name, silent=False):
        # force the import name to automatically convert to strings
        # __import__ is not able to handle unicode strings in the fromlist
        # if the module is a package
        import_name = str(import_name).replace(':', '.')
        try:
            try:
                __import__(import_name)
            except ImportError:
                if '.' not in import_name:
                    raise
            else:
                return sys.modules[import_name]

            module_name, obj_name = import_name.rsplit('.', 1)
            try:
                module = __import__(module_name, None, None, [obj_name])
            except ImportError:
                # support importing modules not yet set up by the parent module
                # (or package for that matter)
                module = self.import_string(module_name)

            try:
                return getattr(module, obj_name)
            except AttributeError as e:
                raise ImportError(e)

        except ImportError as e:
            if not silent:
                raise
                # raise(
                #    ImportStringError,
                #    ImportStringError(import_name, e),
                #    sys.exc_info()[2])

    def from_object(self, obj):
        '''import a python object'''
        if isinstance(obj, str):
                obj = self.import_string(obj)
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)
            #    print key
            #    print getattr(obj,key)

    def from_pyfile(self, filename, silent=False):
        '''import object is file which like from_object'''
        filename = os.path.join(self.root_path, filename)
        d = types.ModuleType('config')
        d.__file__ = filename
        try:
            with open(filename, mode='rb') as config_file:
                exec(compile(config_file.read(), filename, 'exec'), d.__dict__)
        except IOError as e:
            # if silent and e.error in (error.ENOENT, error.EISDIR):
            if silent and e.error:
                return False
            e.strerror = 'Unable to load configuration file (%s)' % e.strerror
            raise
        self.from_object(d)
        return True

    def from_envvar(self, variable_name, silent=False):
        '''import a var which you can export in your env like: export variable_name=your config file path'''
        rv = os.environ.get(variable_name)
        if not rv:
            if silent:
                return False
            raise RuntimeError('The environment variable %r is not set '
                               'and as such configuration could not be '
                               'loaded.  Set this variable and make it '
                               'point to a configuration file' %
                               variable_name)
        return self.from_pyfile(rv, silent=silent)
