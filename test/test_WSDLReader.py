#!/usr/bin/env python

############################################################################
# Joshua R. Boverhof, David W. Robertson, LBNL
# See Copyright for copyright notice!
###########################################################################

import unittest, sys, copy
from ConfigParser import NoOptionError
from pyGridWare.test import utils
from ZSI.wstools.WSDLTools  import WSDLReader


"""
Unittest for the wstools WSDLReader class
"""


class WSDLReaderTestCase(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        global configLoader

        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
            # not thread safe
        self.path = configLoader.nameGenerator.next()
        print self.path
        sys.stdout.flush()

    def __str__(self):
        teststr = unittest.TestCase.__str__(self)
        if hasattr(self, "path"):
            self.printedOut = True
            return "%s: %s" % (teststr, self.path )
        else:
            return "%s" % (teststr)

    def test_WSDLReader(self):
        if self.path[:7] == 'http://':
            wsdl = WSDLReader().loadFromURL(self.path)
        else:
            wsdl = WSDLReader().loadFromFile(self.path)


def makeTestSuite(topLevel=False, config=None):
    global configLoader

    suite = unittest.TestSuite()
    if not hasattr(sys.modules[__name__], "configLoader"):
        if not config:
            configLoader = utils.MatchTestLoader(False, "config.py",
                                         "WSDLReaderTestCase")
        else:
            configLoader = config
    configLoader.testMethodPrefix = "test"
        # need to have as command-line argument
    suite.addTest(configLoader.loadTestsFromConfig(WSDLReaderTestCase,
                                                   "services_by_http"))
    return suite


def main():
    global configLoader

    configLoader = utils.MatchTestLoader(False, "config.py", "makeTestSuite")
    unittest.main(defaultTest="makeTestSuite", testLoader=configLoader)
                  
if __name__ == "__main__" : main()
