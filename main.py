from os import system
import socket
import time
import requests
from googlesearch import search


def Site() :

        print("Hi Welcome !!!!!!!!!!!")        
        print("1.Sql Injection")
        print("2.Get Ip Address")
        print("3.Search For Site")
        ValId = int(input("Enter Your Requests ==>> "))
        if (ValId == 1) :
            nameSite = []
            nameTarget = input("Enter Your Name Target ==>> ")
            googleDork = ["site :" , "inurl :" , "intitle :" , "intext :" , "define :" , "site :" , "phonebook :" , "maps" , "book" , "info :" , "movie :" , "weather : " , "related :" , "link :"]
            for dork in googleDork :
                Dork = dork + nameTarget
                SiteDorkSearch = search(Dork)
                for Site in SiteDorkSearch :
                    print(Site)
                    print("\n")
            print("-------------Start---------------")
            print("Your Target :" , nameTarget)
            print(search(nameTarget))
            SiteSearchName = search(nameTarget)
            for site in SiteSearchName :
                nameSite.append(site)
                if "http" or "https" in site :
                    print(requests.get(site))
                #    requestsChecker = requests.get(site)
                #    if "[200]" in requestsChecker :
                #        print("ture")
                #        print(requestsChecker)
                #    else :
                #        print("false")
                #        print(requestsChecker)

                        
                else :
                    print("The Url IS Invlid")

                print(site + "\n")
            print("--------------end-----------------")
            for site in nameSite :
                print(site + "\n")
        elif (ValId == 2) :
            Target = str(input("Enter Your Site's Name ==>> "))
            Tld = ["AAA","AARP","ABARTH","ABB","ABBOTT","ABBVIE","ABC","ABLE","ABOGADO","ABUDHABI","AC","ACADEMY","ACCENTURE","ACCOUNTANT","ACCOUNTANTS","ACO","ACTOR","AD","ADAC","ADS","ADULT","AE","AEG","AERO","AETNA","AF","AFAMILYCOMPANY","AFL","AFRICA","AG","AGAKHAN","AGENCY","AI","AIG","AIRBUS","AIRFORCE","AIRTEL","AKDN","AL","ALFAROMEO","ALIBABA","ALIPAY","ALLFINANZ","ALLSTATE","ALLY","ALSACE","ALSTOM","AM","AMAZON","AMERICANEXPRESS","AMERICANFAMILY","AMEX","AMFAM","AMICA","AMSTERDAM","ANALYTICS","ANDROID","ANQUAN","ANZ","AO","AOL","APARTMENTS","APP","APPLE","AQ","AQUARELLE","AR","ARAB","ARAMCO","ARCHI","ARMY","ARPA","ART","ARTE","AS","ASDA","ASIA","ASSOCIATES","AT","ATHLETA","ATTORNEY","AU","AUCTION","AUDI","AUDIBLE","AUDIO","AUSPOST","AUTHOR","AUTO","AUTOS","AVIANCA","AW","AWS","AX","AXA","AZ","AZURE","BA","BABY","BAIDU","BANAMEX","BANANAREPUBLIC","BAND","BANK","BAR","BARCELONA","BARCLAYCARD","BARCLAYS","BAREFOOT","BARGAINS","BASEBALL","BASKETBALL","BAUHAUS","BAYERN","BB","BBC","BBT","BBVA","BCG","BCN","BD","BE","BEATS","BEAUTY","BEER","BENTLEY","BERLIN","BEST","BESTBUY","BET","BF","BG","BH","BHARTI","BI","BIBLE","BID","BIKE","BING","BINGO","BIO","BIZ","BJ","BLACK","BLACKFRIDAY","BLOCKBUSTER","BLOG","BLOOMBERG","BLUE","BM","BMS","BMW","BN","BNPPARIBAS","BO","BOATS","BOEHRINGER","BOFA","BOM","BOND","BOO","BOOK","BOOKING","BOSCH","BOSTIK","BOSTON","BOT","BOUTIQUE","BOX","BR","BRADESCO","BRIDGESTONE","BROADWAY","BROKER","BROTHER","BRUSSELS","BS","BT","BUDAPEST","BUGATTI","BUILD","BUILDERS","BUSINESS","BUY","BUZZ","BV","BW","BY","BZ","BZH","CA","CAB","CAFE","CAL","CALL","CALVINKLEIN","CAM","CAMERA","CAMP","CANCERRESEARCH","CANON","CAPETOWN","CAPITAL","CAPITALONE","CAR","CARAVAN","CARDS","CARE","CAREER","CAREERS","CARS","CASA","CASE","CASH","CASINO","CAT","CATERING","CATHOLIC","CBA","CBN","CBRE","CBS","CC","CD","CENTER","CEO","CERN","CF","CFA","CFD","CG","CH","CHANEL","CHANNEL","CHARITY","CHASE","CHAT","CHEAP","CHINTAI","CHRISTMAS","CHROME","CHURCH","CI","CIPRIANI","CIRCLE","CISCO","CITADEL","CITI","CITIC","CITY","CITYEATS","CK","CL","CLAIMS","CLEANING","CLICK","CLINIC","CLINIQUE","CLOTHING","CLOUD","CLUB","CLUBMED","CM","CN","CO","COACH","CODES","COFFEE","COLLEGE","COLOGNE","COM","COMCAST","COMMBANK","COMMUNITY","COMPANY","COMPARE","COMPUTER","COMSEC","CONDOS","CONSTRUCTION","CONSULTING","CONTACT","CONTRACTORS","COOKING","COOKINGCHANNEL","COOL","COOP","CORSICA","COUNTRY","COUPON","COUPONS","COURSES","CPA","CR","CREDIT","CREDITCARD","CREDITUNION","CRICKET","CROWN","CRS","CRUISE","CRUISES","CSC","CU","CUISINELLA","CV","CW","CX","CY","CYMRU","CYOU","CZ","DABUR","DAD","DANCE","DATA","DATE","DATING","DATSUN","DAY","DCLK","DDS","DE","DEAL","DEALER","DEALS","DEGREE","DELIVERY","DELL","DELOITTE","DELTA","DEMOCRAT","DENTAL","DENTIST","DESI","DESIGN","DEV","DHL","DIAMONDS","DIET","DIGITAL","DIRECT","DIRECTORY","DISCOUNT","DISCOVER","DISH","DIY","DJ","DK","DM","DNP","DO","DOCS","DOCTOR","DOG","DOMAINS","DOT","DOWNLOAD","DRIVE","DTV","DUBAI","DUCK","DUNLOP","DUPONT","DURBAN","DVAG","DVR","DZ","EARTH","EAT","EC","ECO","EDEKA","EDU","EDUCATION","EE","EG","EMAIL","EMERCK","ENERGY","ENGINEER","ENGINEERING","ENTERPRISES","EPSON","EQUIPMENT","ER","ERICSSON","ERNI","ES","ESQ","ESTATE","ET","ETISALAT","EU","EUROVISION","EUS","EVENTS","EXCHANGE","EXPERT","EXPOSED","EXPRESS","EXTRASPACE","FAGE","FAIL","FAIRWINDS","FAITH","FAMILY","FAN","FANS","FARM","FARMERS","FASHION","FAST","FEDEX","FEEDBACK","FERRARI","FERRERO","FI","FIAT","FIDELITY","FIDO","FILM","FINAL","FINANCE","FINANCIAL","FIRE","FIRESTONE","FIRMDALE","FISH","FISHING","FIT","FITNESS","FJ","FK","FLICKR","FLIGHTS","FLIR","FLORIST","FLOWERS","FLY","FM","FO","FOO","FOOD","FOODNETWORK","FOOTBALL","FORD","FOREX","FORSALE","FORUM","FOUNDATION","FOX","FR","FREE","FRESENIUS","FRL","FROGANS","FRONTDOOR","FRONTIER","FTR","FUJITSU","FUN","FUND","FURNITURE","FUTBOL","FYI","GA","GAL","GALLERY","GALLO","GALLUP","GAME","GAMES","GAP","GARDEN","GAY","GB","GBIZ","GD","GDN","GE","GEA","GENT","GENTING","GEORGE","GF","GG","GGEE","GH","GI","GIFT","GIFTS","GIVES","GIVING","GL","GLADE","GLASS","GLE","GLOBAL","GLOBO","GM","GMAIL","GMBH","GMO","GMX","GN","GODADDY","GOLD","GOLDPOINT","GOLF","GOO","GOODYEAR","GOOG","GOOGLE","GOP","GOT","GOV","GP","GQ","GR","GRAINGER","GRAPHICS","GRATIS","GREEN","GRIPE","GROCERY","GROUP","GS","GT","GU","GUARDIAN","GUCCI","GUGE","GUIDE","GUITARS","GURU","GW","GY","HAIR","HAMBURG","HANGOUT","HAUS","HBO","HDFC","HDFCBANK","HEALTH","HEALTHCARE","HELP","HELSINKI","HERE","HERMES","HGTV","HIPHOP","HISAMITSU","HITACHI","HIV","HK","HKT","HM","HN","HOCKEY","HOLDINGS","HOLIDAY","HOMEDEPOT","HOMEGOODS","HOMES","HOMESENSE","HONDA","HORSE","HOSPITAL","HOST","HOSTING","HOT","HOTELES","HOTELS","HOTMAIL","HOUSE","HOW","HR","HSBC","HT","HU","HUGHES","HYATT","HYUNDAI","IBM","ICBC","ICE","ICU","ID","IE","IEEE","IFM","IKANO","IL","IM","IMAMAT","IMDB","IMMO","IMMOBILIEN","IN","INC","INDUSTRIES","INFINITI","INFO","ING","INK","INSTITUTE","INSURANCE","INSURE","INT","INTERNATIONAL","INTUIT","INVESTMENTS","IO","IPIRANGA","IQ","IR","IRISH","IS","ISMAILI","IST","ISTANBUL","IT","ITAU","ITV","JAGUAR","JAVA","JCB","JE","JEEP","JETZT","JEWELRY","JIO","JLL","JM","JMP","JNJ","JO","JOBS","JOBURG","JOT","JOY","JP","JPMORGAN","JPRS","JUEGOS","JUNIPER","KAUFEN","KDDI","KE","KERRYHOTELS","KERRYLOGISTICS","KERRYPROPERTIES","KFH","KG","KH","KI","KIA","KIM","KINDER","KINDLE","KITCHEN","KIWI","KM","KN","KOELN","KOMATSU","KOSHER","KP","KPMG","KPN","KR","KRD","KRED","KUOKGROUP","KW","KY","KYOTO","KZ","LA","LACAIXA","LAMBORGHINI","LAMER","LANCASTER","LANCIA","LAND","LANDROVER","LANXESS","LASALLE","LAT","LATINO","LATROBE","LAW","LAWYER","LB","LC","LDS","LEASE","LECLERC","LEFRAK","LEGAL","LEGO","LEXUS","LGBT","LI","LIDL","LIFE","LIFEINSURANCE","LIFESTYLE","LIGHTING","LIKE","LILLY","LIMITED","LIMO","LINCOLN","LINDE","LINK","LIPSY","LIVE","LIVING","LIXIL","LK","LLC","LLP","LOAN","LOANS","LOCKER","LOCUS","LOFT","LOL","LONDON","LOTTE","LOTTO","LOVE","LPL","LPLFINANCIAL","LR","LS","LT","LTD","LTDA","LU","LUNDBECK","LUXE","LUXURY","LV","LY","MA","MACYS","MADRID","MAIF","MAISON","MAKEUP","MAN","MANAGEMENT","MANGO","MAP","MARKET","MARKETING","MARKETS","MARRIOTT","MARSHALLS","MASERATI","MATTEL","MBA","MC","MCKINSEY","MD","ME","MED","MEDIA","MEET","MELBOURNE","MEME","MEMORIAL","MEN","MENU","MERCKMSD","MG","MH","MIAMI","MICROSOFT","MIL","MINI","MINT","MIT","MITSUBISHI","MK","ML","MLB","MLS","MM","MMA","MN","MO","MOBI","MOBILE","MODA","MOE","MOI","MOM","MONASH","MONEY","MONSTER","MORMON","MORTGAGE","MOSCOW","MOTO","MOTORCYCLES","MOV","MOVIE","MP","MQ","MR","MS","MSD","MT","MTN","MTR","MU","MUSEUM","MUTUAL","MV","MW","MX","MY","MZ","NA","NAB","NAGOYA","NAME","NATURA","NAVY","NBA","NC","NE","NEC","NET","NETBANK","NETFLIX","NETWORK","NEUSTAR","NEW","NEWS","NEXT","NEXTDIRECT","NEXUS","NF","NFL","NG","NGO","NHK","NI","NICO","NIKE","NIKON","NINJA","NISSAN","NISSAY","NL","NO","NOKIA","NORTHWESTERNMUTUAL","NORTON","NOW","NOWRUZ","NOWTV","NP","NR","NRA","NRW","NTT","NU","NYC","NZ","OBI","OBSERVER","OFF","OFFICE","OKINAWA","OLAYAN","OLAYANGROUP","OLDNAVY","OLLO","OM","OMEGA","ONE","ONG","ONL","ONLINE","OOO","OPEN","ORACLE","ORANGE","ORG","ORGANIC","ORIGINS","OSAKA","OTSUKA","OTT","OVH","PA","PAGE","PANASONIC","PARIS","PARS","PARTNERS","PARTS","PARTY","PASSAGENS","PAY","PCCW","PE","PET","PF","PFIZER","PG","PH","PHARMACY","PHD","PHILIPS","PHONE","PHOTO","PHOTOGRAPHY","PHOTOS","PHYSIO","PICS","PICTET","PICTURES","PID","PIN","PING","PINK","PIONEER","PIZZA","PK","PL","PLACE","PLAY","PLAYSTATION","PLUMBING","PLUS","PM","PN","PNC","POHL","POKER","POLITIE","PORN","POST","PR","PRAMERICA","PRAXI","PRESS","PRIME","PRO","PROD","PRODUCTIONS","PROF","PROGRESSIVE","PROMO","PROPERTIES","PROPERTY","PROTECTION","PRU","PRUDENTIAL","PS","PT","PUB","PW","PWC","PY","QA","QPON","QUEBEC","QUEST","QVC","RACING","RADIO","RAID","RE","READ","REALESTATE","REALTOR","REALTY","RECIPES","RED","REDSTONE","REDUMBRELLA","REHAB","REISE","REISEN","REIT","RELIANCE","REN","RENT","RENTALS","REPAIR","REPORT","REPUBLICAN","REST","RESTAURANT","REVIEW","REVIEWS","REXROTH","RICH","RICHARDLI","RICOH","RIL","RIO","RIP","RMIT","RO","ROCHER","ROCKS","RODEO","ROGERS","ROOM","RS","RSVP","RU","RUGBY","RUHR","RUN","RW","RWE","RYUKYU","SA","SAARLAND","SAFE","SAFETY","SAKURA","SALE","SALON","SAMSCLUB","SAMSUNG","SANDVIK","SANDVIKCOROMANT","SANOFI","SAP","SARL","SAS","SAVE","SAXO","SB","SBI","SBS","SC","SCA","SCB","SCHAEFFLER","SCHMIDT","SCHOLARSHIPS","SCHOOL","SCHULE","SCHWARZ","SCIENCE","SCJOHNSON","SCOT","SD","SE","SEARCH","SEAT","SECURE","SECURITY","SEEK","SENER","SERVICES","SES","SEVEN","SEW","SEX","SEXY","SFR","SG","SH","SHANGRILA","SHARP","SHAW","SHELL","SHIA","SHIKSHA","SHOES","SHOP","SHOPPING","SHOUJI","SHOW","SHOWTIME","SI","SILK","SINA","SINGLES","SITE","SJ","SK","SKI","SKIN","SKY","SKYPE","SL","SLING","SM","SMART","SMILE","SN","SNCF","SO","SOCCER","SOCIAL","SOFTBANK","SOFTWARE","SOHU","SOLAR","SOLUTIONS","SONG","SONY","SOY","SPA","SPACE","SPORT","SPOT","SR","SRL","SS","ST","STADA","STAPLES","STAR","STATEBANK","STATEFARM","STC","STCGROUP","STOCKHOLM","STORAGE","STORE","STREAM","STUDIO","STUDY","STYLE","SU","SUCKS","SUPPLIES","SUPPLY","SUPPORT","SURF","SURGERY","SUZUKI","SV","SWATCH","SWIFTCOVER","SWISS","SX","SY","SYDNEY","SYSTEMS","SZ","TAB","TAIPEI","TALK","TAOBAO","TARGET","TATAMOTORS","TATAR","TATTOO","TAX","TAXI","TC","TCI","TD","TDK","TEAM","TECH","TECHNOLOGY","TEL","TEMASEK","TENNIS","TEVA","TF","TG","TH","THD","THEATER","THEATRE","TIAA","TICKETS","TIENDA","TIFFANY","TIPS","TIRES","TIROL","TJ","TJMAXX","TJX","TK","TKMAXX","TL","TM","TMALL","TN","TO","TODAY","TOKYO","TOOLS","TOP","TORAY","TOSHIBA","TOTAL","TOURS","TOWN","TOYOTA","TOYS","TR","TRADE","TRADING","TRAINING","TRAVEL","TRAVELCHANNEL","TRAVELERS","TRAVELERSINSURANCE","TRUST","TRV","TT","TUBE","TUI","TUNES","TUSHU","TV","TVS","TW","TZ","UA","UBANK","UBS","UG","UK","UNICOM","UNIVERSITY","UNO","UOL","UPS","US","UY","UZ","VA","VACATIONS","VANA","VANGUARD","VC","VE","VEGAS","VENTURES","VERISIGN","VERSICHERUNG","VET","VG","VI","VIAJES","VIDEO","VIG","VIKING","VILLAS","VIN","VIP","VIRGIN","VISA","VISION","VIVA","VIVO","VLAANDEREN","VN","VODKA","VOLKSWAGEN","VOLVO","VOTE","VOTING","VOTO","VOYAGE","VU","VUELOS","WALES","WALMART","WALTER","WANG","WANGGOU","WATCH","WATCHES","WEATHER","WEATHERCHANNEL","WEBCAM","WEBER","WEBSITE","WED","WEDDING","WEIBO","WEIR","WF","WHOSWHO","WIEN","WIKI","WILLIAMHILL","WIN","WINDOWS","WINE","WINNERS","WME","WOLTERSKLUWER","WOODSIDE","WORK","WORKS","WORLD","WOW","WS","WTC","WTF","XBOX","XEROX","XFINITY","XIHUAN","XIN","XN--11B4C3D","XN--1CK2E1B","XN--1QQW23A","XN--2SCRJ9C","XN--30RR7Y","XN--3BST00M","XN--3DS443G","XN--3E0B707E","XN--3HCRJ9C","XN--3OQ18VL8PN36A","XN--3PXU8K","XN--42C2D9A","XN--45BR5CYL","XN--45BRJ9C","XN--45Q11C","XN--4DBRK0CE","XN--4GBRIM","XN--54B7FTA0CC","XN--55QW42G","XN--55QX5D","XN--5SU34J936BGSG","XN--5TZM5G","XN--6FRZ82G","XN--6QQ986B3XL","XN--80ADXHKS","XN--80AO21A","XN--80AQECDR1A","XN--80ASEHDB","XN--80ASWG","XN--8Y0A063A","XN--90A3AC","XN--90AE","XN--90AIS","XN--9DBQ2A","XN--9ET52U","XN--9KRT00A","XN--B4W605FERD","XN--BCK1B9A5DRE4C","XN--C1AVG","XN--C2BR7G","XN--CCK2B3B","XN--CCKWCXETD","XN--CG4BKI","XN--CLCHC0EA0B2G2A9GCD","XN--CZR694B","XN--CZRS0T","XN--CZRU2D","XN--D1ACJ3B","XN--D1ALF","XN--E1A4C","XN--ECKVDTC9D","XN--EFVY88H","XN--FCT429K","XN--FHBEI","XN--FIQ228C5HS","XN--FIQ64B","XN--FIQS8S","XN--FIQZ9S","XN--FJQ720A","XN--FLW351E","XN--FPCRJ9C3D","XN--FZC2C9E2C","XN--FZYS8D69UVGM","XN--G2XX48C","XN--GCKR3F0F","XN--GECRJ9C","XN--GK3AT1E","XN--H2BREG3EVE","XN--H2BRJ9C","XN--H2BRJ9C8C","XN--HXT814E","XN--I1B6B1A6A2E","XN--IMR513N","XN--IO0A7I","XN--J1AEF","XN--J1AMH","XN--J6W193G","XN--JLQ480N2RG","XN--JLQ61U9W7B","XN--JVR189M","XN--KCRX77D1X4A","XN--KPRW13D","XN--KPRY57D","XN--KPUT3I","XN--L1ACC","XN--LGBBAT1AD8J","XN--MGB9AWBF","XN--MGBA3A3EJT","XN--MGBA3A4F16A","XN--MGBA7C0BBN0A","XN--MGBAAKC7DVF","XN--MGBAAM7A8H","XN--MGBAB2BD","XN--MGBAH1A3HJKRD","XN--MGBAI9AZGQP6J","XN--MGBAYH7GPA","XN--MGBBH1A","XN--MGBBH1A71E","XN--MGBC0A9AZCG","XN--MGBCA7DZDO","XN--MGBCPQ6GPA1A","XN--MGBERP4A5D4AR","XN--MGBGU82A","XN--MGBI4ECEXP","XN--MGBPL2FH","XN--MGBT3DHD","XN--MGBTX2B","XN--MGBX4CD0AB","XN--MIX891F","XN--MK1BU44C","XN--MXTQ1M","XN--NGBC5AZD","XN--NGBE9E0A","XN--NGBRX","XN--NODE","XN--NQV7F","XN--NQV7FS00EMA","XN--NYQY26A","XN--O3CW4H","XN--OGBPF8FL","XN--OTU796D","XN--P1ACF","XN--P1AI","XN--PGBS0DH","XN--PSSY2U","XN--Q7CE6A","XN--Q9JYB4C","XN--QCKA1PMC","XN--QXA6A","XN--QXAM","XN--RHQV96G","XN--ROVU88B","XN--RVC1E0AM3E","XN--S9BRJ9C","XN--SES554G","XN--T60B56A","XN--TCKWE","XN--TIQ49XQYJ","XN--UNUP4Y","XN--VERMGENSBERATER-CTB","XN--VERMGENSBERATUNG-PWB","XN--VHQUV","XN--VUQ861B","XN--W4R85EL8FHU5DNRA","XN--W4RS40L","XN--WGBH1C","XN--WGBL6A","XN--XHQ521B","XN--XKC2AL3HYE2A","XN--XKC2DL3A5EE0H","XN--Y9A3AQ","XN--YFRO4I67O","XN--YGBI2AMMX","XN--ZFR164B","XXX","XYZ","YACHTS","YAHOO","YAMAXUN","YANDEX","YE","YODOBASHI","YOGA","YOKOHAMA","YOU","YOUTUBE","YT","YUN","ZA","ZAPPOS","ZARA","ZERO","ZIP","ZM","ZONE","ZUERICH","ZW" , "aaa","aarp","abarth","abb","abbott","abbvie","abc","able","abogado","abudhabi","ac","academy","accenture","accountant","accountants","aco","actor","ad","adac","ads","adult","ae","aeg","aero","aetna","af","afamilycompany","afl","africa","ag","agakhan","agency","ai","aig","airbus","airforce","airtel","akdn","al","alfaromeo","alibaba","alipay","allfinanz","allstate","ally","alsace","alstom","am","amazon","americanexpress","americanfamily","amex","amfam","amica","amsterdam","analytics","android","anquan","anz","ao","aol","apartments","app","apple","aq","aquarelle","ar","arab","aramco","archi","army","arpa","art","arte","as","asda","asia","associates","at","athleta","attorney","au","auction","audi","audible","audio","auspost","author","auto","autos","avianca","aw","aws","ax","axa","az","azure","ba","baby","baidu","banamex","bananarepublic","band","bank","bar","barcelona","barclaycard","barclays","barefoot","bargains","baseball","basketball","bauhaus","bayern","bb","bbc","bbt","bbva","bcg","bcn","bd","be","beats","beauty","beer","bentley","berlin","best","bestbuy","bet","bf","bg","bh","bharti","bi","bible","bid","bike","bing","bingo","bio","biz","bj","black","blackfriday","blockbuster","blog","bloomberg","blue","bm","bms","bmw","bn","bnpparibas","bo","boats","boehringer","bofa","bom","bond","boo","book","booking","bosch","bostik","boston","bot","boutique","box","br","bradesco","bridgestone","broadway","broker","brother","brussels","bs","bt","budapest","bugatti","build","builders","business","buy","buzz","bv","bw","by","bz","bzh","ca","cab","cafe","cal","call","calvinklein","cam","camera","camp","cancerresearch","canon","capetown","capital","capitalone","car","caravan","cards","care","career","careers","cars","casa","case","cash","casino","cat","catering","catholic","cba","cbn","cbre","cbs","cc","cd","center","ceo","cern","cf","cfa","cfd","cg","ch","chanel","channel","charity","chase","chat","cheap","chintai","christmas","chrome","church","ci","cipriani","circle","cisco","citadel","citi","citic","city","cityeats","ck","cl","claims","cleaning","click","clinic","clinique","clothing","cloud","club","clubmed","cm","cn","co","coach","codes","coffee","college","cologne","com","comcast","commbank","community","company","compare","computer","comsec","condos","construction","consulting","contact","contractors","cooking","cookingchannel","cool","coop","corsica","country","coupon","coupons","courses","cpa","cr","credit","creditcard","creditunion","cricket","crown","crs","cruise","cruises","csc","cu","cuisinella","cv","cw","cx","cy","cymru","cyou","cz","dabur","dad","dance","data","date","dating","datsun","day","dclk","dds","de","deal","dealer","deals","degree","delivery","dell","deloitte","delta","democrat","dental","dentist","desi","design","dev","dhl","diamonds","diet","digital","direct","directory","discount","discover","dish","diy","dj","dk","dm","dnp","do","docs","doctor","dog","domains","dot","download","drive","dtv","dubai","duck","dunlop","dupont","durban","dvag","dvr","dz","earth","eat","ec","eco","edeka","edu","education","ee","eg","email","emerck","energy","engineer","engineering","enterprises","epson","equipment","er","ericsson","erni","es","esq","estate","et","etisalat","eu","eurovision","eus","events","exchange","expert","exposed","express","extraspace","fage","fail","fairwinds","faith","family","fan","fans","farm","farmers","fashion","fast","fedex","feedback","ferrari","ferrero","fi","fiat","fidelity","fido","film","final","finance","financial","fire","firestone","firmdale","fish","fishing","fit","fitness","fj","fk","flickr","flights","flir","florist","flowers","fly","fm","fo","foo","food","foodnetwork","football","ford","forex","forsale","forum","foundation","fox","fr","free","fresenius","frl","frogans","frontdoor","frontier","ftr","fujitsu","fun","fund","furniture","futbol","fyi","ga","gal","gallery","gallo","gallup","game","games","gap","garden","gay","gb","gbiz","gd","gdn","ge","gea","gent","genting","george","gf","gg","ggee","gh","gi","gift","gifts","gives","giving","gl","glade","glass","gle","global","globo","gm","gmail","gmbh","gmo","gmx","gn","godaddy","gold","goldpoint","golf","goo","goodyear","goog","google","gop","got","gov","gp","gq","gr","grainger","graphics","gratis","green","gripe","grocery","group","gs","gt","gu","guardian","gucci","guge","guide","guitars","guru","gw","gy","hair","hamburg","hangout","haus","hbo","hdfc","hdfcbank","health","healthcare","help","helsinki","here","hermes","hgtv","hiphop","hisamitsu","hitachi","hiv","hk","hkt","hm","hn","hockey","holdings","holiday","homedepot","homegoods","homes","homesense","honda","horse","hospital","host","hosting","hot","hoteles","hotels","hotmail","house","how","hr","hsbc","ht","hu","hughes","hyatt","hyundai","ibm","icbc","ice","icu","id","ie","ieee","ifm","ikano","il","im","imamat","imdb","immo","immobilien","in","inc","industries","infiniti","info","ing","ink","institute","insurance","insure","int","international","intuit","investments","io","ipiranga","iq","ir","irish","is","ismaili","ist","istanbul","it","itau","itv","jaguar","java","jcb","je","jeep","jetzt","jewelry","jio","jll","jm","jmp","jnj","jo","jobs","joburg","jot","joy","jp","jpmorgan","jprs","juegos","juniper","kaufen","kddi","ke","kerryhotels","kerrylogistics","kerryproperties","kfh","kg","kh","ki","kia","kim","kinder","kindle","kitchen","kiwi","km","kn","koeln","komatsu","kosher","kp","kpmg","kpn","kr","krd","kred","kuokgroup","kw","ky","kyoto","kz","la","lacaixa","lamborghini","lamer","lancaster","lancia","land","landrover","lanxess","lasalle","lat","latino","latrobe","law","lawyer","lb","lc","lds","lease","leclerc","lefrak","legal","lego","lexus","lgbt","li","lidl","life","lifeinsurance","lifestyle","lighting","like","lilly","limited","limo","lincoln","linde","link","lipsy","live","living","lixil","lk","llc","llp","loan","loans","locker","locus","loft","lol","london","lotte","lotto","love","lpl","lplfinancial","lr","ls","lt","ltd","ltda","lu","lundbeck","luxe","luxury","lv","ly","ma","macys","madrid","maif","maison","makeup","man","management","mango","map","market","marketing","markets","marriott","marshalls","maserati","mattel","mba","mc","mckinsey","md","me","med","media","meet","melbourne","meme","memorial","men","menu","merckmsd","mg","mh","miami","microsoft","mil","mini","mint","mit","mitsubishi","mk","ml","mlb","mls","mm","mma","mn","mo","mobi","mobile","moda","moe","moi","mom","monash","money","monster","mormon","mortgage","moscow","moto","motorcycles","mov","movie","mp","mq","mr","ms","msd","mt","mtn","mtr","mu","museum","mutual","mv","mw","mx","my","mz","na","nab","nagoya","name","natura","navy","nba","nc","ne","nec","net","netbank","netflix","network","neustar","new","news","next","nextdirect","nexus","nf","nfl","ng","ngo","nhk","ni","nico","nike","nikon","ninja","nissan","nissay","nl","no","nokia","northwesternmutual","norton","now","nowruz","nowtv","np","nr","nra","nrw","ntt","nu","nyc","nz","obi","observer","off","office","okinawa","olayan","olayangroup","oldnavy","ollo","om","omega","one","ong","onl","online","ooo","open","oracle","orange","org","organic","origins","osaka","otsuka","ott","ovh","pa","page","panasonic","paris","pars","partners","parts","party","passagens","pay","pccw","pe","pet","pf","pfizer","pg","ph","pharmacy","phd","philips","phone","photo","photography","photos","physio","pics","pictet","pictures","pid","pin","ping","pink","pioneer","pizza","pk","pl","place","play","playstation","plumbing","plus","pm","pn","pnc","pohl","poker","politie","porn","post","pr","pramerica","praxi","press","prime","pro","prod","productions","prof","progressive","promo","properties","property","protection","pru","prudential","ps","pt","pub","pw","pwc","py","qa","qpon","quebec","quest","qvc","racing","radio","raid","re","read","realestate","realtor","realty","recipes","red","redstone","redumbrella","rehab","reise","reisen","reit","reliance","ren","rent","rentals","repair","report","republican","rest","restaurant","review","reviews","rexroth","rich","richardli","ricoh","ril","rio","rip","rmit","ro","rocher","rocks","rodeo","rogers","room","rs","rsvp","ru","rugby","ruhr","run","rw","rwe","ryukyu","sa","saarland","safe","safety","sakura","sale","salon","samsclub","samsung","sandvik","sandvikcoromant","sanofi","sap","sarl","sas","save","saxo","sb","sbi","sbs","sc","sca","scb","schaeffler","schmidt","scholarships","school","schule","schwarz","science","scjohnson","scot","sd","se","search","seat","secure","security","seek","select","sener","services","ses","seven","sew","sex","sexy","sfr","sg","sh","shangrila","sharp","shaw","shell","shia","shiksha","shoes","shop","shopping","shouji","show","showtime","si","silk","sina","singles","site","sj","sk","ski","skin","sky","skype","sl","sling","sm","smart","smile","sn","sncf","so","soccer","social","softbank","software","sohu","solar","solutions","song","sony","soy","spa","space","sport","spot","sr","srl","ss","st","stada","staples","star","statebank","statefarm","stc","stcgroup","stockholm","storage","store","stream","studio","study","style","su","sucks","supplies","supply","support","surf","surgery","suzuki","sv","swatch","swiftcover","swiss","sx","sy","sydney","systems","sz","tab","taipei","talk","taobao","target","tatamotors","tatar","tattoo","tax","taxi","tc","tci","td","tdk","team","tech","technology","tel","temasek","tennis","teva","tf","tg","th","thd","theater","theatre","tiaa","tickets","tienda","tiffany","tips","tires","tirol","tj","tjmaxx","tjx","tk","tkmaxx","tl","tm","tmall","tn","to","today","tokyo","tools","top","toray","toshiba","total","tours","town","toyota","toys","tr","trade","trading","training","travel","travelchannel","travelers","travelersinsurance","trust","trv","tt","tube","tui","tunes","tushu","tv","tvs","tw","tz","ua","ubank","ubs","ug","uk","unicom","university","uno","uol","ups","us","uy","uz","va","vacations","vana","vanguard","vc","ve","vegas","ventures","verisign","versicherung","vet","vg","vi","viajes","video","vig","viking","villas","vin","vip","virgin","visa","vision","viva","vivo","vlaanderen","vn","vodka","volkswagen","volvo","vote","voting","voto","voyage","vu","vuelos","wales","walmart","walter","wang","wanggou","watch","watches","weather","weatherchannel","webcam","weber","website","wed","wedding","weibo","weir","wf","whoswho","wien","wiki","williamhill","win","windows","wine","winners","wme","wolterskluwer","woodside","work","works","world","wow","ws","wtc","wtf","xbox","xerox","xfinity","xihuan","xin","xn--11b4c3d","xn--1ck2e1b","xn--1qqw23a","xn--2scrj9c","xn--30rr7y","xn--3bst00m","xn--3ds443g","xn--3e0b707e","xn--3hcrj9c","xn--3oq18vl8pn36a","xn--3pxu8k","xn--42c2d9a","xn--45br5cyl","xn--45brj9c","xn--45q11c","xn--4dbrk0ce","xn--4gbrim","xn--54b7fta0cc","xn--55qw42g","xn--55qx5d","xn--5su34j936bgsg","xn--5tzm5g","xn--6frz82g","xn--6qq986b3xl","xn--80adxhks","xn--80ao21a","xn--80aqecdr1a","xn--80asehdb","xn--80aswg","xn--8y0a063a","xn--90a3ac","xn--90ae","xn--90ais","xn--9dbq2a","xn--9et52u","xn--9krt00a","xn--b4w605ferd","xn--bck1b9a5dre4c","xn--c1avg","xn--c2br7g","xn--cck2b3b","xn--cckwcxetd","xn--cg4bki","xn--clchc0ea0b2g2a9gcd","xn--czr694b","xn--czrs0t","xn--czru2d","xn--d1acj3b","xn--d1alf","xn--e1a4c","xn--eckvdtc9d","xn--efvy88h","xn--fct429k","xn--fhbei","xn--fiq228c5hs","xn--fiq64b","xn--fiqs8s","xn--fiqz9s","xn--fjq720a","xn--flw351e","xn--fpcrj9c3d","xn--fzc2c9e2c","xn--fzys8d69uvgm","xn--g2xx48c","xn--gckr3f0f","xn--gecrj9c","xn--gk3at1e","xn--h2breg3eve","xn--h2brj9c","xn--h2brj9c8c","xn--hxt814e","xn--i1b6b1a6a2e","xn--imr513n","xn--io0a7i","xn--j1aef","xn--j1amh","xn--j6w193g","xn--jlq480n2rg","xn--jlq61u9w7b","xn--jvr189m","xn--kcrx77d1x4a","xn--kprw13d","xn--kpry57d","xn--kput3i","xn--l1acc","xn--lgbbat1ad8j","xn--mgb9awbf","xn--mgba3a3ejt","xn--mgba3a4f16a","xn--mgba7c0bbn0a","xn--mgbaakc7dvf","xn--mgbaam7a8h","xn--mgbab2bd","xn--mgbah1a3hjkrd","xn--mgbai9azgqp6j","xn--mgbayh7gpa","xn--mgbbh1a","xn--mgbbh1a71e","xn--mgbc0a9azcg","xn--mgbca7dzdo","xn--mgbcpq6gpa1a","xn--mgberp4a5d4ar","xn--mgbgu82a","xn--mgbi4ecexp","xn--mgbpl2fh","xn--mgbt3dhd","xn--mgbtx2b","xn--mgbx4cd0ab","xn--mix891f","xn--mk1bu44c","xn--mxtq1m","xn--ngbc5azd","xn--ngbe9e0a","xn--ngbrx","xn--node","xn--nqv7f","xn--nqv7fs00ema","xn--nyqy26a","xn--o3cw4h","xn--ogbpf8fl","xn--otu796d","xn--p1acf","xn--p1ai","xn--pgbs0dh","xn--pssy2u","xn--q7ce6a","xn--q9jyb4c","xn--qcka1pmc","xn--qxa6a","xn--qxam","xn--rhqv96g","xn--rovu88b","xn--rvc1e0am3e","xn--s9brj9c","xn--ses554g","xn--t60b56a","xn--tckwe","xn--tiq49xqyj","xn--unup4y","xn--vermgensberater-ctb","xn--vermgensberatung-pwb","xn--vhquv","xn--vuq861b","xn--w4r85el8fhu5dnra","xn--w4rs40l","xn--wgbh1c","xn--wgbl6a","xn--xhq521b","xn--xkc2al3hye2a","xn--xkc2dl3a5ee0h","xn--y9a3aq","xn--yfro4i67o","xn--ygbi2ammx","xn--zfr164b","xxx","xyz","yachts","yahoo","yamaxun","yandex","ye","yodobashi","yoga","yokohama","you","youtube","yt","yun","za","zappos","zara","zero","zip","zm","zone","zuerich","zw"] 
            
            
            
            
        
            for tld in Tld :
    
                if "." in Target :
                    info = socket.gethostbyname_ex(Target)
                    for infor in info :
                        if (infor == []) :
                            quit
                        else :
                            print(infor)
                    exit()
                    
                else :
                    Tldd = str(input("Enter TLD Site ==>> "))
                    Target = str(input("Enter Name site ==>> "))
                    Last_Target = Target + "." + Tldd
                    
                    for t in Tld :
                        if t in Tldd :
                            print(Last_Target)
                            Last_Check = str(input("Are you shore y/n ==>> "))
                            if (Last_Check == "y") :
                                infor = socket.gethostbyname_ex(Last_Target)
                                for inf in infor :
                                    
                                    if (inf == []) : 
                                        quit
                                    elif (inf == [""]) :
                                        print(inf[0])
                                    else :
                                        print(inf)
                            
                            else :
                                print("error")
                            break
                    exit()
          
                    
        elif (ValId == 3) :
            print("1.Sql Injection")
            print("2.Normal Search")
            IdSelect = int(input("Choese Please ==>> "))
            if (IdSelect == 1) :
                
                DorkTar = str(input("Inter Your Target or Name Something ==>> "))
                googleDork = "inurl : "
                TargetDork = googleDork + DorkTar
                DorkResult = search(TargetDork)
                File = open("SiteForSqlInjection.txt" , "a")
                for site in DorkResult :
                    File.write("Target's Name : " + site)
                    File.write("\n")
                File.close()
                        
            elif (IdSelect == 2) :
                
                DorkTar = str(input("Inter Your Target or Name Something ==>> "))
                googleDork = ["site :" , "inurl :" , "intitle :" , "intext :" , "define :" , "site :" , "phonebook :" , "maps" , "book" , "info :" , "movie :" , "weather : " , "related :" , "link :"]
                
                for dork in googleDork :
                    DorkCreate = DorkTar + dork
                    DorkResult = search(DorkCreate)
                    for Cdork in DorkResult :
                        print(Cdork)
        
        else :
            print("Main Error")
            
 
Site()
         
