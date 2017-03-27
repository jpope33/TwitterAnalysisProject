from json import *
from twitter import *
import operator
from collections import Counter
import datetime
import re

#You'll need to replace these values with your own twitter app, start at https://apps.twitter.com
#After creating a new app find the needed creditials at 'Keys and Access Tokens' tab
ACCESS_TOKEN = "at"
ACCESS_SECRET = "as"
CONSUMER_KEY = "ck"
CONSUMER_SECRET = "cs"
#connect to twitter API
twitter = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

#simple user input for twitter handle
twitterHandle = input("Enter twitter handle for analysis: ")

tweet1 = []
tweet2 = []
tweetAnalysisVolume = 0

#variable for twitter query instance(s)
JSONroot = twitter.statuses.user_timeline(screen_name=twitterHandle,count=1)
tweet1.extend(JSONroot)
#Oldest tweet id, used to pull more than 200
oldest = tweet1[0]['id']
earlyTweet = lunchTweet = eveningTweet = lateTweet = 0
print("\nInfo on " + " historical tweets from: " + twitterHandle + "\n")
while len(JSONroot) > 0:
    JSONroot = twitter.statuses.user_timeline(screen_name=twitterHandle, count=200,max_id=oldest)
    #number of tweets pulled out of 200 i.e. if user has 6 tweets, check = 6
    tweetsPulled = len(JSONroot)
    tweet1.extend(JSONroot)
    oldest = tweet1[-1]['id'] - 1
    for i in range(0, tweetsPulled):
        #get utc tweet time and create datetime object
        createdAt = JSONroot[i]['created_at']
        originalDatetime = datetime.datetime.strptime(createdAt, "%a %b %d %H:%M:%S %z %Y")
        #print("Original Time: " + str(originalDatetime))
        #get tweet utc offset (seconds)
        utcOffsetSeconds = JSONroot[i]['user']['utc_offset']
        #compenstate utc offset
        convertedTimeDate = originalDatetime
        #print("Converted Time: " + str(convertedTimeDate))
        #increment tweet tally by timeframe
        hour = convertedTimeDate.hour
        print("Converted Hour:" + str(hour))
        if 2 <= hour < 8:
            earlyTweet += 1
            print("Early Tweet")
        elif 8 <= hour < 14:
            lunchTweet += 1
            print("Lunch Tweet")
        elif 14 <= hour < 20:
            eveningTweet += 1
            print("Evening Tweet")
        else:
            lateTweet += 1
            print("Late Tweet")

        #get tweet text
        tweet = JSONroot[i]['text']
        count = Counter()
        tweetAnalysisVolume += 1
        tweet2.append(JSONroot[i]['text'])
        print(createdAt)
        print(tweet + "\n")


#tweet percentage stats and prints
earlyTweetPercent = earlyTweet/tweetAnalysisVolume*100.
lunchTweetPercent = lunchTweet/tweetAnalysisVolume*100.
eveningTweetPercent = eveningTweet/tweetAnalysisVolume*100.
lateTweetPercent = lateTweet/tweetAnalysisVolume*100.
print("Early Percent: " + str(round(earlyTweetPercent, 2)) + "%")
print("Lunch Percent: " + str(round(lunchTweetPercent, 2)) + "%")
print("Evening Percent: " + str(round(eveningTweetPercent, 2)) + "%")
print("Late Percent: " + str(round(lateTweetPercent, 2)) + "%")
print("Total Tweets: " + tweetAnalysisVolume)

#list of empty words to ignore when finding common terms used
ignore = ['rt', 'retweet', 'a', 'an', 'am', 'of', 'that', 'with', 'will', 'at', 'by', 'not', 'no', 'yes', 'was', 'very',
          'they', 'the', 'and', 'are', 'you', 'him', 'her', 'his', 'hers', 'for', 'to', 'in', 'on', 'i', 'is', 'if',
          'me', 'my', 'myself', 'we', 'our', 'ours', 'your', 'youre', 'yours', 'he', 'hes', 'she', 'shes', 'it', 'its',
          'what', 'do', 'did', 'after', 'before', 'as', 'be', 'this', 'too', 'next', 'go', 'day', 'night', 'tell', 'us',
          'came', 'know', 'girl', 'boy', 'face', 'good', 'best', 'never', 'has', 'have', 'had', 'up', 'new', 'make',
          'so', 'out', 'all', 'more', 'president', 'news', 'their', 'there', 'must', 'ok', 'last', 'first',
          'get', 'lol', 'but', 'see', 'saw', 'about', 'dont', 'do', 'amp', 'im', 'these', 'would', 'can', 'cant',
          'when', 'why', 'take', 'ive', 'or', 'than', 'them', 'eat', 'eating', 'pm', 'am', 'b', 'c', 'd', 'e', 'f', 'g',
          'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'were',
          'where', 'tonight', 'tomorrow', 'week', 'thank', 'thanks', 'man', 'woman', 'from', 'like', 'come', 'just',
          'today', 'now', 'one', 'tv', 'eat', 'back', 'much', 'going', 'went', 'want', 'another', 'got', 'still',
          'yall', 'whats', 'how', 'lets', 'lot', 'been', 'here', 'hear', 'way', 'some', 'little', 'big', 'ill', 'then',
          'think', 'feel', 'let', 'said', 'that', 'thats', 'because', 'off', 'on', 'time', 'ever', 'who', 'ur', 'right',
          'someone', 'oh', 'people', 'life', 'gonna', 'being', 'hello', 'hi', 'havent', 'goodbye', 'well']

allTweets = ''.join(tweet2)
#removal of @user, digits, #, links
allTweets = re.sub("(@[A-Za-z0-9]+)|([0-9]+\S+?)|(\\d)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", '', allTweets,
                   flags=re.MULTILINE)
allTweets = allTweets.lower()
allTweets = allTweets.split()
termsUsed = [term for term in allTweets if term not in ignore]
count.update(termsUsed)
print(count.most_common(10))










