#!/usr/bin/env python
import unittest, sys
from ConfigParser import NoOptionError
from ZSI.wstools.WSDLTools  import WSDLReader
from ZSI.wstools.Utility import DOM

CONFIG = None
NETWORK = 'services_by_http'
STANDALONE = 'services_by_file'

class WSDLToolsTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
        pass

    def tearDown(self):
        if self.wsdl:
            self.wsdlServices()
            self.wsdlMessages()
            self.wsdlPortTypes()
            self.wsdlBindings()
            self.wsdlImports()
            self.wsdlExtensions()
            self.wsdlTypes()

    def loadFromConfig(self, config=CONFIG):
        try:
            print config
            path = config.get(self.section, self.option)
        except NoOptionError, ex:
            self.wsdl = None
        else:
            if path[:7] == 'http://':
                self.loadFromURL(url=path)
            else:
                self.loadFromFile(file=path)
 
    def loadFromFile(self, file):
        self.wsdl = WSDLReader().loadFromFile(file)

    def loadFromURL(self, url):
        self.wsdl = WSDLReader().loadFromURL(url)

    def checkWSDLCollection(self, tag_name, component, key='name'):
        definition = self.wsdl.document.documentElement
        version = DOM.WSDLUriToVersion(definition.namespaceURI)
        nspname = DOM.GetWSDLUri(version)
        for node in DOM.getElements(definition, tag_name, nspname):
            name = DOM.getAttr(node, key)
            comp = component[name]
            self.failUnlessEqual(eval('comp.%s' %key), name)

    def checkXSDCollection(self, tag_name, component, node, key='name'):
        for cnode in DOM.getElements(node, tag_name):
            name = DOM.getAttr(cnode, key)
            component[name] 

    def wsdlServices(self):
        self.checkWSDLCollection('service', self.wsdl.services)

    def wsdlMessages(self): 
        self.checkWSDLCollection('message', self.wsdl.messages)

    def wsdlPortTypes(self):
        self.checkWSDLCollection('portType', self.wsdl.portTypes)

    def wsdlBindings(self):
        self.checkWSDLCollection('binding', self.wsdl.bindings)

    def wsdlImports(self):
        self.checkWSDLCollection('import', self.wsdl.imports, key='namespace')

    def wsdlTypes(self):
        for key in self.wsdl.types.keys(): 
            schema = self.wsdl.types[key]
            self.failUnlessEqual(key, schema.getTargetNamespace())

        definition = self.wsdl.document.documentElement
        version = DOM.WSDLUriToVersion(definition.namespaceURI)
        nspname = DOM.GetWSDLUri(version)
        for node in DOM.getElements(definition, 'types', nspname):
            for snode in DOM.getElements(node, 'schema'):
                tns = DOM.findTargetNS(snode)
                schema = self.wsdl.types[tns]
                self.schemaAttributesDeclarations(schema, snode)
                self.schemaAttributeGroupDeclarations(schema, snode)
                self.schemaElementDeclarations(schema, snode)
                self.schemaTypeDefinitions(schema, snode)

    def wsdlExtensions(self):
        if self.wsdl.extensions:
            print 'No check for WSDLTools(%s) Extensions:' %(self.wsdl.name)
            for ext in self.wsdl.extensions: print '\t', ext

    def schemaAttributesDeclarations(self, schema, node):
        self.checkXSDCollection('attribute', schema.attr_decl, node)

    def schemaAttributeGroupDeclarations(self, schema, node):
        self.checkXSDCollection('group', schema.attr_groups, node)

    def schemaElementDeclarations(self, schema, node):
        self.checkXSDCollection('element', schema.elements, node)

    def schemaTypeDefinitions(self, schema, node):
        self.checkXSDCollection('complexType', schema.types, node)
        self.checkXSDCollection('simpleType', schema.types, node)


def makeNetworkSuite():
    return getSuite(section='services_by_http')

def makeStandAloneSuite():
    return getSuite('services_by_file')

def getSuite(section):
    names = CONFIG.options(section)
    tests = []
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    WSDLToolsTestCase.section = section
    for case in [WSDLToolsTestCase,]:
        case.section = section
        test = loader.loadTestsFromTestCase(case)
        tests.append(test)
    #tests.sort()
    suite.addTests(tests)
    return suite

#makeTestSuite = makeStandAloneSuite
#def main():
#    unittest.main(defaultTest="makeTestSuite")


if __name__ == "__main__" : main()
