#! /usr/bin/env python
"""WSDL parsing services package for Web Services for Python."""

ident = "$Id$"

import WSDLTools
import XMLname
import logging

class Base:
    def __init__(self, module=__name__):
        self.logger = logging.getLogger('%s-%s(%x)' %(module, self.__class__, id(self)))
