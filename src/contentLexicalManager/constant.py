
DB_CONFIG = {
    "HOST": "localhost",
    "user": "root",
    "password": "root",
    "database": "world",
    "auth_plugin": "mysql_native_password"
}

CONSTANT_FC1_CONTAINING_DIGITS = "FC1_ContainDigits"
CONSTANT_FC2_WORD_SEGEMENTS = "FC2_SegWordNum"
CONSTANT_FC3_URL_FRACTION = "FC3_UrlFraction"
CONSTANT_FC6_HASHTAG_CLARITY = "FC6_HashTagClarity"
CONSTANT_FC7_TWEET_CLARITY = "FC7_TweetClarityPercentage"

CONSTANT_FX1 = "FX1_TotalUserCount"
CONSTANT_FX2_TOTAL_TWEET_COUNT = "FX2_TotalTweetCount"
CONSTANT_FX3_REPLY_FRAC_VAL = "FX3_ReplyFractionValue"
CONSTANT_FX4_RTWT_FRAC_VAL = "FX4_ReTweetFractionValue"
CONSTANT_FX5_USR_AUTH = "FX5_UserAuthority"

CONSTANT_TOTAL_MENTIONED_USERS = "totalMentionedUsers"
CONSTANT_TOTAL_UNIQUE_URLS = "totalUniqueURLs" 
CONSTANT_TOTAL_TWEET_COUNTS = "FX2_TotalTweetCount"


CONSTANT_FILE_NAME = "contentTweetInfo.json"

CONSTANT_FILE_WRITE_PERMISSION = "w"
CONSTANT_FILE_READ_PERMISSION = "w"
CONSTANT_FILE_EXTENSION_TYPE = ".json"

CONSTANT_FILE_NAME_EXCLUDE = "usersBasedOnHashTag.json"

CONSTANT_MAIN_HOOK = '__main__'
CONSTANT_BOOL_TRUE = True
CONSTANT_BOOL_FALSE = False

CONSTANT_QUERY_TOP_TRENDING_HASHTAGS = "SELECT hashtag, COUNT(hashtag) FROM world.tweet_dataset GROUP BY hashtag ORDER BY COUNT(hashtag) DESC LIMIT 5;"

CONSTANT_QUERY_HASHTAG_BASED_TWEETS = "SELECT w from world.tweet_dataset WHERE hashtag LIKE '%"  

CONSTANT_QUERY_HASHTAG_WITH_COUNTS = "SELECT hashtag, COUNT(hashtag) FROM world.tweet_dataset GROUP BY hashtag ORDER BY COUNT(hashtag) DESC LIMIT 5;"
CONSTANT_QUERY_GET_ALL_HASHTAGS = "SELECT hashtag from world.tweet_dataset WHERE hashtag is not null;" 

CONSTANT_FX1_QUERY_PART_1 = "SELECT count(*) FROM world.tweet_dataset WHERE hashtag LIKE '%"
CONSTANT_FX1_QUERY_PART_2 =  "%' AND mention IS NOT null;"

CONSTANT_COLLECT_LOCAL_INFO_STORE_LOCAL_PART1 = "SELECT COUNT(*) FROM world.tweet_dataset WHERE w LIKE '%@"
CONSTANT_COLLECT_LOCAL_INFO_STORE_LOCAL_PART2 = "%';"

CONSTANT_MENTIONED_USER_QUERY_PART1 = "SELECT distinct(mention) FROM world.tweet_dataset WHERE hashtag LIKE '%" 
CONSTANT_MENTIONED_USER_QUERY_PART2 =  "%';"

CONSTANT_RT_COUNT_QUERY_PART1 = "SELECT w FROM world.tweet_dataset WHERE hashtag LIKE '%" 
CONSTANT_RT_COUNT_QUERY_PART2 = "%';"   

CONSTANT_FX3_QUERY_PART1 = "SELECT mention, COUNT(mention) FROM world.tweet_dataset WHERE hashtag LIKE '%"
CONSTANT_FX3_QUERY_PART2 =  "%' AND mention IS NOT NULL GROUP BY mention HAVING COUNT(mention) > 1 ;"

CONSTANT_KEYWORD_HASHTAG = "#"
CONSTANT_KEYWORD_AT_RATE = "@"
CONSTANT_KEYWORD_HTTP = "http"

CONSTANT_INPUT_VALIDATION_ERROR = "Input does not contain any elements/value in it. Please verify at the callable location!"
CONSTANT_EXCEPTION_ERROR = "Something went wrong, Please check the Error e"

CONSTANT_HASHTAG_CLARITY_VALUE = 0.25
CONSTANT_DEFAULT_VALUE = 0

CONSTANT_RE_CHECK_STRING_HAS_URL = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
CONSTANT_RE_0_9_VALIDATION = '^[0-9]*$'


