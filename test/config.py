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
SolveSystem = xmethods/SolveSystem.wsdl.xml


##########################################################################
# SECTION [services_by_http] - all services available for
#     network testing.
##########################################################################
[services_by_http]
homelandsecurity = http://www.boyzoid.com/threat.cfc?wsdl
SolveSystem = http://www.lixusnet.com/SolveSystem.wsdl
# new URL's from xmethods
194.98.194.111.4dwsdl = http://194.98.194.111/4dwsdl
IWagAddressServerSingle = http://62.212.78.36/cgi-bin/WagAddressServerSingle.exe/wsdl/IWagAddressServerSingle
GoogleSearch = http://api.google.com/GoogleSearch.wsdl
appserver.pepperzak.net.wsdl = http://appserver.pepperzak.net/bankcode/BankCodeEJBHome/wsdl.jsp
AddressFinder = http://arcweb.esri.com/services/v2/AddressFinder.wsdl
MapImage = http://arcweb.esri.com/services/v2/MapImage.wsdl
PlaceFinderSample = http://arcweb.esri.com/services/v2/PlaceFinderSample.wsdl
Proximity = http://arcweb.esri.com/services/v2/Proximity.wsdl
arcweb.esri.com.Query = http://arcweb.esri.com/services/v2/Query.wsdl
RouteFinder = http://arcweb.esri.com/services/v2/RouteFinder.wsdl
QuranVerse = http://aspnet.lamaan.com/webservices/QuranVerse.asmx?WSDL
mxchecker = http://beta2.eraserver.net/webservices/mxchecker/mxchecker.asmx?WSDL
ClientService = http://clientservice.muse.net/ClientService.asmx?WSDL
demo.eltegra.com.wsdl = http://demo.eltegra.com/webservices/wsdl?app=CarPayment
demo.eltegra.com.wsdl.1 = http://demo.eltegra.com/webservices/wsdl?app=MortgageCalculator
FedEpayDirectoryService = http://demo.soapam.com/services/FedEpayDirectory/FedEpayDirectoryService.wsdl
ITempConverter = http://developerdays.com/cgi-bin/tempconverter.exe/wsdl/ITempConverter
KRSS_DAML_Service = http://digilander.libero.it/mamo78/KRSS_DAML_Service.wsdl
computerdictionary = http://dotnet.cyberthink.net/computerdictionary/computerdictionary.asmx?wsdl
ewsdemo.webmethods.com.wsd = http://ewsdemo.webmethods.com/WmEWS/directory/wsd.dsp?interface=wmpayflow.sample&service=Credit_Approval
RentDB2 = http://freene.dynip.com/RentDB2/RentDB2.asmx?wsdl
Currencyws = http://glkev.webs.innerhost.com/glkev_ws/Currencyws.asmx?WSDL
HistoricalStockQuotes = http://glkev.webs.innerhost.com/glkev_ws/HistoricalStockQuotes.asmx?WSDL
StockServices = http://glkev.webs.innerhost.com/glkev_ws/StockServices.asmx?WSDL
UPSTracking = http://glkev.webs.innerhost.com/glkev_ws/UPSTracking.asmx?WSDL
WeatherFetcher = http://glkev.webs.innerhost.com/glkev_ws/WeatherFetcher.asmx?WSDL
businessnews = http://glkev.webs.innerhost.com/glkev_ws/businessnews.asmx?WSDL
RecipeService = http://icuisine.net/webservices/RecipeService.asmx?WSDL
pos_public = http://iis1.grantparksoftware.com:8080/gps/pos_public.asmx?WSDL
promotionService = http://interpressfact.net/webservices/promotionService.asmx?wsdl
java.rus.uni-stuttgart.de.quiz = http://java.rus.uni-stuttgart.de/quiz/quiz.wsdl
amazon_query = http://majordojo.com/amazon_query/amazon_query.wsdl
MysicSearchEngine = http://mysic.com/Webservices/MysicSearchEngine.asmx?WSDL
BusinessPartner = http://mywebservices.free.fr/server/BusinessPartner.wsdl
Temperature = http://mywebservices.free.fr/server/Temperature.wsdl
getCAWeather = http://ocean.cse.ucsc.edu/soap/getCAWeather.wsdl
FaxService = http://oneoutbox.com/wsdl/FaxService.wsdl
9iasmobile = http://otn.oracle.com/ws/9iasmobile?WSDL
otnnews = http://otn.oracle.com/ws/otnnews?WSDL
EqImage = http://otourdes.europe.webmatrixhosting.net/EqImageSharp/EqImage.asmx?WSDL
paracite = http://paracite.ecs.soton.ac.uk/paracite.wsdl
IgetNumbers = http://reto.checkit.ch/Scripts/Lotto.dll/wsdl/IgetNumbers
Action!getWSDL = http://samples.bowstreet.com/bowstreet5/webengine/xmethods/gcd/Action!getWSDL
reports = http://sandbox.grandcentral.com/services/reports?WSDL
CupScores = http://scores.serviceobjects.com/CupScores.asmx?WSDL
currency = http://server1.pointwsp.net/ws/finance/currency.asmx?WSDL
server1.pointwsp.net.main = http://server1.pointwsp.net/ws/postal/main.asmx?WSDL
GraphMagic = http://service.graphmagic.com/GMService/GraphMagic.asmx?wsdl
GetLocalTime = http://services.develop.co.za/GetLocalTime.asmx?WSDL
xmethods-DomainChecker = http://services.xmethods.net/soap/urn:xmethods-DomainChecker.wsdl
xmethods-delayed-quotes = http://services.xmethods.net/soap/urn:xmethods-delayed-quotes.wsdl
ws4gotze = http://slashdemocracy.org/links/ws4gotze.wsdl
subscribe = http://soap.4s4c.com/weblogs/subscribe.wsdl
IACHSOAP = http://soap.achchex.com/exec/achsoap.dll/wsdl/IACHSOAP
ISpamCheck = http://soap.prowizorka.com/spam/wsdl/ISpamCheck
soap.systinet.net.wsdl = http://soap.systinet.net/demos/FTPService/wsdl
soap.systinet.net.wsdl.1 = http://soap.systinet.net/demos/FreeDB/wsdl
soap.systinet.net.wsdl.2 = http://soap.systinet.net/demos/Newsfeed/wsdl
soap.systinet.net.wsdl.3 = http://soap.systinet.net/demos/RpmFinder/wsdl
soap.systinet.net.wsdl.4 = http://soap.systinet.net/demos/W3CSearch/wsdl
soap.systinet.net.wsdl.5 = http://soap.systinet.net/demos/ZVONSearch/wsdl
certService = http://soapclient.com/xml/certService.wsdl
SurveyService = http://survey.rila.net/SurveyService/SurveyService.asmx?wsdl
DocConverterServicePort = http://telecommerce.danet.de/axis/services/DocConverterServicePort?wsdl
TerraService = http://terraservice.net/TerraService.asmx?WSDL
Encryption = http://test.mapfrepr.net/Encryption/Encryption.asmx?WSDL
transform = http://transform.dataconcert.com/transform.wsdl
autoloan = http://upload.eraserver.net/circle24/autoloan.asmx?wsdl
urljr.com.soap = http://urljr.com/soap
CarRentalQuotes = http://wavendon.dsdata.co.uk/axis/services/CarRentalQuotes?wsdl
SpamKiller = http://wavendon.dsdata.co.uk/axis/services/SpamKiller?wsdl
SBGGetAirFareQuote = http://wavendon.dsdata.co.uk:8080/axis/services/SBGGetAirFareQuote?wsdl
WeatherServices = http://weather.unisysfsp.com/PDCWebService/WeatherServices.asmx?WSDL
webservices.empowered.com.stats = http://webservices.empowered.com/statsws/stats.asmx?WSDL
zipcoderesolver = http://webservices.eraserver.net/zipcoderesolver/zipcoderesolver.asmx?WSDL
Distance = http://webservices.imacination.com/distance/Distance.jws?wsdl
zipcodes = http://webservices.instantlogic.com/zipcodes.ils?wsdl
chartWS = http://webservices.isitedesign.com/ws/chartWS.cfc?wsdl
slashdotnews = http://webservices.isitedesign.com/ws/slashdotnews.cfc?wsdl
IEmailService = http://webservices.matlus.com/scripts/emailwebservice.dll/wsdl/IEmailService
IMsSessionBrokerService = http://webservices.matlus.com/scripts/sessionservice.dll/wsdl/IMsSessionBrokerService
webservices.matlus.com.IWhoIs = http://webservices.matlus.com/scripts/whoiswebservice.dll/wsdl/IWhoIs
MP3Charts = http://webservices.mp3.com/MP3Charts.wsdl
webservices.sld.cu.aldia = http://webservices.sld.cu/aldia.wsdl
getQuakeData = http://webservices.tei.or.th/getQuakeData.cfc?wsdl
ws.acrosscommunications.com.Fax = http://ws.acrosscommunications.com/Fax.asmx?WSDL
ws.acrosscommunications.com.ICQ = http://ws.acrosscommunications.com/ICQ.asmx?WSDL
NumPager = http://ws.acrosscommunications.com/NumPager.asmx?WSDL
ws.acrosscommunications.com.Phone = http://ws.acrosscommunications.com/Phone.asmx?WSDL
ws.acrosscommunications.com.SMS = http://ws.acrosscommunications.com/SMS.asmx?WSDL
ws.acrosscommunications.com.TAP = http://ws.acrosscommunications.com/TAP.asmx?WSDL
ws.cdyne.com.ftg = http://ws.cdyne.com/FontToGraphic/ftg.asmx?wsdl
ws.cdyne.com.check = http://ws.cdyne.com/SpellChecker/check.asmx?wsdl
ws.cdyne.com.ev = http://ws.cdyne.com/emailverify/ev.asmx?wsdl
ws.cdyne.com.ip2geo = http://ws.cdyne.com/ip2geo/ip2geo.asmx?wsdl
addresslookup = http://ws.cdyne.com/psaddress/addresslookup.asmx?wsdl
queryip = http://ws.cdyne.com/whoisforip/queryip.asmx?wsdl
ws.cdyne.com.whois = http://ws.cdyne.com/whoisquery/whois.asmx?wsdl
zip2geo = http://ws.cdyne.com/ziptogeo/zip2geo.asmx?wsdl
ws.interfax.net.dfs = http://ws.interfax.net/dfs.asmx?WSDL
render3d = http://ws.xara.com/graphicrender/render3d.wsdl
ws.xara.com.navbar = http://ws.xara.com/navbar/navbar.wsdl
AddressValidate = http://ws2.serviceobjects.net/av/AddressValidate.asmx?WSDL
domainspy = http://ws2.serviceobjects.net/ds/domainspy.asmx?WSDL
EmailValidate = http://ws2.serviceobjects.net/ev/EmailValidate.asmx?WSDL
FastTax = http://ws2.serviceobjects.net/ft/FastTax.asmx?WSDL
FastWeather = http://ws2.serviceobjects.net/fw/FastWeather.asmx?WSDL
GeoCash = http://ws2.serviceobjects.net/gc/GeoCash.asmx?WSDL
GeoPhone = http://ws2.serviceobjects.net/gp/GeoPhone.asmx?WSDL
GeoPinPoint = http://ws2.serviceobjects.net/gpp/GeoPinPoint.asmx?WSDL
lotterynumbers = http://ws2.serviceobjects.net/ln/lotterynumbers.asmx?WSDL
phoneappend = http://ws2.serviceobjects.net/pa/phoneappend.asmx?wsdl
packcost = http://ws2.serviceobjects.net/pc/packcost.asmx?WSDL
PackTrack = http://ws2.serviceobjects.net/pt/PackTrack.asmx?WSDL
FastQuote = http://ws2.serviceobjects.net/sq/FastQuote.asmx?WSDL
ws2.serviceobjects.net.UPC = http://ws2.serviceobjects.net/upc/UPC.asmx?WSDL
USPatentOffice = http://ws2.serviceobjects.net/uspo/USPatentOffice.asmx?WSDL
ws2.serviceobjects.net.WhoIs = http://ws2.serviceobjects.net/whi/WhoIs.asmx?WSDL
YellowPages = http://ws2.serviceobjects.net/yp/YellowPages.asmx?WSDL
holidays = http://wsdl.wsdlfeeds.com/holidays.cfc?wsdl
wsdl.wsdlfeeds.com.odp = http://wsdl.wsdlfeeds.com/odp.cfc?wsdl
wsdl.wsdlfeeds.com.spell = http://wsdl.wsdlfeeds.com/spell.cfc?wsdl
IBorlandBabel = http://ww6.borland.com/webservices/BorlandBabel/BorlandBabel.exe/wsdl/IBorlandBabel
IMapQuest = http://ww6.borland.com/webservices/MapQuest/MapQuest.exe/wsdl/IMapQuest
FreeFaxService = http://www.OneOutBox.com/wsdl/FreeFaxService.wsdl
SQLDataSoap = http://www.SoapClient.com/xml/SQLDataSoap.wsdl
www.abctext.com.SMS = http://www.abctext.com/webservices/SMS.asmx?WSDL
mssoapmp3search = http://www.agnisoft.com/soap/mssoapmp3search.xml
compositions = http://www.alanbushtrust.org.uk/soap/compositions.wsdl
YahooUserPingService = http://www.allesta.net:51110/webservices/wsdl/YahooUserPingService.xml
www.apniurdu.com.Urdu2 = http://www.apniurdu.com/SOAP/Urdu2.wsdl
sekeyword = http://www.aspiringgeek.com/cfc/keyword/sekeyword.cfc?wsdl
piglatin = http://www.aspxpressway.com/maincontent/webservices/piglatin.asmx?wsdl
GetCurrencyExchange = http://www.atlaz.net/webservices/GetCurrencyExchange.wsdl
personlookup = http://www.barnaland.is/dev/personlookup.asmx?WSDL
phonebook = http://www.barnaland.is/dev/phonebook.asmx?WSDL
www.barnaland.is.puki = http://www.barnaland.is/dev/puki.asmx?WSDL
www.barnaland.is.sms = http://www.barnaland.is/dev/sms.asmx?WSDL
xmltracking = http://www.baxglobal.com/xmltracking/xmltracking.asmx?wsdl
ITeeChart = http://www.berneda.com/scripts/TeeChartSOAP.exe/wsdl/ITeeChart
imalert = http://www.bindingpoint.com/ws/imalert/imalert.asmx?wsdl
IBANFuncs = http://www.bitounis.com/IBAN/IBANFuncs.asmx?WSDL
RSAFuncs = http://www.bitounis.com/RSAFunctions/RSAFuncs.asmx?WSDL
LogFileParser = http://www.bitounis.com/W3CParser/LogFileParser.asmx?WSDL
www.bitounis.com.events = http://www.bitounis.com/WebEvents/events.asmx?WSDL
ATTPager = http://www.bitwaste.com/xmethods/ATTPager/ATTPager.wsdl
dispenser = http://www.blackstoneonline.com/webservices/dispenser.xml
www.c6.hu.huzip = http://www.c6.hu/ws/huzip.wsdl
www.cgi101.com.mach = http://www.cgi101.com/~msmithso/wsdl/mach.wsdl
www.chatlog.net.wsdl = http://www.chatlog.net/wsdl.xml
placelookup = http://www.codebump.com/services/placelookup.asmx?wsdl
zipcodelookup = http://www.codebump.com/services/zipcodelookup.asmx?wsdl
xreonline = http://www.codecube.net/services/xreonline.asmx?WSDL
www.codemechanisms.co.uk.UNSPSC = http://www.codemechanisms.co.uk/WebServices/UNSPSC.asmx?WSDL
discordian = http://www.compkarori.com/wsdl/discordian.wsdl
convert = http://www.cosme.nu/services/convert.php?wsdl
www.cosme.nu.dns = http://www.cosme.nu/services/dns.php?wsdl
www.cosme.nu.pop = http://www.cosme.nu/services/pop.php?wsdl
smtpserver = http://www.cosme.nu/services/smtpserver.php?wsdl
www.cs.fsu.edu.lu = http://www.cs.fsu.edu/~engelen/lu.wsdl
www.cs.fsu.edu.magic = http://www.cs.fsu.edu/~engelen/magic.wsdl
CountryInfoLookup = http://www.cs.uga.edu/~sent/xmethods/CountryInfoLookup.wsdl
IWSMazeServer = http://www.culand.net/WebServices/bin/WSMaze_Server.dll/wsdl/IWSMazeServer
IBorlandChess = http://www.danmarinescu.com/WebServices/ChessCGIServer.exe/wsdl/IBorlandChess
Html2xml = http://www.dev1.eraserver.net/REFLECTIONIT/Html2xml.asmx?WSDL
zipCodeService = http://www.discoverdance.co.uk/zipQuery/zipCodeService.asmx?wsdl
www.dl-me.com.dic2 = http://www.dl-me.com/webservices/dic2.asmx?WSDL
engtoarabic = http://www.dl-me.com/webservices/engtoarabic.asmx?WSDL
unitext = http://www.dl-me.com/webservices/unitext.asmx?wsdl
codepostal = http://www.dotnetisp.com/webservices/dotnetisp/codepostal.asmx?WSDL
src2html = http://www.dotnetisp.com/webservices/dotnetisp/src2html.asmx?WSDL
www.dotnetisp.com.ville = http://www.dotnetisp.com/webservices/dotnetisp/ville.asmx?WSDL
www.drbob42.co.uk.IEuro = http://www.drbob42.co.uk/cgi-bin/Euro42/wsdl/IEuro
soap_cdtek = http://www.drouet-web.com/webservices/soap_cdtek.php?wsdl
www.ebi.ac.uk.XEMBL = http://www.ebi.ac.uk/xembl/XEMBL.wsdl
IHeadline = http://www.ebob42.com/cgi-bin/DrBobsClinic.exe/wsdl/IHeadline
www.ebob42.com.IDutch = http://www.ebob42.com/cgi-bin/NumberToWordsInDutch.exe/wsdl/IDutch
www.ebob42.com.IRoman = http://www.ebob42.com/cgi-bin/Romulan.exe/wsdl/IRoman
emailservices = http://www.einsteinware.com/webservices/email/emailservices.asmx?WSDL
nascardataservice = http://www.einsteinware.com/webservices/nascar/nascardataservice.asmx?WSDL
www.ejse.com.Service = http://www.ejse.com/WeatherService/Service.asmx?WSDL
BusinessList = http://www.esynaps.com/WebServices/BusinessList.asmx?WSDL
DailyDiblert = http://www.esynaps.com/WebServices/DailyDiblert.asmx?WSDL
MsProxy = http://www.esynaps.com/WebServices/MsProxy.asmx?WSDL
NFLNews = http://www.esynaps.com/WebServices/NFLNews.asmx?WSDL
SearchWS = http://www.esynaps.com/WebServices/SearchWS.asmx?WSDL
WhoIsService = http://www.esynaps.com/WebServices/WhoIsService.asmx?WSDL
eSynapsFeed = http://www.esynaps.com/WebServices/eSynapsFeed.asmx?WSDL
eSynapsMonitor = http://www.esynaps.com/WebServices/eSynapsMonitor.wsdl
eSynapsSearch = http://www.esynaps.com/WebServices/eSynapsSearch.asmx?WSDL
YourHostInfo = http://www.esynaps.com/webservices/YourHostInfo.asmx?WSDL
codegenerator = http://www.esynaps.com/webservices/codegenerator.asmx?WSDL
MBWSSoapServices = http://www.extensio.com:8080/ExtensioInfoServer/mbsoap/MBWSSoapServices.wsdl
getWSDL = http://www.eyemaginations.com/cgi-bin/getWSDL.pl?wsdl=WebFunction.wsdl
www.financialwebservices.ltd.uk.bond = http://www.financialwebservices.ltd.uk/axis/services/bond?wsdl
dynamicflash = http://www.firelife.eu.com/dynamicflash/dynamicflash.asmx?WSDL
barCodes = http://www.flash-db.com/services/ws/barCodes.wsdl
companyInfo = http://www.flash-db.com/services/ws/companyInfo.wsdl
flashBarChart = http://www.flash-db.com/services/ws/flashBarChart.wsdl
siteInspect = http://www.flash-db.com/services/ws/siteInspect.wsdl
syndicate = http://www.forta.com/cf/tips/syndicate.cfc?wsdl
TakisActiveLib = http://www.forthlink.gr/TakisLib/TakisActiveLib.WSDL
foxcentral = http://www.foxcentral.net/foxcentral.wsdl
HTMLeMail = http://www.framewerks.com/WebServices/HTMLeMail/HTMLeMail.asmx?WSDL
fwArticles = http://www.framewerks.com/WebServices/fWArticleService/fwArticles.asmx?WSDL
helpfulfunctions = http://www.framewerks.com/WebServices/helpfulfunctions/helpfulfunctions.asmx?WSDL
FreshScoreLiveScores = http://www.freshscore.com/service/FreshScoreLiveScores.asmx?WSDL
stockquotes = http://www.gama-system.com/webservices/stockquotes.asmx?wsdl
webchart = http://www.gxchart.com/webchart.wsdl
WeatherService = http://www.hkwizard.com/WeatherService.asmx?wsdl
IndoEconoCator = http://www.indobiz.com/IndoEconoCator.asmx?WSDL
OptionPricing = http://www.indobiz.com/OptionPricing.asmx?WSDL
rtf2html = http://www.infoaccelerator.net/cfc/rtf2html.cfc?WSDL
kannadakasturiwebservice = http://www.kannadakasturi.com/WebServices/kannadakasturiwebservice.asmx?WSDL
www.maillocate.com.index = http://www.maillocate.com/soap/index.php?wsdl
IPGPKeyServer = http://www.marotz.se/PGPKeyServer/PGPKeyServiceX.exe/wsdl/IPGPKeyServer
ISlashdotHeadlineProvider = http://www.marotz.se/scripts/SlashdotHeadlines.exe/wsdl/ISlashdotHeadlineProvider
ISearchSwedishPerson = http://www.marotz.se/scripts/searchperson.exe/wsdl/ISearchSwedishPerson
ISwedishZipInfo = http://www.marotz.se/scripts/zipinfo.exe/wsdl/ISwedishZipInfo
www.nextbigleap.com.whois = http://www.nextbigleap.com/webservices/whois.cfc?wsdl
finnwords = http://www.nickhodge.com/nhodge/finnwords/finnwords.wsdl
www.nims.nl.oms = http://www.nims.nl/soap/oms.wsdl
www.nims.nl.oms2 = http://www.nims.nl/soap/oms2.wsdl
cfrsearchws = http://www.oakleaf.ws/cfrsearchws/cfrsearchws.asmx?wsdl
cfrsectws = http://www.oakleaf.ws/cfrsectws/cfrsectws.asmx?wsdl
cfrtocws = http://www.oakleaf.ws/cfrtocws/cfrtocws.asmx?wsdl
EvaluationService = http://www.onepercentsoftware.com/axis/services/EvaluationService?wsdl
www.orbitarium.com.ows = http://www.orbitarium.com/schemas/ows.wsdl
Cod_fiscale = http://www.pinellus.com/cfc/Cod_fiscale.cfc?wsdl
RichCardValidator = http://www.richsolutions.com/RichPayments/RichCardValidator.asmx?WSDL
richpay = http://www.richsolutions.com/richpayments/richpay.asmx?WSDL
Iws_Verify_NRIC = http://www.rightsecurity.biz/wsdl/NRICWebServices.dll/wsdl/Iws_Verify_NRIC
www.scdi.org.yim = http://www.scdi.org/~avernet/webservice/yim.wsdl
securexml = http://www.securexml.net/securexml/securexml.wsdl
QuotesService = http://www.seshakiran.com/QuoteService/QuotesService.asmx?wsdl
sidrank = http://www.sid64.com/soap/sidrank.php?wsdl
fissiondotnet = http://www.sidespace.com/ws/fission/fissiondotnet.php?wsdl
ISOcode2shortformatService = http://www.siliconllama.com/services/wsdl/ISOcode2shortformatService.wsdl
ISOcodesService = http://www.siliconllama.com/services/wsdl/ISOcodesService.wsdl
dConverterService = http://www.siliconllama.com/services/wsdl/dConverterService.wsdl
www.stgregorioschurchdc.org.Bible = http://www.stgregorioschurchdc.org/wsdl/Bible.wsdl
Calendar = http://www.stgregorioschurchdc.org/wsdl/Calendar.wsdl
statistics = http://www.strikeiron.com/scripts/statistics.asmx?WSDL
Horoscope = http://www.swanandmokashi.com/HomePage/WebServices/Horoscope.asmx?WSDL
QuoteOfTheDay = http://www.swanandmokashi.com/HomePage/WebServices/QuoteOfTheDay.asmx?WSDL
StockQuotes = http://www.swanandmokashi.com/HomePage/WebServices/StockQuotes.asmx?WSDL
geoserve = http://www.transactionalweb.com/SOAP/geoserve.wsdl
globalocator = http://www.transactionalweb.com/SOAP/globalocator.wsdl
globalskilocator = http://www.transactionalweb.com/SOAP/globalskilocator.wsdl
IGetInflection = http://www.verbix.com/cgi-bin/soapx.exe/wsdl/IGetInflection
www.webserviceoftheday.com.wsotd = http://www.webserviceoftheday.com/ws/soap/wsotd.asmx?wsdl
wwhelpservice = http://www.west-wind.com/wconnect/soap/wwhelpservice.wsdl
www.what-is-around.com.awwia = http://www.what-is-around.com/awwia.wsdl
ZipService = http://www.winisp.net/cheeso/zips/ZipService.asmx?WSDL
www.wlug.org.nz.soap = http://www.wlug.org.nz/phpwiki/soap.wsdl
spellcheckservice = http://www.worldwidedesktop.com/spellcheck/spellcheckservice.asmx?wsdl
wsindexLinks = http://www.wsindex.org/pages/wsindexLinks.wsdl
www.x-ws.de.service = http://www.x-ws.de/cgi-bin/bork/service.wsdl
www.x-ws.de.chat = http://www.x-ws.de/cgi-bin/eliza/chat.wsdl
imstatus = http://www.x-ws.de/cgi-bin/msn/imstatus.wsdl
RateInfo = http://www.xeeinc.com/RateInformation/RateInfo.asmx?WSDL
www.xignite.com.xEdgar = http://www.xignite.com/xEdgar.asmx?WSDL
xSurvey = http://www.xignite.com/xSurvey.asmx?WSDL
www.xignite.com.xnews = http://www.xignite.com/xnews.asmx?WSDL
xoptions = http://www.xignite.com/xoptions.asmx?WSDL
xquotes = http://www.xignite.com/xquotes.asmx?WSDL
xretirement = http://www.xignite.com/xretirement.asmx?WSDL
xsecurity = http://www.xignite.com/xsecurity.asmx?WSDL
xsimulation = http://www.xignite.com/xsimulation.asmx?WSDL
xstatistics = http://www.xignite.com/xstatistics.asmx?WSDL
xworldnews = http://www.xignite.com/xworldnews.asmx?WSDL
BNQuoteService = http://www.xmethods.net/sd/2001/BNQuoteService.wsdl
BabelFishService = http://www.xmethods.net/sd/2001/BabelFishService.wsdl
CATrafficService = http://www.xmethods.net/sd/2001/CATrafficService.wsdl
CurrencyExchangeService = http://www.xmethods.net/sd/2001/CurrencyExchangeService.wsdl
EBayWatcherService = http://www.xmethods.net/sd/2001/EBayWatcherService.wsdl
TemperatureService = http://www.xmethods.net/sd/2001/TemperatureService.wsdl
XMethodsFilesystemService = http://www.xmethods.net/sd/2001/XMethodsFilesystemService.wsdl
www.xmethods.net.query = http://www.xmethods.net/wsdl/query.wsdl
WSAmazonBox = http://www.xmlme.com/WSAmazonBox.asmx?WSDL
WSCustNews = http://www.xmlme.com/WSCustNews.asmx?WSDL
WSDailyNet = http://www.xmlme.com/WSDailyNet.asmx?WSDL
WSDailyXml = http://www.xmlme.com/WSDailyXml.asmx?WSDL
WSElectronics = http://www.xmlme.com/WSElectronics.asmx?WSDL
WSShakespeare = http://www.xmlme.com/WSShakespeare.asmx?WSDL
WSSportingGoods = http://www.xmlme.com/WSSportingGoods.asmx?WSDL
WSVideoGames = http://www.xmlme.com/WSVideoGames.asmx?WSDL
www.zanetti-dev.com.IZPOP3 = http://www.zanetti-dev.com/scripts/zpop3ws.exe/wsdl/IZPOP3
IHaddock = http://www2.tankebolaget.com:8080/scripts/Haddock.exe/wsdl/IHaddock
INumToWords = http://www2.tankebolaget.com:8080/scripts/NumToWords.dll/wsdl/INumToWords
IModulusCheck = http://www2.tankebolaget.com:8080/scripts/TBWS.exe/wsdl/IModulusCheck
EncodingsService = http://www25.brinkster.com/balidotnet/EncodingsService.asmx?WSDL
NumberToWords = http://www28.brinkster.com/hegdes/NumberToWords.asmx?WSDL
xml.nig.ac.jp.Blast = http://xml.nig.ac.jp/wsdl/Blast.wsdl
ClustalW = http://xml.nig.ac.jp/wsdl/ClustalW.wsdl
xml.nig.ac.jp.DDBJ = http://xml.nig.ac.jp/wsdl/DDBJ.wsdl
xml.nig.ac.jp.Fasta = http://xml.nig.ac.jp/wsdl/Fasta.wsdl
GetEntry = http://xml.nig.ac.jp/wsdl/GetEntry.wsdl
xml.nig.ac.jp.SRS = http://xml.nig.ac.jp/wsdl/SRS.wsdl
TxSearch = http://xml.nig.ac.jp/wsdl/TxSearch.wsdl
xmlserver = http://xml.redcoal.net/SMSSOAP/xmlserver.wsdl
xmlrad.com.WSDL = http://xmlrad.com/WSFindMP3Bin/WSFindMP3.dll/WSDL
xmlrad.com.WSDL.1 = http://xmlrad.com/WSGeneratorBin/WSGenerator.dll/WSDL


##########################################################################
# SECTION [broken] - Legal challenges.  Appears to be a problem
#    in the wsdl.
##########################################################################
[broken]
amazon = http://soap.amazon.com/schemas/AmazonWebServices.wsdl
rtf2html = http://www.infoaccelerator.net/cfc/rft2html.cfc?WSDL 
rtf2html = xmethods/rtf2html.xml
# circular import
www.winisp.net.books = http://www.winisp.net/cheeso/books/books.asmx?WSDL


