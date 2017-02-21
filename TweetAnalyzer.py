from json import *
from twitter import *
from datetime import datetime

ACCESS_TOKEN = "2284703554-UKL8uB7CMWFGNCVbB351XpD2hz9yu8V5FkVeBlO"
ACCESS_SECRET = "dENDW7fIbFPYtxITKpHIhvwyxog5qSNxkFbPPPAgZZohh"
CONSUMER_KEY = "Uo80ux5dv9yjlbiAbaT5iniaE"
CONSUMER_SECRET = "RKRn0hUl4XbCSopJJ7v4hvYJrFMmNkOgopsHvpKtRMfXwhvN85"

#connect to twitter API
twitter = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

#simple user input for twitter handle
twitterHandle = input("Enter twitter handle for analysis: ")

#variable for twitter query instance(s)
JSONroot = twitter.statuses.user_timeline(screen_name=twitterHandle)

print("Info on 5 most recent tweets from: " + twitterHandle)
for i in range(0,5):

    #get utc tweet time
    createdAt = JSONroot[i]['created_at']

    #get tweet utc offset (seconds)
    utcOffsetHours = JSONroot[i]['user']['utc_offset']

    #get tweet timezone
    timeZone = JSONroot[i]['user']['time_zone']

    # get tweet text
    tweet = JSONroot[i]['text']

    print(createdAt + ' : ' + timeZone + ' : ' + str(utcOffsetHours) + ' : ' + tweet)







