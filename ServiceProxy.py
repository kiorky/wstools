# Copyright (c) 2001 Zope Corporation and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.

from urlparse import urlparse
from ZSI import *
from ZSI.client import *
import weakref

from Utility import DOM
import WSDLTools


class SOAPCallInfo:
    """SOAPCallInfo captures the important binding information about a 
       SOAP operation, in a structure that is easier to work with than
       raw WSDL structures."""

    def __init__(self, methodName):
        self.methodName = methodName
        self.inheaders = []
        self.outheaders = []
        self.inparams = []
        self.outparams = []
        self.retval = None

    encodingStyle = DOM.NS_SOAP_ENC
    documentation = ''
    soapAction = None
    transport = None
    namespace = None
    location = None
    use = 'encoded'
    style = 'rpc'

    def addInParameter(self, name, type, namespace=None, element_type=0):
        """Add an input parameter description to the call info."""
        parameter = ParameterInfo(name, type, namespace, element_type)
        self.inparams.append(parameter)
        return parameter

    def addOutParameter(self, name, type, namespace=None, element_type=0):
        """Add an output parameter description to the call info."""
        parameter = ParameterInfo(name, type, namespace, element_type)
        self.outparams.append(parameter)
        return parameter

    def setReturnParameter(self, name, type, namespace=None, element_type=0):
        """Set the return parameter description for the call info."""
        parameter = ParameterInfo(name, type, namespace, element_type)
        self.retval = parameter
        return parameter

    def addInHeaderInfo(self, name, type, namespace, element_type=0,
                        mustUnderstand=0):
        """Add an input SOAP header description to the call info."""
        headerinfo = HeaderInfo(name, type, namespace, element_type)
        if mustUnderstand:
            headerinfo.mustUnderstand = 1
        self.inheaders.append(headerinfo)
        return headerinfo

    def addOutHeaderInfo(self, name, type, namespace, element_type=0,
                         mustUnderstand=0):
        """Add an output SOAP header description to the call info."""
        headerinfo = HeaderInfo(name, type, namespace, element_type)
        if mustUnderstand:
            headerinfo.mustUnderstand = 1
        self.outheaders.append(headerinfo)
        return headerinfo

    def getInParameters(self):
        """Return a sequence of the in parameters of the method."""
        return self.inparams

    def getOutParameters(self):
        """Return a sequence of the out parameters of the method."""
        return self.outparams

    def getReturnParameter(self):
        """Return param info about the return value of the method."""
        return self.retval

    def getInHeaders(self):
        """Return a sequence of the in headers of the method."""
        return self.inheaders

    def getOutHeaders(self):
        """Return a sequence of the out headers of the method."""
        return self.outheaders


class ParameterInfo:
    """A ParameterInfo object captures parameter binding information."""
    def __init__(self, name, type, namespace=None, element_type=0):
        if element_type:
            self.element_type = 1
        if namespace is not None:
            self.namespace = namespace
        self.name = name
        self.type = type

    element_type = 0
    namespace = None
    default = None


class HeaderInfo(ParameterInfo):
    """A HeaderInfo object captures SOAP header binding information."""
    def __init__(self, name, type, namespace, element_type=None):
        ParameterInfo.__init__(self, name, type, namespace, element_type)

    mustUnderstand = 0
    actor = None


def callInfoFromWSDL(port, name):
    """Return a SOAPCallInfo given a WSDL port and operation name."""
    wsdl = port.getService().getWSDL()
    binding = port.getBinding()
    portType = binding.getPortType()
    operation = portType.operations[name]
    opbinding = binding.operations[name]
    messages = wsdl.messages
    callinfo = SOAPCallInfo(name)

    addrbinding = port.getAddressBinding()
    if not isinstance(addrbinding, WSDLTools.SoapAddressBinding):
        raise ValueError, 'Unsupported binding type.'        
    callinfo.location = addrbinding.location

    soapbinding = binding.findBinding(WSDLTools.SoapBinding)
    if soapbinding is None:
        raise ValueError, 'Missing soap:binding element.'
    callinfo.transport = soapbinding.transport
    callinfo.style = soapbinding.style or 'document'

    soap_op_binding = opbinding.findBinding(WSDLTools.SoapOperationBinding)
    if soap_op_binding is not None:
        callinfo.soapAction = soap_op_binding.soapAction
        callinfo.style = soap_op_binding.style or callinfo.style

    parameterOrder = operation.parameterOrder

    if operation.input is not None:
        message = messages[operation.input.message]
        msgrole = opbinding.input

        mime = msgrole.findBinding(WSDLTools.MimeMultipartRelatedBinding)
        if mime is not None:
            raise ValueError, 'Mime bindings are not supported.'
        else:
            for item in msgrole.findBindings(WSDLTools.SoapHeaderBinding):
                part = messages[item.message].parts[item.part]
                header = callinfo.addInHeaderInfo(
                    part.name,
                    part.element or part.type,
                    item.namespace,
                    element_type = part.element and 1 or 0
                    )
                header.encodingStyle = item.encodingStyle

            body = msgrole.findBinding(WSDLTools.SoapBodyBinding)
            if body is None:
                raise ValueError, 'Missing soap:body binding.'
            callinfo.encodingStyle = body.encodingStyle
            callinfo.namespace = body.namespace
            callinfo.use = body.use

            if body.parts is not None:
                parts = []
                for name in body.parts:
                    parts.append(message.parts[name])
            else:
                parts = message.parts.values()

            for part in parts:
                callinfo.addInParameter(
                    part.name,
                    part.element or part.type,
                    element_type = part.element and 1 or 0
                    )

    if operation.output is not None:
        message = messages[operation.output.message]
        msgrole = opbinding.output

        mime = msgrole.findBinding(WSDLTools.MimeMultipartRelatedBinding)
        if mime is not None:
            raise ValueError, 'Mime bindings are not supported.'
        else:
            for item in msgrole.findBindings(WSDLTools.SoapHeaderBinding):
                part = messages[item.message].parts[item.part]
                header = callinfo.addOutHeaderInfo(
                    part.name,
                    part.element or part.type,
                    item.namespace,
                    element_type = part.element and 1 or 0
                    )
                header.encodingStyle = item.encodingStyle

            body = msgrole.findBinding(WSDLTools.SoapBodyBinding)
            if body is None:
                raise ValueError, 'Missing soap:body binding.'
            callinfo.encodingStyle = body.encodingStyle
            callinfo.namespace = body.namespace
            callinfo.use = body.use

            if body.parts is not None:
                parts = []
                for name in body.parts:
                    parts.append(message.parts[name])
            else:
                parts = message.parts.values()

            if parts:
                callinfo.setReturnParameter(
                    parts[0].name,
                    parts[0].element or parts[0].type,
                    element_type = parts[0].element and 1 or 0
                    )
                for part in parts[1:]:
                    callinfo.addOutParameter(
                        part.name,
                        part.element or part.type,
                        element_type = part.element and 1 or 0
                        )

    return callinfo


class ServiceProxy:
    """A ServiceProxy provides a convenient way to call a remote web
       service that is described with WSDL. The proxy exposes methods
       that reflect the methods of the remote web service."""

    def __init__(self, wsdl, service=None, port=None, tracefile=None,
                 typesmodule=None, nsdict=None):
        if not hasattr(wsdl, 'targetNamespace'):
            wsdl = WSDLTools.WSDLReader().loadFromURL(wsdl)
#        for item in wsdl.types.items():
#            self._serializer.loadSchema(item)
        self._service = wsdl.services[service or 0]
        self.__doc__ = self._service.documentation
        self._port = self._service.ports[port or 0]
        self._name = self._service.name
        self._wsdl = wsdl
        self._tracefile = tracefile
        self._typesmodule = typesmodule
        self._nsdict = nsdict
        binding = self._port.getBinding()
        portType = binding.getPortType()
        for item in portType.operations:
            callinfo = callInfoFromWSDL(self._port, item.name)
            method = MethodProxy(self, callinfo)
            setattr(self, item.name, method)

    def _call(self, name, *args, **kwargs):
        """Call the named remote web service method."""
        if len(args) and len(kwargs):
            raise TypeError(
                'Use positional or keyword argument only.'
                )

        callinfo = getattr(self, name).callinfo
        url = callinfo.location
        (protocol, host, uri, query, fragment, identifier) = urlparse(url)
        port = 80
        if host.find(':') >= 0:
            host, port = host.split(':')

        params = callinfo.getInParameters()
        host = str(host)
        port = str(port)

        binding = Binding(host=host, tracefile=self._tracefile,
                          ssl=(protocol == 'https'),
                          port=port, url=uri, typesmodule=self._typesmodule,
                          nsdict=self._nsdict)

        apply(getattr(binding, callinfo.methodName), args)


	#print binding.ReceiveRaw()

        return binding.Receive()


class MethodProxy:
    """ """
    def __init__(self, parent, callinfo):
        self.__name__ = callinfo.methodName
        self.__doc__ = callinfo.documentation
        self.callinfo = callinfo
        self.parent = weakref.ref(parent)

    def __call__(self, *args, **kwargs):
        return self.parent()._call(self.__name__, *args, **kwargs)
