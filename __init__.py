#! /usr/bin/env python
"""WSDL parsing services package for Web Services for Python."""

ident = "$Id$"

import WSDLTools
import XMLname
from ConfigParser import NoSectionError
LOGGING = 'logging.txt'

from logging import getLogger
import logging
import logging.config

try:
    logging.config.fileConfig(LOGGING)
except (NoSectionError,), ex:
    logging.basicConfig()

class Base:
    def __init__(self, module=__name__):
        self.logger = getLogger('%s-%s(%x)' %(module, self.__class__, id(self)))

