import constant

overAllData = {
    "spymaster": {
        "FC1_ContainDigits": "False",
        "FC2_SegWordNum": 2,
        "FX2_TotalTweetCount": 842,
        "FC3_UrlFraction": 1.0023809523809524,
        "FC6_HashTagClarity": 0.5,
        "FC7_TweetClarityPercentage": 92.1289123024481,
        "totalMentionedUsers": 266,
        "totalUniqueURLs": 17,
        "FX1_TotalUserCount": 286,
        "FX3_ReplyFractionValue": 0.28,
        "FX4_ReTweetFractionValue": 11,
        "FX5_UserAuthority": 0.2915129151291513
    },
    "MP2": {
        "FC1_ContainDigits": "True",
        "FC2_SegWordNum": 1,
        "FX2_TotalTweetCount": 490,
        "FC3_UrlFraction": 13.243243243243244,
        "FC6_HashTagClarity": 0.25,
        "FC7_TweetClarityPercentage": 80.04455387501466,
        "totalMentionedUsers": 88,
        "totalUniqueURLs": 36,
        "FX1_TotalUserCount": 347,
        "FX3_ReplyFractionValue": 3.02,
        "FX4_ReTweetFractionValue": 439,
        "FX5_UserAuthority": 0.18840579710144928
    },
    "squarespace": {
        "FC1_ContainDigits": "False",
        "FC2_SegWordNum": 2,
        "FX2_TotalTweetCount": 456,
        "FC3_UrlFraction": 4.903225806451613,
        "FC6_HashTagClarity": 0.5,
        "FC7_TweetClarityPercentage": 51.67270402727466,
        "totalMentionedUsers": 59,
        "totalUniqueURLs": 71,
        "FX1_TotalUserCount": 72,
        "FX3_ReplyFractionValue": 0.23,
        "FX4_ReTweetFractionValue": 64,
        "FX5_UserAuthority": 0.42592592592592593
    },
    "fb": {
        "FC1_ContainDigits": "False",
        "FC2_SegWordNum": 1,
        "FX2_TotalTweetCount": 398,
        "FC3_UrlFraction": 1.5731225296442688,
        "FC6_HashTagClarity": 0.25,
        "FC7_TweetClarityPercentage": 44.187923797223114,
        "totalMentionedUsers": 94,
        "totalUniqueURLs": 210,
        "FX1_TotalUserCount": 95,
        "FX3_ReplyFractionValue": 0.25,
        "FX4_ReTweetFractionValue": 95,
        "FX5_UserAuthority": 0.5555555555555556
    },
    "VampireBite": {
        "FC1_ContainDigits": "False",
        "FC2_SegWordNum": 3,
        "FX2_TotalTweetCount": 369,
        "FC3_UrlFraction": 1.005449591280654,
        "FC6_HashTagClarity": 0.75,
        "FC7_TweetClarityPercentage": 79.9592252803262,
        "totalMentionedUsers": 723,
        "totalUniqueURLs": 227,
        "FX1_TotalUserCount": 367,
        "FX3_ReplyFractionValue": 0.5,
        "FX4_ReTweetFractionValue": 19,
        "FX5_UserAuthority": 0.2716417910447761
    }
}


scoreOutput = {}

for hashTag, values in overAllData.items():
    # print(hashTag)
    print(values[constant.CONSTANT_FC1_CONTAINING_DIGITS])

    if (values[constant.CONSTANT_FC1_CONTAINING_DIGITS] == constant.CONSTANT_BOOL_TRUE):
        scoreOutput[hashTag] = {
            "score_fc1" : 1,
            "score_fc2" : values[constant.CONSTANT_FC2_WORD_SEGEMENTS],
            "score_fc3" : values[constant.CONSTANT_FC3_URL_FRACTION],
            "score_fc6" : values[constant.CONSTANT_FC6_HASHTAG_CLARITY],
            "score_fc7" : values[constant.CONSTANT_FC7_TWEET_CLARITY],
            "score_fx1" : values[constant.CONSTANT_FX1] / 100,
            "score_fx2" : values[constant.CONSTANT_FX2_TOTAL_TWEET_COUNT]/100,
            "score_fx3" : values[constant.CONSTANT_FX3_REPLY_FRAC_VAL],
            "score_fx4" : values[constant.CONSTANT_FX4_RTWT_FRAC_VAL]/100,
            "score_fx5" : values[constant.CONSTANT_FX5_USR_AUTH]
        }
    else:
        scoreOutput[hashTag] = {
            "score_fc1": 0,
            "score_fc2" : values[constant.CONSTANT_FC2_WORD_SEGEMENTS],
            "score_fc3" : values[constant.CONSTANT_FC3_URL_FRACTION],
            "score_fc6" : values[constant.CONSTANT_FC6_HASHTAG_CLARITY],
            "score_fc7" : values[constant.CONSTANT_FC7_TWEET_CLARITY],
            "score_fx1" : values[constant.CONSTANT_FX1] / 100,
            "score_fx2" : values[constant.CONSTANT_FX2_TOTAL_TWEET_COUNT] /100,
            "score_fx3" : values[constant.CONSTANT_FX3_REPLY_FRAC_VAL],
            "score_fx4" : values[constant.CONSTANT_FX4_RTWT_FRAC_VAL]/100,
            "score_fx5" : values[constant.CONSTANT_FX5_USR_AUTH]  
        }
    
    
    
print(scoreOutput)

overAllScore = {}

for k,v in scoreOutput.items():    
    print(k, sum(list(v.values())))
    overAllScore[k] = sum(list(v.values()))

from matplotlib import pyplot as plt 
  
from matplotlib import pyplot as plt 
  
# x-axis values 
x = list(overAllScore.keys())
  
# Y-axis values 
y = list(overAllScore.values())
  
# Function to plot the bar 
plt.bar(x,y) 
  
# function to show the plot 
plt.show() 
