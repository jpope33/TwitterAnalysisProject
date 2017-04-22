import sys
import json
from twitter import *
import datetime
from collections import Counter
import re

def getTimeStatistics(twitterHandle):

    global userTweets

    # used as printing format
    # non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

    ACCESS_TOKEN = "23141275-vOOBFygRqPQswrtEzIwSxFXY75TLBhLYkPFtDiwTm"
    ACCESS_SECRET = "JobHvwTLlx9jUFNNzax0XSvEU90mK4o77mc2d9vePjfMw"
    CONSUMER_KEY = "GEub3JcSlctyCwyC76alQxDeq"
    CONSUMER_SECRET = "TqCauPlX1oJxnr9czBCkDgV3REgoGogHSYbmAUBfJ6j8KLONqu"

    # connect to twitter API
    twitter = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

    # tweet1: stores all tweets with detailed information
    tweet1 = []

    # variable for twitter query instance(s)
    JSONroot = twitter.statuses.user_timeline(screen_name=twitterHandle, count=1)

    tweet1.extend(JSONroot)

    # oldest: Oldest tweet id used to keep track when pulling over 200 tweets
    oldest = tweet1[0]['id']

    # counting variables
    earlyTweet = midTweet = eveningTweet = lateTweet = count = tweetAnalysisVolume = 0

    userTweets = []

    # print("\nInfo on " + " historical tweets from: " + twitterHandle + "\n")

    while len(JSONroot) > 0:

        JSONroot = twitter.statuses.user_timeline(screen_name=twitterHandle, count=200, max_id=oldest, include_rts=False)

        # tweetsPulled: number of tweets pulled out of 200 i.e. if user has 206 tweets, 1st pull is 200, 2nd is 6
        tweetsPulled = len(JSONroot)
        tweet1.extend(JSONroot)
        oldest = tweet1[-1]['id'] - 1

        for i in range(0, tweetsPulled):
            # get utc tweet time and create datetime object
            createdAt = JSONroot[i]['created_at']

            # timestamp on tweet converted to datetime format
            originalDatetime = datetime.datetime.strptime(createdAt, "%a %b %d %H:%M:%S %z %Y")

            # get tweet utc offset (seconds)
            utcOffsetSeconds = JSONroot[i]['user']['utc_offset']

            # compenstate utc offset
            convertedTimeDate = originalDatetime + datetime.timedelta(seconds=utcOffsetSeconds)
            hour = convertedTimeDate.hour
            #print("Hour of tweet:" + str(hour))

            # used later in regex parser I believe?????     LOOK HERE!!!!!!!!!!!!!!!!!!!!
            tweet = JSONroot[i]['text']
            userTweets.append(tweet)

            # incrementor maintenance
            tweetAnalysisVolume += 1

            #print(tweet.translate(non_bmp_map) + "\n")

            # increment tweet tally by timeframe
            hour = convertedTimeDate.hour
            # print("Converted Hour:" + str(hour))
            if 2 <= hour < 8:
                earlyTweet += 1
                #print("Early Tweet")
            elif 8 <= hour < 14:
                midTweet += 1
                #print("Mid Tweet")
            elif 14 <= hour < 20:
                eveningTweet += 1
                #print("Evening Tweet")
            else:
                lateTweet += 1
                #print("Late Tweet")

    # tweet percentage stats and prints
    earlyTweetPercent = earlyTweet / tweetAnalysisVolume * 100.
    lunchTweetPercent = midTweet / tweetAnalysisVolume * 100.
    eveningTweetPercent = eveningTweet / tweetAnalysisVolume * 100.
    lateTweetPercent = lateTweet / tweetAnalysisVolume * 100.

    '''
    print("Early Percent: " + str(round(earlyTweetPercent, 1)) + "%")
    print("Lunch Percent: " + str(round(lunchTweetPercent, 1)) + "%")
    print("Evening Percent: " + str(round(eveningTweetPercent, 1)) + "%")
    print("Late Percent: " + str(round(lateTweetPercent, 1)) + "%")
    '''

    statisitcs = {}
    statisitcs['earlyTweet'] = round(earlyTweetPercent, 1)
    statisitcs['midTweet'] = round(lunchTweetPercent, 1)
    statisitcs['eveningTweet'] = round(eveningTweetPercent, 1)
    statisitcs['lateTweet'] = round(lateTweetPercent, 1)

    return statisitcs

def getWordStatistics():

    global userTweets

    # list of empty words to ignore when finding common terms used
    ignore = ['rt', 'rts', 'retweet', 'a', 'an', 'am', 'of', 'that', 'with', 'will', 'at', 'by', 'not', 'no', 'yes',
              'was', 'very',
              'they', 'the', 'and', 'are', 'you', 'him', 'her', 'his', 'hers', 'for', 'to', 'in', 'on', 'i', 'is', 'if',
              'me', 'my', 'myself', 'we', 'our', 'ours', 'your', 'youre', 'yours', 'he', 'hes', 'she', 'shes', 'it',
              'its',
              'what', 'do', 'did', 'after', 'before', 'as', 'be', 'this', 'too', 'next', 'go', 'day', 'night', 'tell',
              'us',
              'came', 'know', 'girl', 'boy', 'face', 'good', 'best', 'never', 'has', 'have', 'had', 'up', 'new', 'make',
              'so', 'out', 'all', 'more', 'president', 'news', 'their', 'there', 'must', 'ok', 'last', 'first',
              'get', 'lol', 'but', 'see', 'saw', 'about', 'dont', 'do', 'amp', 'im', 'these', 'would', 'can', 'cant',
              'when', 'why', 'take', 'ive', 'or', 'than', 'them', 'eat', 'eating', 'pm', 'b', 'c', 'd', 'e', 'f', 'g',
              'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'were',
              'where', 'tonight', 'tomorrow', 'week', 'thank', 'thanks', 'man', 'woman', 'from', 'like', 'come', 'just',
              'today', 'now', 'one', 'tv', 'eat', 'back', 'much', 'going', 'went', 'want', 'another', 'got', 'still',
              'yall', 'whats', 'how', 'lets', 'lot', 'been', 'here', 'hear', 'way', 'some', 'little', 'big', 'ill',
              'then',
              'think', 'feel', 'let', 'said', 'that', 'thats', 'because', 'off', 'time', 'ever', 'who', 'ur', 'right',
              'someone', 'oh', 'people', 'life', 'gonna', 'being', 'hello', 'hi', 'havent', 'goodbye', 'well']

    allTweets = ''.join(userTweets)
    # removal of @user, digits, #, links
    allTweets = re.sub("(@[A-Za-z0-9]+)|([0-9]+\S+?)|(\\d)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", '', allTweets,
                       flags=re.MULTILINE)
    allTweets = allTweets.lower()
    allTweets = allTweets.split()
    termsUsed = [term for term in allTweets if term not in ignore]

    count = Counter()
    count.update(termsUsed)
    countTuple = count.most_common(10)

    # print([countTuple])

    statistics = {}
    statistics['commonWords'] = list(map(lambda x: {'word': x[0], 'frequency': x[1]},countTuple))
    # print(statistics)
    # statisitcs['commonWord'] = countTuple[0]
    # statisitcs['wordCount'] = countTuple[1]
    return statistics

#function calls
# twitterHandle = sys.argv[1]

# timeStats = getTimeStatistics(twitterHandle)
#print(timeStats)

# wordStats = getWordStatistics()
#print(wordStats)

# dictAll = {}
# dictAll.update(timeStats)
# dictAll.update(wordStats)

# JSONobject = json.dumps(dictAll)
# print(JSONobject)

def userInfo(twitterHandle):
    timeStats = getTimeStatistics(twitterHandle)
    wordStats = getWordStatistics()

    dictAll = {}
    dictAll.update(timeStats)
    dictAll.update(wordStats)
    
    return dictAll
