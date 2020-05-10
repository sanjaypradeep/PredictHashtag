import re
import constant

def fc1(inputHashTags):
    # checks whether hashtag contains any digits
    if(len(inputHashTags) == 0):
        return constant.CONSTANT_INPUT_VALIDATION_ERROR
    elif(inputHashTags[0] == constant.CONSTANT_KEYWORD_HASHTAG and len(inputHashTags) == 1):
        return False
    else:
        check = re.match(constant.CONSTANT_RE_0_9_VALIDATION, inputHashTags[1:])
        if (check == None):
            return True #means it also has alphhabets in it.
        else:
            return False

def fc1_alternate(inputHashTag):
    return bool(re.search(r'\d', inputHashTag))

import wordsegment as ws
from wordsegment import load, segment

def fc2(inputHashTags):
    # check number of word segements in the given input hashtags
    if(len(inputHashTags) == 0):        
        return constant.CONSTANT_INPUT_VALIDATION_ERROR
    elif(inputHashTags[0] == constant.CONSTANT_KEYWORD_HASHTAG and len(inputHashTags) == 1):
        return constant.CONSTANT_INPUT_VALIDATION_ERROR
    else:
        load()
        x = segment(inputHashTags[1:])
        return len(x)

import re 

def checkStringHasURL(inputTweetsList):
   # findall() has been used  
   # with valid conditions for urls in string
   totalTweetsWithURL = 0
   for i in inputTweetsList:
       ur = re.findall(constant.CONSTANT_RE_CHECK_STRING_HAS_URL, i) 
       if(len(ur) > 0):
           totalTweetsWithURL += 1

   return(totalTweetsWithURL)

def fc3(masterObj, totalTweetsAvailableWithUrl):
    for key, value in totalTweetsAvailableWithUrl.items():
        masterObj[key][constant.CONSTANT_FC3_URL_FRACTION] = masterObj[key][constant.CONSTANT_FX2_TOTAL_TWEET_COUNT] / value
    
    print("Completing FC3..")
    return masterObj


def KL(a, b):
    a = np.asarray(a, dtype=np.float)
    b = np.asarray(b, dtype=np.float)

    return np.sum(np.where(a != 0, a * np.log(a / b), 0))


def fc4():
    pass

def fc5():
    pass

def getAllHashTags(connectionString):
    try:
        allHashTagsFromDB = []

        sql_select_Query = constant.CONSTANT_QUERY_GET_ALL_HASHTAGS
        cursor = connectionString.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        
        for rec in records:
            allHashTagsFromDB.append(rec[0])     
        return allHashTagsFromDB
    except Error as e:
         print(constant.CONSTANT_EXCEPTION_ERROR)

def counterMappedHashTags(listOfHashTags):
    if(len(listOfHashTags) == 0):
        return
    return {x:listOfHashTags.count(x) for x in listOfHashTags}

def fc6(infoObj): #HashTagWordClarity
    if(len(infoObj)) == 0:
        return constant.CONSTANT_INPUT_VALIDATION_ERROR
    for key, value in infoObj.items():
        if value[constant.CONSTANT_FC2_WORD_SEGEMENTS] > 1:
            infoObj[key][constant.CONSTANT_FC6_HASHTAG_CLARITY] = value[constant.CONSTANT_FC2_WORD_SEGEMENTS] * constant.CONSTANT_HASHTAG_CLARITY_VALUE
        elif value[constant.CONSTANT_FC2_WORD_SEGEMENTS] == 1:
            infoObj[key][constant.CONSTANT_FC6_HASHTAG_CLARITY] = constant.CONSTANT_HASHTAG_CLARITY_VALUE
        else:
            infoObj[key][constant.CONSTANT_FC6_HASHTAG_CLARITY] = constant.CONSTANT_DEFAULT_VALUE
    return infoObj

def fc7(infoObj): #TweetClarity
    if(len(infoObj)) == 0:
        return constant.CONSTANT_INPUT_VALIDATION_ERROR
    
    sampleOb = {}
    for key, value in infoObj.items():
        overAllTweet = value
        
        allTweetString = ""
        for tweets in overAllTweet:
            allTweetString += tweets + ""    
        
        totalLenOfAllTweetString = len(allTweetString.split(" "))

        totalLenOfUniqueWords = len(set(allTweetString.split(" ")))

        tweetClarityCalc =  (totalLenOfUniqueWords/totalLenOfAllTweetString) * 100

        # print(key.replace("\n", ""), 100 - tweetClarityCalc)

        totalUnquieWords = set(allTweetString.split(" "))


        hT = []
        menD = []
        urls = []
        others = []
        for uniqueWords in totalUnquieWords:
            if uniqueWords[0] == constant.CONSTANT_KEYWORD_AT_RATE:
                menD.append(uniqueWords)
            elif uniqueWords[0] == constant.CONSTANT_KEYWORD_HASHTAG:
                hT.append(uniqueWords)
            elif uniqueWords[0:4] == constant.CONSTANT_KEYWORD_HTTP:
                urls.append(uniqueWords)
            else:
                others.append(uniqueWords)

        sampleOb[key] = {
                            constant.CONSTANT_FC7_TWEET_CLARITY : 100 - tweetClarityCalc,
                            constant.CONSTANT_TOTAL_MENTIONED_USERS : len(menD), 
                            constant.CONSTANT_TOTAL_UNIQUE_URLS : len(urls)
                        }

        # print(sampleOb)

    return sampleOb
    

def fx2_getTotalTweets(connectionString, hashTagInfo):
    try:
        sql_select_Query = constant.CONSTANT_QUERY_HASHTAG_WITH_COUNTS
        cursor = connectionString.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        for row in records:
            hashTagInfo[row[0]][constant.CONSTANT_TOTAL_TWEET_COUNTS] = row[1]                  
        
        return hashTagInfo
    except Error as e:
        print(constant.CONSTANT_EXCEPTION_ERROR)

def getTweetsBasedOnHashTag(connectionString, hashTagList):
    if(len(hashTagList) == 0):
        return
    try:
        sampleObj =  {}
        for hashTag in hashTagList:
            sql_select_Query = constant.CONSTANT_QUERY_HASHTAG_BASED_TWEETS + hashTag + "%';"    
            cursor = connectionString.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()

            tweetList = []
            for rec in records:
                tweetList.append(rec[0])        

            sampleObj[hashTag] = tweetList
        return sampleObj
    except Error as e:
         print(constant.CONSTANT_EXCEPTION_ERROR)


def getAllTopTrendingHashTagsFromDataset(connectionString):
    try:
        sql_select_Query = constant.CONSTANT_QUERY_TOP_TRENDING_HASHTAGS
        cursor = connectionString.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        trendingHashtags = []
        for row in records:
            trendingHashtags.append(row[0])

        return trendingHashtags
    except Error as e:
        print(constant.CONSTANT_EXCEPTION_ERROR)

import mysql.connector
from mysql.connector import Error

def connectToDB():
    try:
        connection = mysql.connector.connect(host= constant.DB_CONFIG["HOST"],
                                            database=constant.DB_CONFIG["database"],
                                            user= constant.DB_CONFIG["user"],
                                            password= constant.DB_CONFIG["password"],
                                            auth_plugin= constant.DB_CONFIG["auth_plugin"])
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("\nConnected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("\nYou're connected to database: ", record)
            return connection
    except Error as e:
        print(constant.CONSTANT_EXCEPTION_ERROR)

if __name__ == constant.CONSTANT_MAIN_HOOK:

    connectionHook = connectToDB()

    topTrendingHash = getAllTopTrendingHashTagsFromDataset(connectionHook)

    sampleHashTagObjj = {}
    for topHash in topTrendingHash:
        if fc1_alternate(topHash):
            sampleHashTagObjj[topHash] = { constant.CONSTANT_FC1_CONTAINING_DIGITS : "True"}
        else:
            sampleHashTagObjj[topHash] = {constant.CONSTANT_FC1_CONTAINING_DIGITS : "False"}

        segNumbers = fc2(topHash)
        sampleHashTagObjj[topHash][constant.CONSTANT_FC2_WORD_SEGEMENTS] = segNumbers

    # print(sampleHashTagObjj)

    hashTagObj = fx2_getTotalTweets(connectionHook, sampleHashTagObjj)

    allTweetsBasedOnHashTag = getTweetsBasedOnHashTag(connectionHook, topTrendingHash)

    # print(allTweetsBasedOnHashTag)

    print("=========FX2 Completed ============")

    tempInfo = {}
    for key,value in allTweetsBasedOnHashTag.items():
        opValue = checkStringHasURL(value)
        tempInfo[key] = opValue
    # print(tempInfo)

    fc3CompletedHashTagObj = fc3(hashTagObj, tempInfo)
    # print(fc3CompletedHashTagObj)

    print("==================FC3 Completed =========================")

    fc6CompletionObj = fc6(fc3CompletedHashTagObj)

    # print(fc6CompletionObj)

    globalInfoObj = fc6CompletionObj

    print("=========FC6 Completed ============")


    test = fc7(allTweetsBasedOnHashTag)

    for key,value in globalInfoObj.items():
        globalInfoObj[key][constant.CONSTANT_FC7_TWEET_CLARITY] = test[key]['FC7_TweetClarityPercentage']
        globalInfoObj[key][constant.CONSTANT_TOTAL_MENTIONED_USERS] = test[key]['totalMentionedUsers']
        globalInfoObj[key][constant.CONSTANT_TOTAL_UNIQUE_URLS] = test[key]['totalUniqueURLs']
    
    # print(globalInfoObj)

    print("=========FC7 Completed ============")

    import json

    with open(constant.CONSTANT_FILE_NAME, constant.CONSTANT_FILE_WRITE_PERMISSION) as contextTweet:
        json.dump(globalInfoObj, contextTweet)

    print("=============== Context Process Completed =============")