############################################################################
# Joshua R. Boverhof, LBNL
# See Copyright for copyright notice!
###########################################################################

###########################################################################
# Config file for the unit test framework. 
# Sections below.
###########################################################################

##########################################################################
# SECTION [files] - archives of wsdl/xsd files.
# 
##########################################################################
[files]
archives = ('xmethods.tar.gz', 'schema.tar.gz')

##########################################################################
# SECTION [services_by_file] - all services locally available for
#     testing.
##########################################################################
[services_by_file]
ogsi = schema/ogsi/ogsi_service.wsdl
airport = xmethods/airport.wsdl
amazon = xmethods/AmazonWebServices.wsdl
books = xmethods/books.wsdl
distance = xmethods/Distance.wsdl
freedb = xmethods/freedb.wsdl
globalweather = xmethods/globalweather.wsdl
IHaddock = xmethods/IHaddock.wsdl
ip2geo = xmethods/ip2geo.wsdl
magic = xmethods/magic.wsdl
query = xmethods/query.wsdl
RateInfo = xmethods/RateInfo.wsdl
SHA1Encrypt = xmethods/SHA1Encrypt.wsdl
siteInsepct = xmethods/siteInspect.wsdl
TemperatureService = xmethods/TemperatureService.wsdl
usweather = xmethods/usweather.wsdl
zip2geo = xmethods/zip2geo.wsdl


##########################################################################
# SECTION [services_by_http] - all services available for
#     network testing.
##########################################################################
[services_by_http]
amazon = http://soap.amazon.com/schemas/AmazonWebServices.wsdl
homelandsecurity = http://www.boyzoid.com/threat.cfc?wsdl
rtf2html = http://www.infoaccelerator.net/cfc/rft2html.cfc?WSDL


