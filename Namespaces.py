#! /usr/bin/env python
"""Namespace module, so you don't need PyXML 
"""

try:
    from xml.ns import SOAP, SCHEMA, WSDL, XMLNS
except:
    class SOAP:
        ENV         = "http://schemas.xmlsoap.org/soap/envelope/"
        ENC         = "http://schemas.xmlsoap.org/soap/encoding/"
        ACTOR_NEXT  = "http://schemas.xmlsoap.org/soap/actor/next"

    class SCHEMA:
        XSD1        = "http://www.w3.org/1999/XMLSchema"
        XSD2        = "http://www.w3.org/2000/10/XMLSchema"
        XSD3        = "http://www.w3.org/2001/XMLSchema"
        XSI1        = "http://www.w3.org/1999/XMLSchema-instance"
        XSI2        = "http://www.w3.org/2000/10/XMLSchema-instance"
        XSI3        = "http://www.w3.org/2001/XMLSchema-instance"
        BASE        = XSD3

    class WSDL:
        BASE     = 'http://schemas.xmlsoap.org/wsdl/'
        BIND_HTTP = 'http://schemas.xmlsoap.org/wsdl/http/'
        BIND_MIME = 'http://schemas.xmlsoap.org/wsdl/mime/'
        BIND_SOAP = 'http://schemas.xmlsoap.org/wsdl/soap/'

    class XMLNS:
        BASE        = "http://www.w3.org/2000/xmlns/"
        XML         = "http://www.w3.org/XML/1998/namespace"
        HTML        = "http://www.w3.org/TR/REC-html40"
