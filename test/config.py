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
# SECTION [no_schemas] -
#      no associated schemas
##########################################################################
[no_schemas]

IEuroservice  =  http://www.drbob42.co.uk/cgi-bin/Euro42/wsdl/IEuro
GetEntry  =  http://xml.nig.ac.jp/wsdl/GetEntry.wsdl
DistanceService  =  http://webservices.imacination.com/distance/Distance.jws?wsdl
IBorlandBabelservice  =  http://ww6.borland.com/webservices/BorlandBabel/BorlandBabel.exe/wsdl/IBorlandBabel
IHeadLineservice  =  http://www.ebob42.com/cgi-bin/DrBobsClinic.exe/wsdl/IHeadline
pop  =  http://www.cosme.nu/services/pop.php?wsdl
IPGPKeyServerservice  =  http://www.marotz.se/PGPKeyServer/PGPKeyServiceX.exe/wsdl/IPGPKeyServer
DiscordianService  =  http://www.compkarori.com/wsdl/discordian.wsdl
WSFindMP3  =  http://xmlrad.com/WSFindMP3Bin/WSFindMP3.dll/WSDL
ISlashdotHeadlineProviderservice  =  http://www.marotz.se/scripts/SlashdotHeadlines.exe/wsdl/ISlashdotHeadlineProvider
UrduSOAP  =  http://www.apniurdu.com/SOAP/Urdu2.wsdl
EMWebFunctionWSs  =  http://www.eyemaginations.com/cgi-bin/getWSDL.pl?wsdl=WebFunction.wsdl
YahooUserPingService  =  http://www.allesta.net:51110/webservices/wsdl/YahooUserPingService.xml
MortgageCalculator  =  http://demo.eltegra.com/webservices/wsdl?app=MortgageCalculator
FreeFaxService  =  http://www.OneOutBox.com/wsdl/FreeFaxService.wsdl
TxSearch  =  http://xml.nig.ac.jp/wsdl/TxSearch.wsdl
IgetNumbersservice  =  http://reto.checkit.ch/Scripts/Lotto.dll/wsdl/IgetNumbers
ITempConverterservice  =  http://developerdays.com/cgi-bin/tempconverter.exe/wsdl/ITempConverter
CarPayment  =  http://demo.eltegra.com/webservices/wsdl?app=CarPayment
IEmailServiceservice  =  http://webservices.matlus.com/scripts/emailwebservice.dll/wsdl/IEmailService
FaxService  =  http://oneoutbox.com/wsdl/FaxService.wsdl
SurveyService  =  http://survey.rila.net/SurveyService/SurveyService.asmx?wsdl
ATTPager  =  http://www.bitwaste.com/xmethods/ATTPager/ATTPager.wsdl
IRomanservice  =  http://www.ebob42.com/cgi-bin/Romulan.exe/wsdl/IRoman
dns  =  http://www.cosme.nu/services/dns.php?wsdl
IWSMazeServerservice  =  http://www.culand.net/WebServices/bin/WSMaze_Server.dll/wsdl/IWSMazeServer
MBWSSoapService  =  http://www.extensio.com:8080/ExtensioInfoServer/mbsoap/MBWSSoapServices.wsdl
Blast  =  http://xml.nig.ac.jp/wsdl/Blast.wsdl
XEMBL  =  http://www.ebi.ac.uk/xembl/XEMBL.wsdl
DDBJ  =  http://xml.nig.ac.jp/wsdl/DDBJ.wsdl
finnwords  =  http://www.nickhodge.com/nhodge/finnwords/finnwords.wsdl
Bible  =  http://www.stgregorioschurchdc.org/wsdl/Bible.wsdl
IMsSessionBrokerServiceservice  =  http://webservices.matlus.com/scripts/sessionservice.dll/wsdl/IMsSessionBrokerService
ISpamCheckservice  =  http://soap.prowizorka.com/spam/wsdl/ISpamCheck
IBorlandChessservice  =  http://www.danmarinescu.com/WebServices/ChessCGIServer.exe/wsdl/IBorlandChess
SRS  =  http://xml.nig.ac.jp/wsdl/SRS.wsdl
IDutchservice  =  http://www.ebob42.com/cgi-bin/NumberToWordsInDutch.exe/wsdl/IDutch
TemperatureConversion  =  http://mywebservices.free.fr/server/Temperature.wsdl
Calendar  =  http://www.stgregorioschurchdc.org/wsdl/Calendar.wsdl
Wiki  =  http://www.wlug.org.nz/phpwiki/soap.wsdl
convert  =  http://www.cosme.nu/services/convert.php?wsdl
ClustalW  =  http://xml.nig.ac.jp/wsdl/ClustalW.wsdl
ISwedishZipInfoservice  =  http://www.marotz.se/scripts/zipinfo.exe/wsdl/ISwedishZipInfo
YIM Service  =  http://www.scdi.org/~avernet/webservice/yim.wsdl
IMapQuestservice  =  http://ww6.borland.com/webservices/MapQuest/MapQuest.exe/wsdl/IMapQuest
WSGenerator  =  http://xmlrad.com/WSGeneratorBin/WSGenerator.dll/WSDL
KRSS_DAML_Service  =  http://digilander.libero.it/mamo78/KRSS_DAML_Service.wsdl
IWagAddressServerSingleservice  =  http://62.212.78.36/cgi-bin/WagAddressServerSingle.exe/wsdl/IWagAddressServerSingle
CountryInfoLookupService  =  http://www.cs.uga.edu/~sent/xmethods/CountryInfoLookup.wsdl
Verify_NRICservice  =  http://www.rightsecurity.biz/wsdl/NRICWebServices.dll/wsdl/Iws_Verify_NRIC
Fasta  =  http://xml.nig.ac.jp/wsdl/Fasta.wsdl
IWhoIsservice  =  http://webservices.matlus.com/scripts/whoiswebservice.dll/wsdl/IWhoIs
ISOcode2shortformat  =  http://www.siliconllama.com/services/wsdl/ISOcode2shortformatService.wsdl


##########################################################################
# SECTION [simpleTypes] - 
#      have associated schemas with simple types
##########################################################################
[simpleTypes]

NumPager  =  http://ws.acrosscommunications.com/NumPager.asmx?WSDL
dConverter  =  http://www.siliconllama.com/services/wsdl/dConverterService.wsdl
CodeGenerator  =  http://www.esynaps.com/webservices/codegenerator.asmx?WSDL
EncryptionWS  =  http://test.mapfrepr.net/Encryption/Encryption.asmx?WSDL
IBANFunctions  =  http://www.bitounis.com/IBAN/IBANFuncs.asmx?WSDL
Puki  =  http://www.barnaland.is/dev/puki.asmx?WSDL
GetCustomNews  =  http://www.xmlme.com/WSCustNews.asmx?WSDL
SMS  =  http://ws.acrosscommunications.com/SMS.asmx?WSDL
VideoGamesFinder  =  http://www.xmlme.com/WSVideoGames.asmx?WSDL
WhoIsService  =  http://www.esynaps.com/WebServices/WhoIsService.asmx?WSDL
xmlserver  =  http://xml.redcoal.net/SMSSOAP/xmlserver.wsdl
bork  =  http://www.x-ws.de/cgi-bin/bork/service.wsdl
Shakespeare  =  http://www.xmlme.com/WSShakespeare.asmx?WSDL
eSynapsFeed  =  http://www.esynaps.com/WebServices/eSynapsFeed.asmx?WSDL
CFRToc  =  http://www.oakleaf.ws/cfrtocws/cfrtocws.asmx?wsdl
unitext  =  http://www.dl-me.com/webservices/unitext.asmx?wsdl
WebSearchWS  =  http://www.esynaps.com/WebServices/SearchWS.asmx?WSDL
WebChart  =  http://www.gxchart.com/webchart.wsdl
GetLocalTime  =  http://services.develop.co.za/GetLocalTime.asmx?WSDL
SecureXML  =  http://www.securexml.net/securexml/securexml.wsdl
QueryIP  =  http://ws.cdyne.com/whoisforip/queryip.asmx?wsdl
UNSPSCConvert  =  http://www.codemechanisms.co.uk/WebServices/UNSPSC.asmx?WSDL
XmlTracking  =  http://www.baxglobal.com/xmltracking/xmltracking.asmx?wsdl
getCAWeather  =  http://ocean.cse.ucsc.edu/soap/getCAWeather.wsdl
wwhelpservice  =  http://www.west-wind.com/wconnect/soap/wwhelpservice.wsdl
QuranVerse  =  http://aspnet.lamaan.com/webservices/QuranVerse.asmx?WSDL
DailyDilbert  =  http://www.esynaps.com/WebServices/DailyDiblert.asmx?WSDL
promotionService  =  http://interpressfact.net/webservices/promotionService.asmx?wsdl
imstatus  =  http://www.x-ws.de/cgi-bin/msn/imstatus.wsdl
WhoIS  =  http://ws.cdyne.com/whoisquery/whois.asmx?wsdl
NFLNews  =  http://www.esynaps.com/WebServices/NFLNews.asmx?WSDL
CFRSearch  =  http://www.oakleaf.ws/cfrsearchws/cfrsearchws.asmx?wsdl
Phone  =  http://ws.acrosscommunications.com/Phone.asmx?WSDL
CreditCardValidator  =  http://www.richsolutions.com/RichPayments/RichCardValidator.asmx?WSDL
piglatin  =  http://www.aspxpressway.com/maincontent/webservices/piglatin.asmx?wsdl
SMS.1  =  http://www.barnaland.is/dev/sms.asmx?WSDL
fWArticleService  =  http://www.framewerks.com/WebServices/fWArticleService/fwArticles.asmx?WSDL
TAP  =  http://ws.acrosscommunications.com/TAP.asmx?WSDL
ZipCodesService  =  http://webservices.instantlogic.com/zipcodes.ils?wsdl
MSProxy  =  http://www.esynaps.com/WebServices/MsProxy.asmx?WSDL
SQLDataSoap  =  http://www.SoapClient.com/xml/SQLDataSoap.wsdl
engtoarabic  =  http://www.dl-me.com/webservices/engtoarabic.asmx?WSDL
DotnetDailyFact  =  http://www.xmlme.com/WSDailyNet.asmx?WSDL
foxcentral  =  http://www.foxcentral.net/foxcentral.wsdl
Fax  =  http://ws.acrosscommunications.com/Fax.asmx?WSDL
FTPService  =  http://soap.systinet.net/demos/FTPService/wsdl
ISearchSwedishPersonservice  =  http://www.marotz.se/scripts/searchperson.exe/wsdl/ISearchSwedishPerson
XreOnline  =  http://www.codecube.net/services/xreonline.asmx?WSDL
chat  =  http://www.x-ws.de/cgi-bin/eliza/chat.wsdl
CFRSect  =  http://www.oakleaf.ws/cfrsectws/cfrsectws.asmx?wsdl
CEqImage  =  http://otourdes.europe.webmatrixhosting.net/EqImageSharp/EqImage.asmx?WSDL
ICQ  =  http://ws.acrosscommunications.com/ICQ.asmx?WSDL
OTNNews  =  http://otn.oracle.com/ws/otnnews?WSDL
wmpayflow  =  http://ewsdemo.webmethods.com/WmEWS/directory/wsd.dsp?interface=wmpayflow.sample&service=Credit_Approval
TakisActiveLib  =  http://www.forthlink.gr/TakisLib/TakisActiveLib.WSDL
MXChecker  =  http://beta2.eraserver.net/webservices/mxchecker/mxchecker.asmx?WSDL
ElectronicProductsFinder  =  http://www.xmlme.com/WSElectronics.asmx?WSDL
RSAFuncs  =  http://www.bitounis.com/RSAFunctions/RSAFuncs.asmx?WSDL
InstantMessageAlert  =  http://www.bindingpoint.com/ws/imalert/imalert.asmx?wsdl
Autoloan  =  http://upload.eraserver.net/circle24/autoloan.asmx?wsdl
Currencyws  =  http://glkev.webs.innerhost.com/glkev_ws/Currencyws.asmx?WSDL
AmazonBox  =  http://www.xmlme.com/WSAmazonBox.asmx?WSDL
Quotes  =  http://www.seshakiran.com/QuoteService/QuotesService.asmx?wsdl
eSynapsSerach  =  http://www.esynaps.com/WebServices/eSynapsSearch.asmx?WSDL
SportingGoodsFinder  =  http://www.xmlme.com/WSSportingGoods.asmx?WSDL
BankCode  =  http://appserver.pepperzak.net/bankcode/BankCodeEJBHome/wsdl.jsp
XmlDailyFact  =  http://www.xmlme.com/WSDailyXml.asmx?WSDL
DynamicFlashWebService  =  http://www.firelife.eu.com/dynamicflash/dynamicflash.asmx?WSDL
Paracite  =  http://paracite.ecs.soton.ac.uk/paracite.wsdl


##########################################################################
# SECTION [services_by_http] - 
#      have associated schemas with complex types, but many are just
#      sequences
##########################################################################
[services_by_http]

Service  =  http://www.ejse.com/WeatherService/Service.asmx?WSDL
SolveSystemService  =  http://www.lixusnet.com/SolveSystem.wsdl
DOTSFastWeather  =  http://ws2.serviceobjects.net/fw/FastWeather.asmx?WSDL
AmazonQuery  =  http://majordojo.com/amazon_query/amazon_query.wsdl
DOTSUPC  =  http://ws2.serviceobjects.net/upc/UPC.asmx?WSDL
SlashdotNewsService  =  http://webservices.isitedesign.com/ws/slashdotnews.cfc?wsdl
WhoIs  =  http://ws2.serviceobjects.net/whi/WhoIs.asmx?WSDL
GMChart  =  http://service.graphmagic.com/GMService/GraphMagic.asmx?wsdl
QueryInterfaceService  =  http://www.transactionalweb.com/SOAP/globalskilocator.wsdl
AlanBushCompositions  =  http://www.alanbushtrust.org.uk/soap/compositions.wsdl
Zip2Geo  =  http://ws.cdyne.com/ziptogeo/zip2geo.asmx?wsdl
odpService  =  http://wsdl.wsdlfeeds.com/odp.cfc?wsdl
QuizService  =  http://java.rus.uni-stuttgart.de/quiz/quiz.wsdl
QuoteOfTheDay  =  http://www.swanandmokashi.com/HomePage/WebServices/QuoteOfTheDay.asmx?WSDL
DOTSPackageTracking  =  http://ws2.serviceobjects.net/pt/PackTrack.asmx?WSDL
SOAPcdtek  =  http://www.drouet-web.com/webservices/soap_cdtek.php?wsdl
DOTSFastQuote  =  http://ws2.serviceobjects.net/sq/FastQuote.asmx?WSDL
ZipCodeResolver  =  http://webservices.eraserver.net/zipcoderesolver/zipcoderesolver.asmx?WSDL
Dispenser  =  http://www.blackstoneonline.com/webservices/dispenser.xml
ISoapFindMP3service  =  http://www.agnisoft.com/soap/mssoapmp3search.xml
StockQuotes  =  http://www.swanandmokashi.com/HomePage/WebServices/StockQuotes.asmx?WSDL
Calculator  =  http://www.indobiz.com/OptionPricing.asmx?WSDL
DOTSDomainSpy  =  http://ws2.serviceobjects.net/ds/domainspy.asmx?WSDL
WS4lsql  =  http://slashdemocracy.org/links/ws4gotze.wsdl
dic2  =  http://www.dl-me.com/webservices/dic2.asmx?WSDL
WeatherService  =  http://www.hkwizard.com/WeatherService.asmx?wsdl
threatService  =  http://www.boyzoid.com/threat.cfc?wsdl
XigniteEdgar  =  http://www.xignite.com/xEdgar.asmx?WSDL
NavBarServer  =  http://ws.xara.com/navbar/navbar.wsdl
ITeeChartservice  =  http://www.berneda.com/scripts/TeeChartSOAP.exe/wsdl/ITeeChart
W3CSearchService  =  http://soap.systinet.net/demos/W3CSearch/wsdl
SBGGetAirFareQuoteService  =  http://wavendon.dsdata.co.uk:8080/axis/services/SBGGetAirFareQuote?wsdl
DOTSShippingComparison  =  http://ws2.serviceobjects.net/pc/packcost.asmx?WSDL
HTMLeMail  =  http://www.framewerks.com/WebServices/HTMLeMail/HTMLeMail.asmx?WSDL
xmethods_gcd  =  http://samples.bowstreet.com/bowstreet5/webengine/xmethods/gcd/Action!getWSDL
WeblogsSubscriber  =  http://soap.4s4c.com/weblogs/subscribe.wsdl
ev  =  http://ws.cdyne.com/emailverify/ev.asmx?wsdl
YourHost  =  http://www.esynaps.com/webservices/YourHostInfo.asmx?WSDL
XigniteWorldNews  =  http://www.xignite.com/xworldnews.asmx?WSDL
DocConverterService  =  http://telecommerce.danet.de/axis/services/DocConverterServicePort?wsdl
sekeywordService  =  http://www.aspiringgeek.com/cfc/keyword/sekeyword.cfc?wsdl
spellService  =  http://wsdl.wsdlfeeds.com/spell.cfc?wsdl
OnlineMessengerService  =  http://www.nims.nl/soap/oms2.wsdl
WebServiceOfTheDay  =  http://www.webserviceoftheday.com/ws/soap/wsotd.asmx?wsdl
RecipeService  =  http://icuisine.net/webservices/RecipeService.asmx?WSDL
RichPayments  =  http://www.richsolutions.com/richpayments/richpay.asmx?WSDL
DOTSPatentOffice  =  http://ws2.serviceobjects.net/uspo/USPatentOffice.asmx?WSDL
IZPOP3service  =  http://www.zanetti-dev.com/scripts/zpop3ws.exe/wsdl/IZPOP3
DOTSGeoPinPoint  =  http://ws2.serviceobjects.net/gpp/GeoPinPoint.asmx?WSDL
getQuakeDataService  =  http://webservices.tei.or.th/getQuakeData.cfc?wsdl
AddressLookup  =  http://ws.cdyne.com/psaddress/addresslookup.asmx?wsdl
PersonLookup  =  http://www.barnaland.is/dev/personlookup.asmx?WSDL
WSIndex  =  http://www.wsindex.org/pages/wsindexLinks.wsdl
DOTSAddressValidate  =  http://ws2.serviceobjects.net/av/AddressValidate.asmx?WSDL
FreeDBService  =  http://soap.systinet.net/demos/FreeDB/wsdl
WeatherServices  =  http://weather.unisysfsp.com/PDCWebService/WeatherServices.asmx?WSDL
whoisService  =  http://www.nextbigleap.com/webservices/whois.cfc?wsdl
SpamKillerService  =  http://wavendon.dsdata.co.uk/axis/services/SpamKiller?wsdl
MailLocate  =  http://www.maillocate.com/soap/index.php?wsdl
TerraService  =  http://terraservice.net/TerraService.asmx?WSDL
GeoPlaces  =  http://www.codebump.com/services/placelookup.asmx?wsdl
AldiaService  =  http://webservices.sld.cu/aldia.wsdl
certServices  =  http://soapclient.com/xml/certService.wsdl
SMS.2  =  http://www.abctext.com/webservices/SMS.asmx?WSDL
Transform  =  http://transform.dataconcert.com/transform.wsdl
DOTSPhoneAppend  =  http://ws2.serviceobjects.net/pa/phoneappend.asmx?wsdl
RenderServer3D  =  http://ws.xara.com/graphicrender/render3d.wsdl
AddressFinder  =  http://arcweb.esri.com/services/v2/AddressFinder.wsdl
DOTSGeoCash  =  http://ws2.serviceobjects.net/gc/GeoCash.asmx?WSDL
XigniteSimulation  =  http://www.xignite.com/xsimulation.asmx?WSDL
FedRoutingDirectoryService  =  http://demo.soapam.com/services/FedEpayDirectory/FedEpayDirectoryService.wsdl
XigniteOptions  =  http://www.xignite.com/xoptions.asmx?WSDL
holidaysService  =  http://wsdl.wsdlfeeds.com/holidays.cfc?wsdl
IP2Geo  =  http://ws.cdyne.com/ip2geo/ip2geo.asmx?wsdl
OTNMobileWrapper  =  http://otn.oracle.com/ws/9iasmobile?WSDL
XigniteRetirement  =  http://www.xignite.com/xretirement.asmx?WSDL
ZipCodes  =  http://www.codebump.com/services/zipcodelookup.asmx?wsdl
XigniteQuotes  =  http://www.xignite.com/xquotes.asmx?WSDL
URLjr_Library  =  http://urljr.com/soap
ISOcodes  =  http://www.siliconllama.com/services/wsdl/ISOcodesService.wsdl
DOTSFastTax  =  http://ws2.serviceobjects.net/ft/FastTax.asmx?WSDL
tt4d_WebService  =  http://194.98.194.111/4dwsdl
IACHSOAPservice  =  http://soap.achchex.com/exec/achsoap.dll/wsdl/IACHSOAP
pwspNoCentrbankCurRates  =  http://server1.pointwsp.net/ws/finance/currency.asmx?WSDL
IGetInflectionservice  =  http://www.verbix.com/cgi-bin/soapx.exe/wsdl/IGetInflection
NewsfeedService  =  http://soap.systinet.net/demos/Newsfeed/wsdl
GoogleSearch  =  http://api.google.com/GoogleSearch.wsdl
DataService  =  http://webservices.empowered.com/statsws/stats.asmx?WSDL
FlashBarChart  =  http://www.flash-db.com/services/ws/flashBarChart.wsdl
RpmService  =  http://soap.systinet.net/demos/RpmFinder/wsdl
what-is-around  =  http://www.what-is-around.com/awwia.wsdl
RateInfoClass  =  http://www.xeeinc.com/RateInformation/RateInfo.asmx?WSDL
ZipcodeLookupService  =  http://www.winisp.net/cheeso/zips/ZipService.asmx?WSDL
BarCodes  =  http://www.flash-db.com/services/ws/barCodes.wsdl
TWSFissionDotNet  =  http://www.sidespace.com/ws/fission/fissiondotnet.php?wsdl
DOTSLotteryNumbers  =  http://ws2.serviceobjects.net/ln/lotterynumbers.asmx?WSDL
CompanyInfo  =  http://www.flash-db.com/services/ws/companyInfo.wsdl
WeatherFetcher  =  http://glkev.webs.innerhost.com/glkev_ws/WeatherFetcher.asmx?WSDL
XigniteNews  =  http://www.xignite.com/xnews.asmx?WSDL
check  =  http://ws.cdyne.com/SpellChecker/check.asmx?wsdl
BusinessNews  =  http://glkev.webs.innerhost.com/glkev_ws/businessnews.asmx?WSDL
CarRentalQuotesService  =  http://wavendon.dsdata.co.uk/axis/services/CarRentalQuotes?wsdl
Online Messenger Service  =  http://www.nims.nl/soap/oms.wsdl
XigniteStatistics  =  http://www.xignite.com/xstatistics.asmx?WSDL
DOTSYellowPages  =  http://ws2.serviceobjects.net/yp/YellowPages.asmx?WSDL
CupScores  =  http://scores.serviceobjects.com/CupScores.asmx?WSDL
DOTSGeoPhone  =  http://ws2.serviceobjects.net/gp/GeoPhone.asmx?WSDL
HistoricalStockQuotes  =  http://glkev.webs.innerhost.com/glkev_ws/HistoricalStockQuotes.asmx?WSDL
DOTSEmailValidate  =  http://ws2.serviceobjects.net/ev/EmailValidate.asmx?WSDL
HelpfulFunctions  =  http://www.framewerks.com/WebServices/helpfulfunctions/helpfulfunctions.asmx?WSDL
ChatLogService  =  http://www.chatlog.net/wsdl.xml
chartWSService  =  http://webservices.isitedesign.com/ws/chartWS.cfc?wsdl
UPSTracking  =  http://glkev.webs.innerhost.com/glkev_ws/UPSTracking.asmx?WSDL
getSessionReport  =  http://sandbox.grandcentral.com/services/reports?WSDL
eSynapsMonitor  =  http://www.esynaps.com/WebServices/eSynapsMonitor.wsdl
Horoscope  =  http://www.swanandmokashi.com/HomePage/WebServices/Horoscope.asmx?WSDL
ZVONSearchService  =  http://soap.systinet.net/demos/ZVONSearch/wsdl
XigniteSecurity  =  http://www.xignite.com/xsecurity.asmx?WSDL
XigniteSurvey  =  http://www.xignite.com/xSurvey.asmx?WSDL
SiteInspect  =  http://www.flash-db.com/services/ws/siteInspect.wsdl


##########################################################################
# SECTION [ WSDLReaderErrors ] - 
#      unable to load file with WSDLReader
##########################################################################
[WSDLReaderErrors]

www.bitounis.com.events  =  http://www.bitounis.com/WebEvents/events.asmx?WSDL
codepostal  =  http://www.dotnetisp.com/webservices/dotnetisp/codepostal.asmx?WSDL
www.cs.fsu.edu.magic  =  http://www.cs.fsu.edu/~engelen/magic.wsdl
ihaddock  =  http://www2.tankebolaget.com:8080/scripts/Haddock.exe/wsdl/IHaddock
encodingsservice  =  http://www25.brinkster.com/balidotnet/EncodingsService.asmx?WSDL
inumtowords  =  http://www2.tankebolaget.com:8080/scripts/NumToWords.dll/wsdl/INumToWords
www.xmethods.net.query  =  http://www.xmethods.net/wsdl/query.wsdl
www.financialwebservices.ltd.uk.bond  =  http://www.financialwebservices.ltd.uk/axis/services/bond?wsdl
cod_fiscale  =  http://www.pinellus.com/cfc/Cod_fiscale.cfc?wsdl
www.cgi101.com.mach  =  http://www.cgi101.com/~msmithso/wsdl/mach.wsdl
evaluationservice  =  http://www.onepercentsoftware.com/axis/services/EvaluationService?wsdl
computerdictionary  =  http://dotnet.cyberthink.net/computerdictionary/computerdictionary.asmx?wsdl
html2xml  =  http://www.dev1.eraserver.net/REFLECTIONIT/Html2xml.asmx?WSDL
babelfishservice  =  http://www.xmethods.net/sd/2001/BabelFishService.wsdl
nascardataservice  =  http://www.einsteinware.com/webservices/nascar/nascardataservice.asmx?WSDL
xmethodsfilesystemservice  =  http://www.xmethods.net/sd/2001/XMethodsFilesystemService.wsdl
www.cs.fsu.edu.lu  =  http://www.cs.fsu.edu/~engelen/lu.wsdl
mysicsearchengine  =  http://mysic.com/Webservices/MysicSearchEngine.asmx?WSDL
bnquoteservice  =  http://www.xmethods.net/sd/2001/BNQuoteService.wsdl
logfileparser  =  http://www.bitounis.com/W3CParser/LogFileParser.asmx?WSDL
businesslist  =  http://www.esynaps.com/WebServices/BusinessList.asmx?WSDL
xmethods-domainchecker  =  http://services.xmethods.net/soap/urn:xmethods-DomainChecker.wsdl
www.dotnetisp.com.ville  =  http://www.dotnetisp.com/webservices/dotnetisp/ville.asmx?WSDL
sidrank  =  http://www.sid64.com/soap/sidrank.php?wsdl
ebaywatcherservice  =  http://www.xmethods.net/sd/2001/EBayWatcherService.wsdl
ws.cdyne.com.ftg  =  http://ws.cdyne.com/FontToGraphic/ftg.asmx?wsdl
emailservices  =  http://www.einsteinware.com/webservices/email/emailservices.asmx?WSDL
syndicate  =  http://www.forta.com/cf/tips/syndicate.cfc?wsdl
mp3charts  =  http://webservices.mp3.com/MP3Charts.wsdl
xmethods-delayed-quotes  =  http://services.xmethods.net/soap/urn:xmethods-delayed-quotes.wsdl
catrafficservice  =  http://www.xmethods.net/sd/2001/CATrafficService.wsdl
www.c6.hu.huzip  =  http://www.c6.hu/ws/huzip.wsdl
numbertowords  =  http://www28.brinkster.com/hegdes/NumberToWords.asmx?WSDL
freshscorelivescores  =  http://www.freshscore.com/service/FreshScoreLiveScores.asmx?WSDL
phonebook  =  http://www.barnaland.is/dev/phonebook.asmx?WSDL
currencyexchangeservice  =  http://www.xmethods.net/sd/2001/CurrencyExchangeService.wsdl
temperatureservice  =  http://www.xmethods.net/sd/2001/TemperatureService.wsdl
spellcheckservice  =  http://www.worldwidedesktop.com/spellcheck/spellcheckservice.asmx?wsdl
src2html  =  http://www.dotnetisp.com/webservices/dotnetisp/src2html.asmx?WSDL
imoduluscheck  =  http://www2.tankebolaget.com:8080/scripts/TBWS.exe/wsdl/IModulusCheck


##########################################################################
# SECTION [wsdl2pythonErrors] - 
#      errors in code generation
##########################################################################
[wsdl2pythonErrors]

RentDB2  =  http://freene.dynip.com/RentDB2/RentDB2.asmx?wsdl
GetCurrencyExchange  =  http://www.atlaz.net/webservices/GetCurrencyExchange.wsdl
QueryInterfaceService  =  http://www.transactionalweb.com/SOAP/globalocator.wsdl
PlaceFinderSample  =  http://arcweb.esri.com/services/v2/PlaceFinderSample.wsdl
MapImage  =  http://arcweb.esri.com/services/v2/MapImage.wsdl
Statistics  =  http://www.strikeiron.com/scripts/statistics.asmx?WSDL
IndoEconoCator  =  http://www.indobiz.com/IndoEconoCator.asmx?WSDL
Proximity  =  http://arcweb.esri.com/services/v2/Proximity.wsdl
StockServices  =  http://glkev.webs.innerhost.com/glkev_ws/StockServices.asmx?WSDL
Muse.net_x0020_Client_x0020_Web_x0020_Service  =  http://clientservice.muse.net/ClientService.asmx?WSDL
InterFax  =  http://ws.interfax.net/dfs.asmx?WSDL
pwspPostalSearch  =  http://server1.pointwsp.net/ws/postal/main.asmx?WSDL
pos_public  =  http://iis1.grantparksoftware.com:8080/gps/pos_public.asmx?WSDL
myMappingService  =  http://mywebservices.free.fr/server/BusinessPartner.wsdl
zipCodeService  =  http://www.discoverdance.co.uk/zipQuery/zipCodeService.asmx?wsdl
Query  =  http://arcweb.esri.com/services/v2/Query.wsdl
smtpserver  =  http://www.cosme.nu/services/smtpserver.php?wsdl
RouteFinder  =  http://arcweb.esri.com/services/v2/RouteFinder.wsdl
Orbitarium  =  http://www.orbitarium.com/schemas/ows.wsdl
KKwebservice  =  http://www.kannadakasturi.com/WebServices/kannadakasturiwebservice.asmx?WSDL


##########################################################################
# SECTION [broken] - Legal challenges.  Appears to be a problem
#    in the wsdl.
##########################################################################
[broken]
amazon = http://soap.amazon.com/schemas/AmazonWebServices.wsdl
rtf2html = http://www.infoaccelerator.net/cfc/rft2html.cfc?WSDL 
# circular import
books = http://www.winisp.net/cheeso/books/books.asmx?WSDL
# bad import statement, bad element declarations
geoserve  =  http://www.transactionalweb.com/SOAP/geoserve.wsdl

# files
rtf2html = xmethods/rtf2html.xml
amazon = xmethods/AmazonWebServices.wsdl
books = xmethods/books.wsdl

