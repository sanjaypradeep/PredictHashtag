import constant
import json

dat = open(constant.CONSTANT_FILE_NAME, constant.CONSTANT_FILE_WRITE_PERMISSION)
overAllJSONResult = json.load(dat)

scoreOutput = {}

# for hashTag, values in overAllData.items():
for hashTag, values in overAllJSONResult.items():
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
    # print(k, sum(list(v.values())))
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
