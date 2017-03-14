from json import *
from twitter import *
import datetime

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

#variable for twitter query instance(s)
JSONroot = twitter.statuses.user_timeline(screen_name=twitterHandle)

earlyTweet = lunchTweet = eveningTweet = lateTweet = 0
tweetAnalysisVolume = 20 # values greater than 20 crash
print("\nInfo on " + str(tweetAnalysisVolume) + " historical tweets from: " + twitterHandle + "\n")

for i in range(0,tweetAnalysisVolume):

    #get utc tweet time and create datetime object
    createdAt = JSONroot[i]['created_at']
    originalDatetime = datetime.datetime.strptime(createdAt, "%a %b %d %H:%M:%S %z %Y")
    #print("Original Time: " + str(originalDatetime))

    #get tweet utc offset (seconds)
    utcOffsetSeconds = JSONroot[i]['user']['utc_offset']

    #compenstate utc offset
    convertedTimeDate = originalDatetime + datetime.timedelta(seconds=utcOffsetSeconds)
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











