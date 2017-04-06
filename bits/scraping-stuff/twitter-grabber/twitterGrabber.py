from twython import Twython # pip install twython
import twitterKeys as tKey # get keys from .gitignored twitterKeys.py file
import time
import json

twitter = Twython(tKey.CONSUMER_KEY, tKey.CONSUMER_SECRET, tKey.ACCESS_KEY, tKey.ACCESS_SECRET)

user_timeline = twitter.get_user_timeline(screen_name="realDonaldTrump",count=1)
tweetList = [user_timeline[0]['id']] ## the latest starting tweet id; iterates backwards from

tweetCount = 0

outputJson = open("tweets.json", "w")
outputJson.write("[\n")

for i in range(0, 64): ## iterate through 3200 (max) tweets
## tweet extract method with the last tweetListt item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name = "realDonaldTrump",
    count = 200, include_retweets = False, max_id = tweetList[-1])

    for tweet in user_timeline:
        tweetCount = tweetCount + 1
        print (str(tweetCount) + ": " + tweet['text'].encode("utf-8")) ## print the tweet text
        	
        # print (tweet) # add the tweet to json array
        
        outputJson.write(json.dumps(tweet)+",")
		
        tweetList.append(tweet['id']) ## append tweet id's
		
	time.sleep(2) ## 2 second rest between api calls
	
outputJson.write("\n]")