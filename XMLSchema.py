# Copyright (c) 2001 Zope Corporation and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.

import string, types, base64, re
from Utility import DOM, Collection
from StringIO import StringIO


class SchemaReader:
    """A SchemaReader creates XMLSchema objects from urls and xml data."""

    def loadFromStream(self, file):
        """Return an XMLSchema instance loaded from a file object."""
        document = DOM.loadDocument(file)
        schema = XMLSchema()
        schema.load(document)
        return schema

    def loadFromString(self, data):
        """Return an XMLSchema instance loaded from an xml string."""
        return self.loadFromStream(StringIO(data))

    def loadFromURL(self, url):
        """Return an XMLSchema instance loaded from the given url."""
        document = DOM.loadFromURL(url)
        schema = XMLSchema()
        schema.location = url
        schema.load(document)
        return schema

    def loadFromFile(self, filename):
        """Return an XMLSchema instance loaded from the given file."""
        file = open(filename, 'rb')
        try:     schema = self.loadFromStream(file)
        finally: file.close()
        return schema


class XMLSchema:
    # This is temporary, for the benefit of WSDL until the real thing works.
    def __init__(self, element):
        self.targetNamespace = DOM.getAttr(element, 'targetNamespace')
        self.element = element

class realXMLSchema:
    """A schema is a collection of schema components derived from one
       or more schema documents, that is, one or more <schema> element
       information items. It represents the abstract notion of a schema
       rather than a single schema document (or other representation)."""
    def __init__(self):
        self.simpleTypes = Collection(self)
        self.complexTypes = Collection(self)
        self.attributes = Collection(self)
        self.elements = Collection(self)
        self.attrGroups = Collection(self)
        self.idConstraints=None
        self.modelGroups = None
        self.notations = None
        self.extensions = []

    targetNamespace = None
    attributeFormDefault = 'unqualified'
    elementFormDefault = 'unqualified'
    blockDefault = None
    finalDefault = None
    location = None
    version = None
    id = None

    def load(self, document):
        if document.nodeType == document.DOCUMENT_NODE:
            schema = DOM.getElement(document, 'schema', None, None)
        else:
            schema = document
        if schema is None:
            raise SchemaError('Missing <schema> element.')

        self.namespace = namespace = schema.namespaceURI
        if not namespace in DOM.NS_XSD_ALL:
            raise SchemaError(
                'Unknown XML schema namespace: %s.' % self.namespace
                )

        for attrname in (
            'targetNamespace', 'attributeFormDefault', 'elementFormDefault',
            'blockDefault', 'finalDefault', 'version', 'id'
            ):
            value = DOM.getAttr(schema, attrname, None, None)
            if attr is not None:
                setattr(self, attrname, value)


        # Resolve imports and includes here?
##         imported = {}
##         while 1:
##             imports = []
##             for element in DOM.getElements(definitions, 'import', NS_WSDL):
##                 location = DOM.getAttr(element, 'location')
##                 if not imported.has_key(location):
##                     imports.append(element)
##             if not imports:
##                 break
##             for element in imports:
##                 self._import(document, element)
##                 imported[location] = 1

        for element in DOM.getElements(schema, None, None):
            localName = element.localName

            if not DOM.nsUriMatch(element.namespaceURI, namespace):
                self.extensions.append(element)
                continue

            elif localName == 'message':
                name = DOM.getAttr(element, 'name')
                docs = GetDocumentation(element)
                message = self.addMessage(name, docs)
                parts = DOM.getElements(element, 'part', NS_WSDL)
                message.load(parts)
                continue

    def _import(self, document, element):
        namespace = DOM.getAttr(element, 'namespace', default=None)
        location = DOM.getAttr(element, 'location', default=None)
        if namespace is None or location is None:
            raise WSDLError(
                'Invalid import element (missing namespace or location).'
                )

        # Sort-of support relative locations to simplify unit testing. The
        # WSDL specification actually doesn't allow relative URLs, so its
        # ok that this only works with urls relative to the initial document.
        location = urllib.basejoin(self.location, location)

        obimport = self.addImport(namespace, location)
        obimport._loaded = 1

        importdoc = DOM.loadFromURL(location)
        try:
            if location.find('#') > -1:
                idref = location.split('#')[-1]
                imported = DOM.getElementById(importdoc, idref)
            else:
                imported = importdoc.documentElement
            if imported is None:
                raise WSDLError(
                    'Import target element not found for: %s' % location
                    )

            imported_tns = DOM.getAttr(imported, 'targetNamespace')
            importer_tns = namespace

            if imported_tns != importer_tns:
                return

            if imported.localName == 'definitions':
                imported_nodes = imported.childNodes
            else:
                imported_nodes = [imported]
            parent = element.parentNode
            for node in imported_nodes:
                if node.nodeType != node.ELEMENT_NODE:
                    continue
                child = DOM.importNode(document, node, 1)
                parent.appendChild(child)
                child.setAttribute('targetNamespace', importer_tns)
                attrsNS = imported._attrsNS
                for attrkey in attrsNS.keys():
                    if attrkey[0] == DOM.NS_XMLNS:
                        attr = attrsNS[attrkey].cloneNode(1)
                        child.setAttributeNode(attr)
        finally:
            importdoc.unlink()


class Element:
    """Common base class for element representation classes."""
    def __init__(self, name=None, documentation=''):
        self.name = name
        self.documentation = documentation
        self.extensions = []

    def addExtension(self, item):
        self.extensions.append(item)


class SimpleTypeDefinition:
    """Represents an xml schema simple type definition."""

class ComplexTypeDefinition:
    """Represents an xml schema complex type definition."""

class AttributeDeclaration:
    """Represents an xml schema attribute declaration."""

class ElementDeclaration:
    """Represents an xml schema element declaration."""
    def __init__(self, name, type=None, targetNamespace=None):
        self.name = name

    targetNamespace = None
    annotation = None
    nillable = 0
    abstract = 0
    default = None
    fixed = None
    scope = 'global'
    type = None
    form = 0
    # Things we will not worry about for now.
    id_constraint_defs = None
    sub_group_exclude = None
    sub_group_affils = None
    disallowed_subs = None










class AttributeGroupDefinition:
    """Represents an xml schema attribute group definition."""

class IdentityConstraintDefinition:
    """Represents an xml schema identity constraint definition."""

class ModelGroupDefinition:
    """Represents an xml schema model group definition."""

class NotationDeclaration:
    """Represents an xml schema notation declaration."""

class Annotation:
    """Represents an xml schema annotation."""

class ModelGroup:
    """Represents an xml schema model group."""

class Particle:
    """Represents an xml schema particle."""

class WildCard:
    """Represents an xml schema wildcard."""

class AttributeUse:
    """Represents an xml schema attribute use."""


class ElementComponent:
    namespace = ''
    name = ''
    type = None
    form = 'qualified | unqualified'
    scope = 'global or complex def'
    constraint = ('value', 'default | fixed')
    nillable = 0
    id_constraint_defs = None
    sub_group_affil = None
    sub_group_exclusions = None
    disallowed_subs = 'substitution, extension, restriction'
    abstract = 0
    minOccurs = 1
    maxOccurs = 1
    ref = ''

class AttributeThing:
    name = ''
    namespace = ''
    typeName = ''
    typeUri = ''
    scope = 'global | local to complex def'
    constraint = ('value:default', 'value:fixed')
    use = 'optional | prohibited | required'

class ElementDataType:
    namespace = ''
    name = ''
    element_form = 'qualified | unqualified'
    attr_form = None
    type_name = ''
    type_uri = ''
    def __init__(self, name, namespace, type_name, type_uri):
        self.namespace = namespace
        self.name = name
        # type may be anonymous...
        self.type_name = type_name
        self.type_uri = type_uri

    def checkValue(self, value, context):
        # Delegate value checking to the type of the element.
        typeref = (self.type_uri, self.type_name)
        handler = context.serializer.getType(typeref)
        return handler.checkValue(value, context)

    def serialize(self, name, namespace, value, context, **kwargs):
        if context.check_values:
            self.checkValue(value, context)
        # Delegate serialization to the type of the element.
        typeref = (self.type_uri, self.type_name)
        handler = context.serializer.getType(typeref)
        return handler.serialize(self.name, self.namespace, value, context)

    def deserialize(self, element, context):
        if element_is_null(element, context):
            return None
        # Delegate deserialization to the type of the element.
        typeref = (self.type_uri, self.type_name)
        handler = context.serializer.getType(typeref)
        return handler.deserialize(element, context)



def parse_schema(data):
    targetNS = ''
    attributeFormDefault = 0
    elementFormDefault = 0
    blockDefault = ''
    finalDefault = ''
    language = None
    version = None
    id = ''
