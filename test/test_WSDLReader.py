#!/usr/bin/env python

############################################################################
# Joshua R. Boverhof, David W. Robertson, LBNL
# See LBNLCopyright for copyright notice!
###########################################################################

import unittest, sys, copy
from ConfigParser import NoOptionError
import utils
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


def makeTestSuite(section=None):
    global configLoader

    suite = unittest.TestSuite()
    configLoader = utils.MatchTestLoader(False, "config.py", "WSDLReaderTestCase")
    if not section:
        found = configLoader.setSection(sys.argv)
        if not found:
            configLoader.setSection("services_by_http")
    else:
        configLoader.setSection(section)
    suite.addTest(configLoader.loadTestsFromConfig(WSDLReaderTestCase))
    return suite


def main():
    loader = utils.MatchTestLoader(False, None, "makeTestSuite")
    unittest.main(defaultTest="makeTestSuite", testLoader=loader)
                  

if __name__ == "__main__" : main()
