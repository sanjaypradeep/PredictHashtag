import mysql.connector
from mysql.connector import Error
import constant
import json

def connectToDB():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='world',
                                            user='root',
                                            password='root',
                                            auth_plugin='mysql_native_password')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("\nConnected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("\nYou're connected to database: ", record)
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)


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

def fx1(connectionString, hashTagList, globalInfoObj):    
    if (connectionString == '' or len(hashTagList) ==0 or len(globalInfoObj) == 0):
        return
    
    try:        
        for hash in hashTagList:
            sql_select_Query = constant.CONSTANT_FX1_QUERY_PART_1 + hash + constant.CONSTANT_FX1_QUERY_PART_2
            cursor = connectionString.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()

            globalInfoObj[hash][constant.CONSTANT_FX1] = list(records[0])[0]
                    
        return globalInfoObj
    except Error as e:
        print(constant.CONSTANT_EXCEPTION_ERROR, e)

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

def fx3(connectionString, hashTagList, globalInfoObj):    
    if (connectionString == '' or len(hashTagList) ==0 or len(globalInfoObj) == 0):
        return
    
    try:        
        for hash in hashTagList:
            sql_select_Query = constant.CONSTANT_FX3_QUERY_PART1 + hash + constant.CONSTANT_FX3_QUERY_PART2
            cursor = connectionString.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            
            totalReplyList = []
            for rec in records:
                totalReplyList.append(rec[1])

            globalInfoObj[hash][constant.CONSTANT_FX3_REPLY_FRAC_VAL] = sum(totalReplyList) * 0.01
                    
        return globalInfoObj
    except Error as e:
        print(constant.CONSTANT_EXCEPTION_ERROR, e)

def reTweetCount(connectionString, hashTagName):
    if (connectionString == '' or len(hashTagName) == 0):
        return
    
    try:        
        sql_select_Query = constant.CONSTANT_RT_COUNT_QUERY_PART1 + hashTagName + constant.CONSTANT_RT_COUNT_QUERY_PART2
        cursor = connectionString.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        
        tempReTweetList = []
        for rec in records:
            splittedRecord = rec[0].split()
            for spRec in splittedRecord[:4]:
                if 'RT' in spRec or 'rt' in spRec:
                    tempReTweetList.append(rec[0])

        toBeSent = {hashTagName: len(tempReTweetList)}
       
        return toBeSent            
                            
    except Error as e:
        print(constant.CONSTANT_EXCEPTION_ERROR, e)


def fx4(connectionString, hashTagList, globalInfoObj):
    if (connectionString == '' or len(hashTagList) ==0 or len(globalInfoObj) == 0):
        return
    
    try:
        for hashTagName in hashTagList:
            rtCountObject = reTweetCount(connectionString, hashTagName)            
            globalInfoObj[hashTagName][constant.CONSTANT_FX4_RTWT_FRAC_VAL] = list(rtCountObject.values())[0]
            
        return globalInfoObj
    except Error as e:
        print(constant.CONSTANT_EXCEPTION_ERROR)

def getAllMentionedUsersFromHashTag(connectionString, hashTagList):

    if (connectionString == '' or len(hashTagList) ==0):
        return
    try:
        htObjWithUsers = {}
        for hashTagName in hashTagList:
            sql_select_Query = constant.CONSTANT_MENTIONED_USER_QUERY_PART1 + hashTagName + constant.CONSTANT_MENTIONED_USER_QUERY_PART2
            cursor = connectionString.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()

            htObjWithUsers[hashTagName] = [rec[0] for rec in records]        
        
        with open(constant.CONSTANT_FILE_NAME_EXCLUDE, constant.CONSTANT_FILE_WRITE_PERMISSION) as userData:
            json.dump(htObjWithUsers, userData)

        for key,value in htObjWithUsers.items():
            testing = _collectInfoStoreLocal(connectionString, key, value)

    except Error as e:
        print(constant.CONSTANT_EXCEPTION_ERROR)

def _collectInfoStoreLocal(connectionString, trendingHashtag, usersList):
    try:
        userMentionedObj = {}
        sample = {}
        for user in usersList[1:]:             
            if user:
                sql_select_Query = constant.CONSTANT_COLLECT_LOCAL_INFO_STORE_LOCAL_PART1 + user + constant.CONSTANT_COLLECT_LOCAL_INFO_STORE_LOCAL_PART2
                cursor = connectionString.cursor()
                cursor.execute(sql_select_Query)
                records = cursor.fetchall()

                sample[user] = list(records[0])[0]

        userMentionedObj[trendingHashtag] = sample

        trendingHashtag = trendingHashtag.replace("\n", "")
        trendingHashtag = trendingHashtag.replace("/n", "")
        trendingHashtag = trendingHashtag.replace('"', "")

        with open(trendingHashtag+constant.CONSTANT_FILE_EXTENSION_TYPE, constant.CONSTANT_FILE_WRITE_PERMISSION) as userData:
            json.dump(userMentionedObj, userData)
        
        return True
    except Error as e:
        print(constant.CONSTANT_EXCEPTION_ERROR)


def fx5(hashTagList, globalInfoObj):
    sample = {}
    
    import os

    availableJsonFiles = []    
    for root, dirs, files in os.walk("."):        
        for filename in files:
            if constant.CONSTANT_FILE_EXTENSION_TYPE in filename:                
                if constant.CONSTANT_FILE_NAME in filename or constant.CONSTANT_FILE_NAME_EXCLUDE in filename:
                    pass
                else:
                    availableJsonFiles.append(filename)
        break
        
    for files in availableJsonFiles:
        dat = open(files) 
        
        hashTagUserCount = json.load(dat)
        userMentionCount = []
        for key,value in hashTagUserCount.items():
            hashTagName = key
            for k,v in value.items():
                userMentionCount.append(v)
        
        setInfo = set(userMentionCount)

        userMentionCount.sort()
        userMentionCount.reverse()

        x = len([i for i in userMentionCount if i>1])
        sample[hashTagName] = {constant.CONSTANT_FX5_USR_AUTH:  x/len(userMentionCount) }
        
    sampleKeys = list(sample.keys())
    globalKeys = list(globalInfoObj.keys())

    for ele in sampleKeys:
        if ele in globalInfoObj:
            globalInfoObj[ele][constant.CONSTANT_FX5_USR_AUTH] = sample[ele][constant.CONSTANT_FX5_USR_AUTH]

    return globalInfoObj
    

if __name__ == constant.CONSTANT_MAIN_HOOK:

    
    connectionHook = connectToDB()

    topTrendingHash = getAllTopTrendingHashTagsFromDataset(connectionHook)    

    print("============Sub Module 1 Executed=============")

    import json 
  
    # Opening JSON file 
    f = open(constant.CONSTANT_FILE_NAME,) 

    contextualJSON = json.load(f)

    print("============Sub Module 1 Executed=============")

    print("============ Content Lexical Module Starting...=============")

    thisLevelGlobalObject = fx1(connectionHook, topTrendingHash, contextualJSON)

    print("================ FX1 Completed =============")


    thisLevelGlobalObject = fx3(connectionHook, topTrendingHash, thisLevelGlobalObject)    
    
    print("================ FX2 Completed =============")
    print("================ FX3 Completed =============")


    thisLevelGlobalObject = fx4(connectionHook, topTrendingHash, thisLevelGlobalObject)
    # print(thisLevelGlobalObject)

    print("================ FX4 Completed =============")


    # *****Below code can be commented after executing for the first time ****
    # getAllMentionedUsersFromHashTag(connectionHook, topTrendingHash)
    # *************************************************************************

    thisLevelGlobalObject = fx5(topTrendingHash, thisLevelGlobalObject)
    # print(thisLevelGlobalObject)

    print("================ FX5 Completed =============")

    print(" Please Execute clGraphy.py as a next process .. ")
    print(" Please Execute predictTomoHashTag.py as final process .. ")


