import matplotlib.pyplot as plt
import constant
import json

if __name__ == constant.CONSTANT_MAIN_HOOK:

    contentResultFile = open(constant.CONSTANT_FILE_NAME) 
        
    hashTagInfo = json.load(contentResultFile)

    topTrendingHashGroups = list(hashTagInfo.keys())
    topTrendingHashGroups = [i.replace('\n', "")for i in topTrendingHashGroups]

    topTrendingHashValues = []

    for ht,value in hashTagInfo.items():
        topTrendingHashValues.append((value[constant.CONSTANT_FC2_WORD_SEGEMENTS]))
    
    
    plt.figure(figsize=(9, 3))

    plt.subplot(131)
    plt.bar(topTrendingHashGroups, topTrendingHashValues)
    plt.subplot(132)
    plt.scatter(topTrendingHashGroups, topTrendingHashValues)
    plt.subplot(133)
    plt.plot(topTrendingHashGroups, topTrendingHashValues)
    plt.suptitle(constant.CONSTANT_SEGEMENT_WORD_PHRASE)
    plt.ylabel(constant.CONSTANT_SEGEMENT_COUNT_PHRASE)
    plt.show()

    topTrendingHashValues.clear()
    for ht,value in hashTagInfo.items():
        topTrendingHashValues.append((value[constant.CONSTANT_FC3_URL_FRACTION]))
    
    
    plt.scatter(topTrendingHashGroups, topTrendingHashValues)
    plt.title(constant.CONSTANT_PLOT_TITLE_1)
    plt.show()

    topTrendingHashValues.clear()
    for ht,value in hashTagInfo.items():
        topTrendingHashValues.append((value[constant.CONSTANT_FC6_HASHTAG_CLARITY]))
    
    
    plt.scatter(topTrendingHashGroups, topTrendingHashValues)
    plt.title(constant.CONSTANT_PLOT_TITLE_2)
    plt.show()

    topTrendingHashValues.clear()
    for ht,value in hashTagInfo.items():
        topTrendingHashValues.append((value[constant.CONSTANT_FC7_TWEET_CLARITY]))
    
    
    plt.bar(topTrendingHashGroups, topTrendingHashValues)
    plt.title(constant.CONSTANT_PLOT_TITLE_3)
    plt.show()
