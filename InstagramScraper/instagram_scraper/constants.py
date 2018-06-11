# coding: utf-8
BASE_URL = 'https://www.instagram.com/'
LOGIN_URL = BASE_URL + 'accounts/login/ajax/'
LOGOUT_URL = BASE_URL + 'accounts/logout/'
CHROME_WIN_UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
USER_URL = BASE_URL + '{0}/?__a=1'

STORIES_URL = 'https://i.instagram.com/api/v1/feed/user/{0}/story/'
STORIES_UA = 'Instagram 9.5.2 (iPhone7,2; iPhone OS 9_3_3; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/420+'
STORIES_COOKIE = 'ds_user_id={0}; sessionid={1};'

TAGS_URL = BASE_URL + 'explore/tags/{0}/?__a=1'
LOCATIONS_URL = BASE_URL + 'explore/locations/{0}/?__a=1'
VIEW_MEDIA_URL = BASE_URL + 'p/{0}/?__a=1'
SEARCH_URL = BASE_URL + 'web/search/topsearch/?context=blended&query={0}'

QUERY_COMMENTS = BASE_URL + 'graphql/query/?query_id=17852405266163336&shortcode={0}&first=100&after={1}'
QUERY_HASHTAG = BASE_URL + 'graphql/query/?query_id=17882293912014529&tag_name={0}&first=100&after={1}'
QUERY_LOCATION = BASE_URL + 'graphql/query/?query_id=17881432870018455&id={0}&first=100&after={1}'
QUERY_MEDIA = BASE_URL + 'graphql/query/?query_id=17888483320059182&id={0}&first=100&after={1}'



FILE_EXTENSION = '.json'
DIRECTORYPATH = './'
LikeToKnowItUserList =['cocorocha', 'blaireadiebee', 'hellofashionblog','hapatime', 'lolariostyle', 'cmcoving', 'kaitlynn_carter', 'emmahill', 'kathleen_barnes', 'doina', 'champagneandchanel', 'shortstoriesandskirts', 'lyndiinthecity', 'cellajaneblog', 'jessi_afshin', 'hauteofftherack', 'apinchoflovely', 'holliewdwrd', 'stephsterjovski', 'laurenkaysims', 'samanthabelbel', 'littleblondebook', 'thehouseofsequins', 'oliviarink','themilleraffect','joellefriend','jordanunderwood','kenzasmg','katiesbliss','jaimeshrayber','daphnemodeandthecity','ruerodier','thestylebungalow','babiolesdezoe','sorayabakhtiar','jessannkirby','n_g_le','chicflavours','hellovalentine','the_beauty_issue','themoptop','karazwaanstra','jdfashionfreak','interiordesignerella', 'thedoubletakegirls','jessicawhitaker','polishedavenue','modern.mrs']
SwedishUserList = ['thessan.se','zaralarsson','amandafranzeen','hannamw','johannasjoo','lisa.olssons','kenzas','angelicablick','jannid','thereselindgren','victoriatornegren','biancaingrosso','linnahlborg','emmahill','sagascott','josephineqvist','isabellajedler','emmabuggo','rebeccaeden','monikawolff','nicolinehedlund','jackieferm','amandafranzeen','emmy.winther','lazoey','nellielindgren','idakrensler','thereseklockare','platins.se']
DATABASE = ''
USERLISTCOLLECTION = ''
LIKETOKNOWIT = ''
SWEDISHUSER = ''
NOJSON_DIR = '/home/ummul/FinalDatabaseData/nojson'
#usernameidtable
#liketoknowituser
#swedishuser
