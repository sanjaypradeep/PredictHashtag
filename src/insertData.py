from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import json

import mysql.connector
from mysql.connector import Error

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


def readFile(con):
    
    with open("C:\\Users\\sanja\\Desktop\\FL\\March, 2020\\PopularTweet\\datasets\\test5060K-7500k_1.txt", "r", encoding='utf-8') as dataContent:        

        t = ""
        u = ""
        w = ""
        hashTag = "" 
        mentioned = ""
        for i in dataContent:
            # print(i)       

            if(i[0] == "T"):
                byTab = i.split("\t")
                t += byTab[1]
            if(i[0] == "U"):
                byTab = i.split("\t")
                u += byTab[1]
            if(i[0] == "W"):
                byTab = i.split("\t")
                w += json.dumps(byTab[1])
                # print("Befor stripping - W ...", w)
                w = w.strip('\"')
                w = w.replace("'", "")
                w = w.replace("\\n", "")
                w = w.replace("\\n\\", "")
                # print("After stripping - W ...", w)

                splittedTweet = w.split()
                hashTagList = []
                for tagElement in splittedTweet:
                    if (tagElement.startswith('#')):
                        hashTagList.append(tagElement)
                print("Found HashTag - ", hashTagList)

                mentioned = []
                splittedSentence = w.split()
                
                if(len(splittedSentence) == 1):
                    if(len(splittedSentence[0]) > 20):
                        print("some unusal language may be.")
                        pass
                else:                    
                    for tag in splittedSentence:
                        if tag.startswith("@"):
                            mentioned.append(tag.strip("@"))
                
                mentionedString = ""
                hashTagString = ""
                if(len(mentioned)> 1):
                    for i in mentioned:
                        mentionedString += "@" + str(i) + ","
                elif (len(mentioned) == 1):
                    mentionedString += str(mentioned[0])
                else:
                    mentionedString = ""

                if len(mentionedString) > 50:
                    mentionedString = ""

                if(len(hashTagList) > 1):
                    for i in hashTagList:
                        hashTagString +=  str(i) + " "
                elif (len(hashTagList) == 1):
                    hashTagString += str(hashTagList[0])
                
                if len(hashTagString) > 50:
                    hashTagString = ""

                print("final #HashTags .. " , hashTagString)
                print("final @mentioned .. ",mentionedString)
                        
            if t != "" and u != "" and w != "":
                if len(hashTag) == 0 and len(mentionedString) == 0:                    
                    print("both are not avaialble")
                    workingQuery = "INSERT INTO `world`.`tweet_dataset` (`t`, `u`,`w`) VALUES ('" + t + "','" + u + "','" + w + "');"

                    cursor = con.cursor()
                    cursor.execute(workingQuery)
                    con.commit()

                if len(hashTag) > 0 and len(mentionedString) >0:
                    print("Both available..")
                    workingQuery = "INSERT INTO `world`.`tweet_dataset` (`t`, `u`,`w`, `hashtag`, `mention` ) VALUES ('" + t + "','" + u + "','" + w + "','" + hashTagString + "','" + mentionedString + "');"

                    cursor = con.cursor()
                    cursor.execute(workingQuery)
                    con.commit()

                if len(hashTag) > 0 and len(mentionedString) == 0:
                    print("only hashTag value available")
                    print("insert without mentioned")
                    workingQuery = "INSERT INTO `world`.`tweet_dataset` (`t`, `u`,`w`, `hashtag`) VALUES ('" + t + "','" + u + "','" + w + "','" + hashTagString + "');"

                    cursor = con.cursor()
                    cursor.execute(workingQuery)
                    con.commit()

                elif len(hashTag) == 0 and len(mentionedString) > 0:
                    print("only mentioned available but not hashtag")
                    workingQuery = "INSERT INTO `world`.`tweet_dataset` (`t`, `u`,`w`, `mention`) VALUES ('" + t + "','" + u + "','" + w + "','" + mentionedString + "');"

                    cursor = con.cursor()                     
                    cursor.execute(workingQuery)
                    con.commit()

                t = ""
                u = ""
                w = ""
                hashTag = ""
                mentioned = ""
            




if __name__ == '__main__':

    connectionHook = connectToDB()
    readFile(connectionHook)
