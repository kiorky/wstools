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
# SECTION  [no_schemas]  - 
#      no associated schemas
##########################################################################
[no_schemas] 

AbysalSendEmail  =  http://www.abysal.com/soap/AbysalEmail.wsdl
BNQuoteService  =  http://www.xmethods.net/sd/2001/BNQuoteService.wsdl
BabelFishService  =  http://www.xmethods.net/sd/2001/BabelFishService.wsdl
Bible  =  http://www.stgregorioschurchdc.org/wsdl/Bible.wsdl
Blast  =  http://xml.nig.ac.jp/wsdl/Blast.wsdl
CATrafficService  =  http://www.xmethods.net/sd/2001/CATrafficService.wsdl
Calendar  =  http://www.stgregorioschurchdc.org/wsdl/Calendar.wsdl
ClustalW  =  http://xml.nig.ac.jp/wsdl/ClustalW.wsdl
CountryInfoLookupService  =  http://www.cs.uga.edu/~sent/xmethods/CountryInfoLookup.wsdl
CurrencyExchangeService  =  http://www.xmethods.net/sd/2001/CurrencyExchangeService.wsdl
DDBJ  =  http://xml.nig.ac.jp/wsdl/DDBJ.wsdl
DiscordianService  =  http://www.compkarori.com/wsdl/discordian.wsdl
DistanceService  =  http://webservices.imacination.com/distance/Distance.jws?wsdl
DocServService  =  http://docserv.aurigalogic.com/docserv.wsdl
EMWebFunctionWS  =  http://www.eyemaginations.com/cgi-bin/getWSDL.pl?wsdl=WebFunction.wsdl
Fasta  =  http://xml.nig.ac.jp/wsdl/Fasta.wsdl
FaxService  =  http://oneoutbox.com/wsdl/FaxService.wsdl
FreeFaxService  =  http://www.OneOutBox.com/wsdl/FreeFaxService.wsdl
GetEntry  =  http://xml.nig.ac.jp/wsdl/GetEntry.wsdl
IBorlandBabelservice  =  http://ww6.borland.com/webservices/BorlandBabel/BorlandBabel.exe/wsdl/IBorlandBabel
IBorlandChessservice  =  http://www.danmarinescu.com/WebServices/ChessCGIServer.exe/wsdl/IBorlandChess
IDutchservice  =  http://www.ebob42.com/cgi-bin/NumberToWordsInDutch.exe/wsdl/IDutch
IEmailServiceservice  =  http://webservices.matlus.com/scripts/emailwebservice.dll/wsdl/IEmailService
IEuroservice  =  http://www.drbob42.co.uk/cgi-bin/Euro42/wsdl/IEuro
IHeadLineservice  =  http://www.ebob42.com/cgi-bin/DrBobsClinic.exe/wsdl/IHeadline
IMapQuestservice  =  http://ww6.borland.com/webservices/MapQuest/MapQuest.exe/wsdl/IMapQuest
IMsSessionBrokerServiceservice  =  http://webservices.matlus.com/scripts/sessionservice.dll/wsdl/IMsSessionBrokerService
IPGPKeyServerservice  =  http://www.marotz.se/PGPKeyServer/PGPKeyServiceX.exe/wsdl/IPGPKeyServer
IPrimeGeneratorservice  =  http://www.jusufdarmawan.com/wsprimegenerator.exe/wsdl/IPrimeGenerator
IRomanservice  =  http://www.ebob42.com/cgi-bin/Romulan.exe/wsdl/IRoman
ISOcode2shortformat  =  http://www.siliconllama.com/services/wsdl/ISOcode2shortformatService.wsdl
ISlashdotHeadlineProviderservice  =  http://www.marotz.se/scripts/SlashdotHeadlines.exe/wsdl/ISlashdotHeadlineProvider
ISwedishZipInfoservice  =  http://www.marotz.se/scripts/zipinfo.exe/wsdl/ISwedishZipInfo
ITempConverterservice  =  http://developerdays.com/cgi-bin/tempconverter.exe/wsdl/ITempConverter
IWSMazeServerservice  =  http://www.culand.net/WebServices/bin/WSMaze_Server.dll/wsdl/IWSMazeServer
IWagAddressServerSingleservice  =  http://62.212.78.36/cgi-bin/WagAddressServerSingle.exe/wsdl/IWagAddressServerSingle
IWhoIsservice  =  http://webservices.matlus.com/scripts/whoiswebservice.dll/wsdl/IWhoIs
Ieconomicservice  =  http://www.suiyi.com/soap/economic.dll/wsdl/Ieconomic
IgetNumbersservice  =  http://reto.checkit.ch/Scripts/Lotto.dll/wsdl/IgetNumbers
Iws_Verify_NRICservice  =  http://www.rightsecurity.biz/NRICWebServices/NRICWebServices.dll/wsdl/Iws_Verify_NRIC
KRSS_DAML_Service  =  http://digilander.libero.it/mamo78/KRSS_DAML_Service.wsdl
MBWSSoapService  =  http://www.extensio.com:8080/ExtensioInfoServer/mbsoap/MBWSSoapServices.wsdl
SRS  =  http://xml.nig.ac.jp/wsdl/SRS.wsdl
ServiceSMS  =  http://smsserver.dotnetisp.com/servicesms.asmx?WSDL
SmsService  =  http://sms.smspoint.net:8080/special/services/Sms?wsdl
TemperatureConversion  =  http://mywebservices.free.fr/server/Temperature.wsdl
TemperatureService  =  http://www.xmethods.net/sd/2001/TemperatureService.wsdl
TxSearch  =  http://xml.nig.ac.jp/wsdl/TxSearch.wsdl
UrduSOAP  =  http://www.apniurdu.com/SOAP/Urdu2.wsdl
WSFindMP3  =  http://xmlrad.com/WSFindMP3Bin/WSFindMP3.dll/WSDL
WSGenerator  =  http://xmlrad.com/WSGeneratorBin/WSGenerator.dll/WSDL
Wiki  =  http://www.wlug.org.nz/phpwiki/soap.wsdl
WorldTimeService  =  http://ws.digiposs.com/WorldTime.jws?wsdl
XEMBL  =  http://www.ebi.ac.uk/xembl/XEMBL.wsdl
XMethodsFilesystemService  =  http://www.xmethods.net/sd/2001/XMethodsFilesystemService.wsdl
YIM Service  =  http://www.scdi.org/~avernet/webservice/yim.wsdl
YahooUserPingService  =  http://www.allesta.net:51110/webservices/wsdl/YahooUserPingService.xml
convert  =  http://www.cosme.nu/services/convert.php?wsdl
dns  =  http://www.cosme.nu/services/dns.php?wsdl
eBayWatcherService  =  http://www.xmethods.net/sd/2001/EBayWatcherService.wsdl
finnwords  =  http://www.nickhodge.com/nhodge/finnwords/finnwords.wsdl
net.xmethods.services.stockquote.StockQuote  =  http://services.xmethods.net/soap/urn:xmethods-delayed-quotes.wsdl
pop  =  http://www.cosme.nu/services/pop.php?wsdl
urn:ATTPager  =  http://www.bitwaste.com/xmethods/ATTPager/ATTPager.wsdl



##########################################################################
# SECTION  [simpleTypes]  - 
#      have associated schemas with simple types
##########################################################################
[simpleTypes] 

ABA  =  http://www.webservicex.net/aba.asmx?WSDL
AmazonBox  =  http://www.xmlme.com/WSAmazonBox.asmx?WSDL
AustralianPostCode  =  http://www.webservicex.net/AustralianPostCode.asmx?WSDL
Autoloan  =  http://upload.eraserver.net/circle24/autoloan.asmx?wsdl
BNPrice  =  http://www.abundanttech.com/webservices/bnprice/bnprice.wsdl
BankCode  =  http://appserver.pepperzak.net/bankcode/BankCodeEJBHome/wsdl.jsp
BarCode  =  http://www.webservicex.net/barcode.asmx?WSDL
BibleWebservice  =  http://www.webservicex.net/BibleWebservice.asmx?wsdl
Braille  =  http://www.webservicex.net/braille.asmx?WSDL
CEqImage  =  http://otourdes.europe.webmatrixhosting.net/EqImageSharp/EqImage.asmx?WSDL
CFRSearch  =  http://www.oakleaf.ws/cfrsearchws/cfrsearchws.asmx?wsdl
CFRSect  =  http://www.oakleaf.ws/cfrsectws/cfrsectws.asmx?wsdl
CFRToc  =  http://www.oakleaf.ws/cfrtocws/cfrtocws.asmx?wsdl
CodeGenerator  =  http://www.esynaps.com/webservices/codegenerator.asmx?WSDL
CreditCardValidator  =  http://www.richsolutions.com/RichPayments/RichCardValidator.asmx?WSDL
CurrencyConvertor  =  http://www.webservicex.net/CurrencyConvertor.asmx?wsdl
Currencyws  =  http://glkev.webs.innerhost.com/glkev_ws/Currencyws.asmx?WSDL
DailyDilbert  =  http://www.esynaps.com/WebServices/DailyDiblert.asmx?WSDL
DotnetDailyFact  =  http://www.xmlme.com/WSDailyNet.asmx?WSDL
DynamicFlashWebService  =  http://www.firelife.eu.com/dynamicflash/dynamicflash.asmx?WSDL
ElectronicProductsFinder  =  http://www.xmlme.com/WSElectronics.asmx?WSDL
EncryptionWS  =  http://test.mapfrepr.net/Encryption/Encryption.asmx?WSDL
Fax  =  http://ws.acrosscommunications.com/Fax.asmx?WSDL
FinanceService  =  http://www.webservicex.net/FinanceService.asmx?WSDL
GetCustomNews  =  http://www.xmlme.com/WSCustNews.asmx?WSDL
GetLocalTime  =  http://services.develop.co.za/GetLocalTime.asmx?WSDL
GlobalWeather  =  http://www.webservicex.net/globalweather.asmx?WSDL
HCPCS  =  http://www.webservicex.net/hcpcs.asmx?WSDL
IBANFunctions  =  http://www.bitounis.com/IBAN/IBANFuncs.asmx?WSDL
ICD10  =  http://www.webservicex.net/icd10.asmx?WSDL
ICD9  =  http://www.webservicex.net/icd9.asmx?WSDL
ICD9Drug  =  http://www.webservicex.net/icd9drug.asmx?WSDL
ICD9ToICD10  =  http://www.webservicex.net/icd9toicd10.asmx?WSDL
ICQ  =  http://ws.acrosscommunications.com/ICQ.asmx?WSDL
ISearchSwedishPersonservice  =  http://www.marotz.se/scripts/searchperson.exe/wsdl/ISearchSwedishPerson
InstantMessageAlert  =  http://www.bindingpoint.com/ws/imalert/imalert.asmx?wsdl
MSProxy  =  http://www.esynaps.com/WebServices/MsProxy.asmx?WSDL
MXChecker  =  http://beta2.eraserver.net/webservices/mxchecker/mxchecker.asmx?WSDL
NAICS  =  http://www.webservicex.net/NAICS.asmx?wsdl
NFLNews  =  http://www.esynaps.com/WebServices/NFLNews.asmx?WSDL
NumPager  =  http://ws.acrosscommunications.com/NumPager.asmx?WSDL
NumberToWords  =  http://www28.brinkster.com/hegdes/NumberToWords.asmx?WSDL
OTNNews  =  http://otn.oracle.com/ws/otnnews?WSDL
Paracite  =  http://paracite.ecs.soton.ac.uk/paracite.wsdl
Phone  =  http://ws.acrosscommunications.com/Phone.asmx?WSDL
Puki  =  http://www.barnaland.is/dev/puki.asmx?WSDL
QueryIP  =  http://ws.cdyne.com/whoisforip/queryip.asmx?wsdl
Quotes  =  http://www.seshakiran.com/QuoteService/QuotesService.asmx?wsdl
QuranVerse  =  http://aspnet.lamaan.com/webservices/QuranVerse.asmx?WSDL
RSAFuncs  =  http://www.bitounis.com/RSAFunctions/RSAFuncs.asmx?WSDL
RSStoHTML  =  http://www.webservicex.net/RssToHTML.asmx?WSDL
SMS  =  http://ws.acrosscommunications.com/SMS.asmx?WSDL
SMS_1  =  http://www.barnaland.is/dev/sms.asmx?WSDL
SQLDataSoap  =  http://www.SoapClient.com/xml/SQLDataSoap.wsdl
SecureXML  =  http://www.securexml.net/securexml/securexml.wsdl
SendSMSWorld  =  http://www.webservicex.net/sendsmsworld.asmx?WSDL
Shakespeare  =  http://www.xmlme.com/WSShakespeare.asmx?WSDL
SportingGoodsFinder  =  http://www.xmlme.com/WSSportingGoods.asmx?WSDL
StockQuote  =  http://www.webservicex.net/stockquote.asmx?WSDL
StockQuotes  =  http://www.gama-system.com/webservices/stockquotes.asmx?wsdl
TAP  =  http://ws.acrosscommunications.com/TAP.asmx?WSDL
TakisActiveLib  =  http://www.forthlink.gr/TakisLib/TakisActiveLib.WSDL
UDDIBusinessFinder  =  http://www.webservicex.net/UDDIBusinessFinder.asmx?WSDL
UKLocation  =  http://www.webservicex.net/uklocation.asmx?WSDL
UNSPSCConvert  =  http://www.codemechanisms.co.uk/WebServices/UNSPSC.asmx?WSDL
USWeather  =  http://www.webservicex.net/usweather.asmx?WSDL
ValidateEmail  =  http://www.webservicex.net/ValidateEmail.asmx?WSDL
VideoGamesFinder  =  http://www.xmlme.com/WSVideoGames.asmx?WSDL
WebChart  =  http://www.gxchart.com/webchart.wsdl
WebSearchWS  =  http://www.esynaps.com/WebServices/SearchWS.asmx?WSDL
WhoIS  =  http://ws.cdyne.com/whoisquery/whois.asmx?wsdl
WhoIsService  =  http://www.esynaps.com/WebServices/WhoIsService.asmx?WSDL
XmlDailyFact  =  http://www.xmlme.com/WSDailyXml.asmx?WSDL
XmlTracking  =  http://www.baxglobal.com/xmltracking/xmltracking.asmx?wsdl
XreOnline  =  http://www.codecube.net/services/xreonline.asmx?WSDL
ZipCodesService  =  http://webservices.instantlogic.com/zipcodes.ils?wsdl
airport  =  http://www.webservicex.net/airport.asmx?wsdl
bork  =  http://www.x-ws.de/cgi-bin/bork/service.wsdl
chat  =  http://www.x-ws.de/cgi-bin/eliza/chat.wsdl
com.systinet.demo.ftp.FTPService  =  http://soap.systinet.net/demos/FTPService/wsdl
country  =  http://www.webservicex.net/country.asmx?wsdl
dConverter  =  http://www.siliconllama.com/services/wsdl/dConverterService.wsdl
eSynapsFeed  =  http://www.esynaps.com/WebServices/eSynapsFeed.asmx?WSDL
eSynapsSerach  =  http://www.esynaps.com/WebServices/eSynapsSearch.asmx?WSDL
engtoarabic  =  http://www.dl-me.com/webservices/engtoarabic.asmx?WSDL
fWArticleService  =  http://www.framewerks.com/WebServices/fWArticleService/fwArticles.asmx?WSDL
fax  =  http://www.webservicex.net/fax.asmx?wsdl
foxcentral  =  http://www.foxcentral.net/foxcentral.wsdl
getCAWeather  =  http://ocean.cse.ucsc.edu/soap/getCAWeather.wsdl
getJoke  =  http://www.interpressfact.net/webservices/getJoke.asmx?wsdl
http___ewsdemo_webmethods_com_wmpayflow_sample  =  http://ewsdemo.webmethods.com/WmEWS/directory/wsd.dsp?interface=wmpayflow.sample&service=Credit_Approval
imstatus  =  http://www.x-ws.de/cgi-bin/msn/imstatus.wsdl
periodictable  =  http://www.webservicex.net/periodictable.asmx?wsdl
piglatin  =  http://www.aspxpressway.com/maincontent/webservices/piglatin.asmx?wsdl
promotionService  =  http://interpressfact.net/webservices/promotionService.asmx?wsdl
unitext  =  http://www.dl-me.com/webservices/unitext.asmx?wsdl
wwhelpservice  =  http://www.west-wind.com/wconnect/soap/wwhelpservice.wsdl
xmlserver  =  http://xml.redcoal.net/SMSSOAP/xmlserver.wsdl



##########################################################################
# SECTION  [services_by_http]  - 
#      have associated schemas, only complex types
##########################################################################
[services_by_http] 

AddFinderService  =  http://www.lixusnet.com/lixusnet/AddFinder.jws?wsdl
AddressFinder  =  http://arcweb.esri.com/services/v2/AddressFinder.wsdl
AddressLookup  =  http://ws.cdyne.com/psaddress/addresslookup.asmx?wsdl
AlanBushCompositions  =  http://www.alanbushtrust.org.uk/soap/compositions.wsdl
AmazonQuery  =  http://majordojo.com/amazon_query/amazon_query.wsdl
BondService  =  http://www.financialwebservices.ltd.uk/axis/services/bond?wsdl
BusinessNews  =  http://glkev.webs.innerhost.com/glkev_ws/businessnews.asmx?WSDL
CarRentalQuotesService  =  http://wavendon.dsdata.co.uk/axis/services/CarRentalQuotes?wsdl
ChatLogService  =  http://www.chatlog.net/wsdl.xml
CupScores  =  http://scores.serviceobjects.com/CupScores.asmx?WSDL
DOTSAddressValidate  =  http://ws2.serviceobjects.net/av/AddressValidate.asmx?WSDL
DOTSDomainSpy  =  http://ws2.serviceobjects.net/ds/domainspy.asmx?WSDL
DOTSEmailValidate  =  http://ws2.serviceobjects.net/ev/EmailValidate.asmx?WSDL
DOTSFastQuote  =  http://ws2.serviceobjects.net/sq/FastQuote.asmx?WSDL
DOTSFastTax  =  http://ws2.serviceobjects.net/ft/FastTax.asmx?WSDL
DOTSFastWeather  =  http://ws2.serviceobjects.net/fw/FastWeather.asmx?WSDL
DOTSGeoCash  =  http://ws2.serviceobjects.net/gc/GeoCash.asmx?WSDL
DOTSGeoPhone  =  http://ws2.serviceobjects.net/gp/GeoPhone.asmx?WSDL
DOTSGeoPinPoint  =  http://ws2.serviceobjects.net/gpp/GeoPinPoint.asmx?WSDL
DOTSLotteryNumbers  =  http://ws2.serviceobjects.net/ln/lotterynumbers.asmx?WSDL
DOTSPackageTracking  =  http://ws2.serviceobjects.net/pt/PackTrack.asmx?WSDL
DOTSPatentOffice  =  http://ws2.serviceobjects.net/uspo/USPatentOffice.asmx?WSDL
DOTSPhoneAppend  =  http://ws2.serviceobjects.net/pa/phoneappend.asmx?wsdl
DOTSShippingComparison  =  http://ws2.serviceobjects.net/pc/packcost.asmx?WSDL
DOTSUPC  =  http://ws2.serviceobjects.net/upc/UPC.asmx?WSDL
DOTSYellowPages  =  http://ws2.serviceobjects.net/yp/YellowPages.asmx?WSDL
DataService  =  http://webservices.empowered.com/statsws/stats.asmx?WSDL
Dispenser  =  http://www.blackstoneonline.com/webservices/dispenser.xml
DocConverterService  =  http://telecommerce.danet.de/axis/services/DocConverterServicePort?wsdl
FOPService  =  http://live.capescience.com/wsdl/FOPService.wsdl
FedRoutingDirectoryService  =  http://demo.soapam.com/services/FedEpayDirectory/FedEpayDirectoryService.wsdl
GMChart  =  http://service.graphmagic.com/GMService/GraphMagic.asmx?wsdl
GeoPlaces  =  http://www.codebump.com/services/placelookup.asmx?wsdl
GlobalWeather  =  http://live.capescience.com/wsdl/GlobalWeather.wsdl
GoogleSearch  =  http://api.google.com/GoogleSearch.wsdl
HTMLeMail  =  http://www.framewerks.com/WebServices/HTMLeMail/HTMLeMail.asmx?WSDL
HelpfulFunctions  =  http://www.framewerks.com/WebServices/helpfulfunctions/helpfulfunctions.asmx?WSDL
HistoricalStockQuotes  =  http://glkev.webs.innerhost.com/glkev_ws/HistoricalStockQuotes.asmx?WSDL
Horoscope  =  http://www.swanandmokashi.com/HomePage/WebServices/Horoscope.asmx?WSDL
IACHSOAPservice  =  http://soap.achchex.com/exec/achsoap.dll/wsdl/IACHSOAP
IGetInflectionservice  =  http://www.verbix.com/cgi-bin/soapx.exe/wsdl/IGetInflection
IP2Geo  =  http://ws.cdyne.com/ip2geo/ip2geo.asmx?wsdl
ISOcodes  =  http://www.siliconllama.com/services/wsdl/ISOcodesService.wsdl
ISoapFindMP3service  =  http://www.agnisoft.com/soap/mssoapmp3search.xml
ITeeChartservice  =  http://www.berneda.com/scripts/TeeChartSOAP.exe/wsdl/ITeeChart
IZPOP3service  =  http://www.zanetti-dev.com/scripts/zpop3ws.exe/wsdl/IZPOP3
LookyBookService  =  http://www.winisp.net/cheeso/books/books.asmx?WSDL
MailLocate  =  http://www.maillocate.com/soap/index.php?wsdl
NavBarServer  =  http://ws.xara.com/navbar/navbar.wsdl
Online Messenger Service  =  http://www.nims.nl/soap/oms.wsdl
OnlineMessengerService  =  http://www.nims.nl/soap/oms2.wsdl
Option_x0020_Pricing_x0020_Calculator  =  http://www.indobiz.com/OptionPricing.asmx?WSDL
PersonLookup  =  http://www.barnaland.is/dev/personlookup.asmx?WSDL
Phonebook  =  http://www.barnaland.is/dev/phonebook.asmx?WSDL
PopulationWS  =  http://www.abundanttech.com/webservices/population/population.wsdl
QueryInterfaceService  =  http://www.transactionalweb.com/SOAP/globalskilocator.wsdl
QuizService  =  http://java.rus.uni-stuttgart.de/quiz/quiz.wsdl
QuoteOfTheDay  =  http://www.swanandmokashi.com/HomePage/WebServices/QuoteOfTheDay.asmx?WSDL
RateInfoClass  =  http://www.xeeinc.com/RateInformation/RateInfo.asmx?WSDL
RateInfoClass_1  =  http://www.xeeinc.com/RateInformation/Rateinfo.asmx?WSDL
RecipeService  =  http://icuisine.net/webservices/RecipeService.asmx?WSDL
RenderServer3D  =  http://ws.xara.com/graphicrender/render3d.wsdl
RichPayments  =  http://www.richsolutions.com/richpayments/richpay.asmx?WSDL
SBGGetAirFareQuoteService  =  http://wavendon.dsdata.co.uk:8080/axis/services/SBGGetAirFareQuote?wsdl
SMS  =  http://www.abctext.com/webservices/SMS.asmx?WSDL
SOAPcdtek  =  http://www.drouet-web.com/webservices/soap_cdtek.php?wsdl
SalesRankNPrice  =  http://www.PerfectXML.NET/WebServices/SalesRankNPrice/BookService.asmx?WSDL
SendSMS  =  http://www.webservicex.net/SendSMS.asmx?WSDL
Service  =  http://www.ejse.com/WeatherService/Service.asmx?WSDL
SolveSystemService  =  http://www.lixusnet.com/SolveSystem.wsdl
SpamKillerService  =  http://wavendon.dsdata.co.uk/axis/services/SpamKiller?wsdl
StockQuotes  =  http://www.swanandmokashi.com/HomePage/WebServices/StockQuotes.asmx?WSDL
TWSFissionDotNet  =  http://www.sidespace.com/ws/fission/fissiondotnet.php?wsdl
TerraService  =  http://terraservice.net/TerraService.asmx?WSDL
Transform  =  http://transform.dataconcert.com/transform.wsdl
UPSTracking  =  http://glkev.webs.innerhost.com/glkev_ws/UPSTracking.asmx?WSDL
URLjr_Library  =  http://urljr.com/soap
WeatherFetcher  =  http://glkev.webs.innerhost.com/glkev_ws/WeatherFetcher.asmx?WSDL
WeatherService  =  http://www.hkwizard.com/WeatherService.asmx?wsdl
WeatherServices  =  http://weather.unisysfsp.com/PDCWebService/WeatherServices.asmx?WSDL
WebServiceOfTheDay  =  http://www.webserviceoftheday.com/ws/soap/wsotd.asmx?wsdl
WeblogsSubscriber  =  http://soap.4s4c.com/weblogs/subscribe.wsdl
WhoIs  =  http://ws2.serviceobjects.net/whi/WhoIs.asmx?WSDL
WhoisDataService  =  http://wavendon.dsdata.co.uk/axis/services/WhoisData?wsdl
XMethodsQuery  =  http://www.xmethods.net/wsdl/query.wsdl
XigniteEdgar  =  http://www.xignite.com/xEdgar.asmx?WSDL
XigniteNews  =  http://www.xignite.com/xnews.asmx?WSDL
XigniteOptions  =  http://www.xignite.com/xoptions.asmx?WSDL
XigniteQuotes  =  http://www.xignite.com/xquotes.asmx?WSDL
XigniteRealTime  =  http://www.xignite.com/xrealtime.asmx?WSDL
XigniteRetirement  =  http://www.xignite.com/xretirement.asmx?WSDL
XigniteSecurity  =  http://www.xignite.com/xsecurity.asmx?WSDL
XigniteSimulation  =  http://www.xignite.com/xsimulation.asmx?WSDL
XigniteStatistics  =  http://www.xignite.com/xstatistics.asmx?WSDL
XigniteSurvey  =  http://www.xignite.com/xSurvey.asmx?WSDL
XigniteWorldNews  =  http://www.xignite.com/xworldnews.asmx?WSDL
YourHost  =  http://www.esynaps.com/webservices/YourHostInfo.asmx?WSDL
Zip2Geo  =  http://ws.cdyne.com/ziptogeo/zip2geo.asmx?wsdl
ZipCodeResolver  =  http://webservices.eraserver.net/zipcoderesolver/zipcoderesolver.asmx?WSDL
ZipCodes  =  http://www.codebump.com/services/zipcodelookup.asmx?wsdl
ZipcodeLookupService  =  http://www.winisp.net/cheeso/zips/ZipService.asmx?WSDL
certServices  =  http://soapclient.com/xml/certService.wsdl
check  =  http://ws.cdyne.com/SpellChecker/check.asmx?wsdl
com.systinet.demo.freedb.FreeDBService  =  http://soap.systinet.net/demos/FreeDB/wsdl
com.systinet.demo.newsfeed.version1.NewsfeedService  =  http://soap.systinet.net/demos/Newsfeed/wsdl
com.systinet.demo.rpmfind.RpmService  =  http://soap.systinet.net/demos/RpmFinder/wsdl
com.systinet.demo.search.w3c.W3CSearchService  =  http://soap.systinet.net/demos/W3CSearch/wsdl
com.systinet.demo.search.zvon.ZVONSearchService  =  http://soap.systinet.net/demos/ZVONSearch/wsdl
dic2  =  http://www.dl-me.com/webservices/dic2.asmx?WSDL
eSynapsMonitor  =  http://www.esynaps.com/WebServices/eSynapsMonitor.wsdl
ev  =  http://ws.cdyne.com/emailverify/ev.asmx?wsdl
getQuakeDataService  =  http://webservices.tei.or.th/getQuakeData.cfc?wsdl
getSessionReport  =  http://sandbox.grandcentral.com/services/reports?WSDL
pwspNoCentrbankCurRates  =  http://server1.pointwsp.net/ws/finance/currency.asmx?WSDL
sekeywordService  =  http://www.aspiringgeek.com/cfc/keyword/sekeyword.cfc?wsdl
threatService  =  http://www.boyzoid.com/threat.cfc?wsdl
urn:AldiaService  =  http://webservices.sld.cu/aldia.wsdl
urn:BarCodes  =  http://www.flash-db.com/services/ws/barCodes.wsdl
urn:CompanyInfo  =  http://www.flash-db.com/services/ws/companyInfo.wsdl
urn:FlashBarChart  =  http://www.flash-db.com/services/ws/flashBarChart.wsdl
urn:SiteInspect  =  http://www.flash-db.com/services/ws/siteInspect.wsdl
urn:WS4lsql  =  http://slashdemocracy.org/links/ws4gotze.wsdl
urn:WSIndex  =  http://www.wsindex.org/pages/wsindexLinks.wsdl
urn:what-is-around  =  http://www.what-is-around.com/awwia.wsdl
whoisService  =  http://www.nextbigleap.com/webservices/whois.cfc?wsdl
xmethods_gcd  =  http://samples.bowstreet.com/bowstreet5/webengine/xmethods/gcd/Action!getWSDL



##########################################################################
# SECTION  [WSDLReaderErrors]  - 
#      unable to load file
##########################################################################
[WSDLReaderErrors] 

BusinessList  =  http://www.esynaps.com/WebServices/BusinessList.asmx?WSDL
EvaluationService  =  http://www.onepercentsoftware.com/axis/services/EvaluationService?wsdl
FreshScoreLiveScores  =  http://www.freshscore.com/service/FreshScoreLiveScores.asmx?WSDL
Html2xml  =  http://www.dev1.eraserver.net/REFLECTIONIT/Html2xml.asmx?WSDL
ISpamCheck  =  http://soap.prowizorka.com/spam/wsdl/ISpamCheck
LogFileParser  =  http://www.bitounis.com/W3CParser/LogFileParser.asmx?WSDL
MP3Charts  =  http://webservices.mp3.com/MP3Charts.wsdl
MysicSearchEngine  =  http://mysic.com/Webservices/MysicSearchEngine.asmx?WSDL
SurveyService  =  http://survey.rila.net/SurveyService/SurveyService.asmx?wsdl
chartWS  =  http://webservices.isitedesign.com/ws/chartWS.cfc?wsdl
codepostal  =  http://www.dotnetisp.com/webservices/dotnetisp/codepostal.asmx?WSDL
computerdictionary  =  http://dotnet.cyberthink.net/computerdictionary/computerdictionary.asmx?wsdl
events  =  http://www.bitounis.com/WebEvents/events.asmx?WSDL
ftg  =  http://ws.cdyne.com/FontToGraphic/ftg.asmx?wsdl
holidays  =  http://wsdl.wsdlfeeds.com/holidays.cfc?wsdl
huzip  =  http://www.c6.hu/ws/huzip.wsdl
iifws  =  http://www.inkostar.com/wsdl/iifws/iifws.wsdl
lu  =  http://www.cs.fsu.edu/~engelen/lu.wsdl
mach  =  http://www.cgi101.com/~msmithso/wsdl/mach.wsdl
magic  =  http://www.cs.fsu.edu/~engelen/magic.wsdl
netpress1  =  http://www22.brinkster.com/horaciovallejo/netpress1.asmx?wsdl
odp  =  http://wsdl.wsdlfeeds.com/odp.cfc?wsdl
slashdotnews  =  http://webservices.isitedesign.com/ws/slashdotnews.cfc?wsdl
spell  =  http://wsdl.wsdlfeeds.com/spell.cfc?wsdl
spellcheckservice  =  http://www.worldwidedesktop.com/spellcheck/spellcheckservice.asmx?wsdl
src2html  =  http://www.dotnetisp.com/webservices/dotnetisp/src2html.asmx?WSDL
syndicate  =  http://www.forta.com/cf/tips/syndicate.cfc?wsdl
uszip  =  http://www.webservicex.net/uszip.asmx?WSDL
ville  =  http://www.dotnetisp.com/webservices/dotnetisp/ville.asmx?WSDL



##########################################################################
# SECTION  [wsdl2pythonErrors]  - 
#      errors in code generation
##########################################################################
[wsdl2pythonErrors] 

Cod_fiscaleService  =  http://www.pinellus.com/cfc/Cod_fiscale.cfc?wsdl
DeadOrAlive  =  http://www.abundanttech.com/webservices/deadoralive/deadoralive.wsdl
GetCurrencyExchange  =  http://www.atlaz.net/webservices/GetCurrencyExchange.wsdl
IndoEconoCator  =  http://www.indobiz.com/IndoEconoCator.asmx?WSDL
InterFax  =  http://ws.interfax.net/dfs.asmx?WSDL
KKwebservice  =  http://www.kannadakasturi.com/WebServices/kannadakasturiwebservice.asmx?WSDL
MapImage  =  http://arcweb.esri.com/services/v2/MapImage.wsdl
Muse.net_x0020_Client  =  http://clientservice.muse.net/ClientService.asmx?WSDL
PlaceFinderSample  =  http://arcweb.esri.com/services/v2/PlaceFinderSample.wsdl
Proximity  =  http://arcweb.esri.com/services/v2/Proximity.wsdl
Query  =  http://arcweb.esri.com/services/v2/Query.wsdl
QueryInterfaceService  =  http://www.transactionalweb.com/SOAP/globalocator.wsdl
RentDB2  =  http://freene.dynip.com/RentDB2/RentDB2.asmx?wsdl
RouteFinder  =  http://arcweb.esri.com/services/v2/RouteFinder.wsdl
SID64sidRANK  =  http://www.sid64.com/soap/sidrank.php?wsdl
SearchMusicTeachers  =  http://www.PerfectXML.net/WebServices/MusicTeachers/MusicTeachers.asmx?wsdl
Statistics  =  http://www.strikeiron.com/scripts/statistics.asmx?WSDL
StockServices  =  http://glkev.webs.innerhost.com/glkev_ws/StockServices.asmx?WSDL
adSearch  =  http://www.interpressfact.net/webservices/getAds.asmx?wsdl
myMappingService  =  http://mywebservices.free.fr/server/BusinessPartner.wsdl
pos_public  =  http://iis1.grantparksoftware.com:8080/gps/pos_public.asmx?WSDL
pwspPostalSearch  =  http://server1.pointwsp.net/ws/postal/main.asmx?WSDL
smtpserver  =  http://www.cosme.nu/services/smtpserver.php?wsdl
zipCodeService  =  http://www.discoverdance.co.uk/zipQuery/zipCodeService.asmx?wsdl

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

