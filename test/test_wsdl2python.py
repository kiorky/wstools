############################################################################
# David W. Robertson, LBNL
# See Copyright for copyright notice!
###########################################################################
import sys, ConfigParser, unittest
import StringIO
from ZSI import wsdl2python
from ZSI.wstools.WSDLTools import WSDLReader
import utils

"""
Unittest for the wsdl2python class
"""

def setUpWsdl(path):
    if path[:7] == 'http://':
        wsdl = WSDLReader().loadFromURL(path)
    else:
        wsdl = WSDLReader().loadFromFile(path)
    return wsdl


class Wsdl2pythonTest(unittest.TestCase):
    """Test case for wsdl2python.WriteServiceModule
    """

    def __init__(self, methodName='runTest'):
        global configLoader

        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
            # not thread safe
        self.path = configLoader.nameGenerator.next()
        print self.path
        sys.stdout.flush()
        self.testdiff = utils.TestDiff(self)
        self.wsdl = configLoader.nameGenerator.next()

    def tearDown(self):
        if self.wsdl is not None:
            del self.wsdl
        self.testdiff.close()
 
    def __str__(self):
        teststr = unittest.TestCase.__str__(self)
        if hasattr(self, "path"):
            return "%s: %s" % (teststr, self.path )
        else:
            return "%s" % (teststr)


    def do_diffs(self, choice):
        self.failUnless(self.wsdl is not None, "Unable to start, load failed")

        codegen = wsdl2python.WriteServiceModule(self.wsdl)
        f_types, f_services = codegen.get_module_names()

        strFile = StringIO.StringIO()
        if choice == "service_types":
            self.testdiff.setDiffFile(f_types + ".py")
            codegen.write_service_types(f_types, strFile)
        else:
            self.testdiff.setDiffFile(f_services + ".py")
            codegen.write_services(f_types, f_services, strFile)
        self.testdiff.failUnlessEqual(strFile)
        strFile.close()

    def test_Xmethods_service_types(self):
            # add exception for url not found
        self.do_diffs("service_types")

    def test_Xmethods_services(self):
        self.do_diffs("services")


def makeTestSuite(topLevel=False, config=None):
    global configLoader

    suite = unittest.TestSuite()
    if not hasattr(sys.modules[__name__], "configLoader"):
        if not config:
            configLoader = utils.MatchTestLoader(False, "config.py",
                                         "Wsdl2pythonTest")
        else:
            configLoader = config
    configLoader.testMethodPrefix = "test"
    suite.addTest(configLoader.loadTestsFromConfig(Wsdl2pythonTest,
                                                   "services_by_http",
                                                   valueFunc = setUpWsdl))
    return suite


def main():
    global configLoader

    configLoader = utils.MatchTestLoader(False, "config.py", "makeTestSuite")
    unittest.main(defaultTest="makeTestSuite", testLoader=configLoader)
                  
if __name__ == "__main__" : main()
