
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

CONSTANT_FX1 = ""
CONSTANT_FX2_TOTAL_TWEET_COUNT = "FX2_TotalTweetCount"

CONSTANT_TOTAL_MENTIONED_USERS = "totalMentionedUsers"
CONSTANT_TOTAL_UNIQUE_URLS = "totalUniqueURLs" 
CONSTANT_TOTAL_TWEET_COUNTS = "FX2_TotalTweetCount"


CONSTANT_FILE_NAME = "contentTweetInfo.json"

CONSTANT_FILE_WRITE_PERMISSION = "w"

CONSTANT_MAIN_HOOK = '__main__'
CONSTANT_SEGEMENT_WORD_PHRASE = 'Segement Word Plots'
CONSTANT_SEGEMENT_COUNT_PHRASE = 'Segment Counts'
CONSTANT_PLOT_TITLE_1 = 'URL Fraction'
CONSTANT_PLOT_TITLE_2 = 'HashTag Clarity'
CONSTANT_PLOT_TITLE_3 = 'Tweet Clarity'

CONSTANT_QUERY_TOP_TRENDING_HASHTAGS = "SELECT hashtag, COUNT(hashtag) FROM world.tweet_dataset GROUP BY hashtag ORDER BY COUNT(hashtag) DESC LIMIT 5;"

CONSTANT_QUERY_HASHTAG_BASED_TWEETS = "SELECT w from world.tweet_dataset WHERE hashtag LIKE '%"  

CONSTANT_QUERY_HASHTAG_WITH_COUNTS = "SELECT hashtag, COUNT(hashtag) FROM world.tweet_dataset GROUP BY hashtag ORDER BY COUNT(hashtag) DESC LIMIT 5;"
CONSTANT_QUERY_GET_ALL_HASHTAGS = "SELECT hashtag from world.tweet_dataset WHERE hashtag is not null;" 

CONSTANT_KEYWORD_HASHTAG = "#"
CONSTANT_KEYWORD_AT_RATE = "@"
CONSTANT_KEYWORD_HTTP = "http"

CONSTANT_INPUT_VALIDATION_ERROR = "Input does not contain any elements/value in it. Please verify at the callable location!"
CONSTANT_EXCEPTION_ERROR = "Something went wrong, Please check the Error e"

CONSTANT_HASHTAG_CLARITY_VALUE = 0.25
CONSTANT_DEFAULT_VALUE = 0

CONSTANT_RE_CHECK_STRING_HAS_URL = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
CONSTANT_RE_0_9_VALIDATION = '^[0-9]*$'
