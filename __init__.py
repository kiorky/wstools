#! /usr/bin/env python
"""WSDL parsing services package for Web Services for Python."""

ident = "$Id$"

import WSDLTools
import XMLname
from ConfigParser import NoSectionError
LOGGING = 'logging.txt'

try:
    from logging import getLogger
    import logging
except ImportError, ex:
    class logger:
        '''Default logger for python2.2
        '''
        def __init__(self, name):
            self.name = name
            self.out = out

        def write(self, arg):
            self.out.write(arg)

        def _write(self, severity, msg, *args, **kw):
            self.write('%s:  %s  -- %s' %(severity, self.name, msg))

        def error(self, msg, *args, **kw):
            self._write('ERROR', msg, *args, **kw)

        def warning(self, msg, *args, **kw):
            self._write('WARNING', msg, *args, **kw)

        def critical(self, msg, *args, **kw):
            self._write('CRITICAL', msg, *args, **kw)

    def getLogger(name):
        return logger(name)

else:
    import logging.config
    try:
        logging.config.fileConfig(LOGGING)
    except (NoSectionError,), ex:
        logging.basicConfig()

class Base:
    def __init__(self, module=__name__):
        self.logger = getLogger('%s-%s(%x)' %(module, self.__class__, id(self)))

