#!/usr/bin/env python
import unittest, sys
from ConfigParser import ConfigParser
from ZSI.wstools.WSDLTools  import WSDLReader
from test_wsdl import WSDLToolsTestCase, NETWORK, STANDALONE

CONFIG = None

class HomeLandSecurityTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'homelandsecurity'
        self.loadFromConfig(CONFIG)

class Rtf2htmlTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'rtf2html'
        self.loadFromConfig(CONFIG)

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

class BooksTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'books'
        self.loadFromConfig(CONFIG)

class DistanceTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'distance'
        self.loadFromConfig(CONFIG)

class FreeDBTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'freedb'
        self.loadFromConfig(CONFIG)

class GlobalWeatherTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'globalweather'
        self.loadFromConfig(CONFIG)

class IHaddockTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'IHaddock'
        self.loadFromConfig(CONFIG)

class Ip2geoTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'ip2geo'
        self.loadFromConfig(CONFIG)

class MagicTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'magic'
        self.loadFromConfig(CONFIG)

class QueryTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'query'
        self.loadFromConfig(CONFIG)

class RateInfoTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'RateInfo'
        self.loadFromConfig(CONFIG)

class SHA1EncryptTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'SHA1Encrypt'
        self.loadFromConfig(CONFIG)

class SiteInspectTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'siteInspect'
        self.loadFromConfig(CONFIG)

class SolveSystemsTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'SolveSystem'
        self.loadFromConfig(CONFIG)

class TemperatureServiceTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'TemperatureService'
        self.loadFromConfig(CONFIG)

class USweatherTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'usweather'
        self.loadFromConfig(CONFIG)

class Zip2geoTestCase(WSDLToolsTestCase):
    def test(self):
        self.option = 'zip2geo'
        self.loadFromConfig(CONFIG)

CASES = [AirportTestCase, 
         AmazonTestCase, 
         BooksTestCase,
         DistanceTestCase, 
         FreeDBTestCase, 
         GlobalWeatherTestCase,
         HomeLandSecurityTestCase,
         IHaddockTestCase, 
         Ip2geoTestCase, 
         MagicTestCase,
         OGSITestCase, 
         QueryTestCase, 
         RateInfoTestCase, 
         Rtf2htmlTestCase,
         SHA1EncryptTestCase, 
         SiteInspectTestCase, 
         SolveSystemsTestCase,
         TemperatureServiceTestCase,
         USweatherTestCase, 
         WSDLToolsTestCase, 
         Zip2geoTestCase]

def makeNetworkSuite():
    return getSuite(NETWORK)

def makeStandAloneSuite():
    return getSuite(STANDALONE)

def getSuite(section):
    tests = []
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    WSDLToolsTestCase.section = section
    for case in CASES:
        #case.section = section
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
