#!/usr/bin/env python
import unittest, sys
from ConfigParser import ConfigParser
from ZSI.wstools.WSDLTools  import WSDLReader
from test_wsdl import WSDLToolsTestCase, NETWORK, STANDALONE

CONFIG = None

class AmazonTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'amazon'
        self.loadFromConfig(CONFIG)

class AirportTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'airport'
        self.loadFromConfig(CONFIG)

class OGSITestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'ogsi'
        self.loadFromConfig(CONFIG)

CASES = [AmazonTestCase, AirportTestCase, OGSITestCase]
def makeNetworkSuite():
    return getSuite(NETWORK)

def makeStandAloneSuite():
    return getSuite(STANDALONE)

def getSuite(section):
    tests = []
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    for case in CASES:
        case.section = section
        test = loader.loadTestsFromTestCase(case)
        tests.append(test)
    suite.addTests(tests)
    return suite

def main():
    global CONFIG
    from test_wstools import CONFIG_FILE
    CONFIG = ConfigParser()
    CONFIG.read(CONFIG_FILE)
    unittest.TestProgram(defaultTest='makeStandAloneSuite')

if __name__ == "__main__" : main()
