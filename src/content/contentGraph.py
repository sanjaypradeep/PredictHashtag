import matplotlib.pyplot as plt
import constant
import json

if __name__ == '__main__':

    contentResultFile = open(constant.CONSTANT_FILE_NAME) 
        
    hashTagInfo = json.load(contentResultFile)

    topTrendingHashGroups = list(hashTagInfo.keys())
    topTrendingHashGroups = [i.replace('\n', "")for i in topTrendingHashGroups]

    topTrendingHashValues = []

    for ht,value in hashTagInfo.items():
        topTrendingHashValues.append((value["FC2_SegWordNum"]))
    
    
    plt.figure(figsize=(9, 3))

    plt.subplot(131)
    plt.bar(topTrendingHashGroups, topTrendingHashValues)
    plt.subplot(132)
    plt.scatter(topTrendingHashGroups, topTrendingHashValues)
    plt.subplot(133)
    plt.plot(topTrendingHashGroups, topTrendingHashValues)
    plt.suptitle('Segement Word Plots')
    plt.ylabel("Segment Counts")
    plt.show()

    topTrendingHashValues.clear()
    for ht,value in hashTagInfo.items():
        topTrendingHashValues.append((value["FC3_UrlFraction"]))
    
    
    plt.scatter(topTrendingHashGroups, topTrendingHashValues)
    plt.title("URL Fraction")
    plt.show()

    topTrendingHashValues.clear()
    for ht,value in hashTagInfo.items():
        topTrendingHashValues.append((value["FC6_HashTagClarity"]))
    
    
    plt.scatter(topTrendingHashGroups, topTrendingHashValues)
    plt.title("HashTag Clarity")
    plt.show()

    topTrendingHashValues.clear()
    for ht,value in hashTagInfo.items():
        topTrendingHashValues.append((value["FC7_TweetClarityPercentage"]))
    
    
    plt.bar(topTrendingHashGroups, topTrendingHashValues)
    plt.title("Tweet Clarity")
    plt.show()
