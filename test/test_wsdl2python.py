#!/usr/bin/env python

############################################################################
# David W. Robertson, LBNL
# See LBNLCopyright for copyright notice!
###########################################################################
import sys, ConfigParser, unittest
import StringIO
from ZSI import wsdl2python
from ZSI.wstools.WSDLTools import WSDLReader
import utils

"""
Unittest for the wsdl2python class
"""

class Wsdl2pythonTest(unittest.TestCase):
    """Test case for wsdl2python.WriteServiceModule
    """

    def __init__(self, methodName='runTest'):
        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
        global configLoader

            # not thread safe
        self.path = configLoader.nameGenerator.next()
        print self.path
        sys.stdout.flush()
        self.testdiff = utils.TestDiff(self)

    def tearDown(self):
        self.testdiff.close()

    def __str__(self):
        teststr = unittest.TestCase.__str__(self)
        if hasattr(self, "path"):
            return "%s: %s" % (teststr, self.path )
        else:
            return "%s" % (teststr)


    def test_Xmethods_services(self):
        try:
            wsdl = utils.setUpWsdl(self.path)
        except:
            self.path = self.path + ": load failed, unable to start"
            raise
        codegen = wsdl2python.WriteServiceModule(wsdl)
        f_types, f_services = codegen.get_module_names()
        hasSchema = len(codegen._wa.getSchemaDict())

        if hasSchema:
            strFile = StringIO.StringIO()
            self.testdiff.setDiffFile(f_types + ".py")
            try:
                codegen.write_service_types(f_types, strFile)
            except:
                self.path = self.path + ": write_service_types"
                raise
            if strFile.closed:
                print "trouble"
            self.testdiff.failUnlessEqual(strFile)
            strFile.close()

        strFile = StringIO.StringIO()
        self.testdiff.setDiffFile(f_services + ".py")
        try:
            signatures = codegen.write_services(f_types,
                             f_services, strFile, hasSchema)
        except:
            self.path = self.path + ": write_services"
            raise
        self.testdiff.failUnlessEqual(strFile)
        strFile.close()



def makeTestSuite(section=None):
    global configLoader

    suite = unittest.TestSuite()
    configLoader = utils.MatchTestLoader(False, "config.py", "Wsdl2pythonTest")
    if not section:
        found = configLoader.setSection(sys.argv)
        if not found:
            configLoader.setSection("services_by_http")
    else:
        configLoader.setSection(section)
    suite.addTest(configLoader.loadTestsFromConfig(Wsdl2pythonTest))
    return suite


def foo():
    loader = utils.MatchTestLoader(False, "config.py", "makeTestSuite")
    unittest.main(defaultTest="makeTestSuite", testLoader=loader)
                  

if __name__ == "__main__" : foo()
