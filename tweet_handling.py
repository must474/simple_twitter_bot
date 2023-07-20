def choosing_todays_tweet():
    f=open("tweets.txt","r")
    tweets=f.readlines()
    if len(tweets):
        tweet=tweets[0]
        f.close()
        tweets.remove(tweet)
        f=open("tweets.txt","w")
        f.writelines(tweets)
        return tweet
    else:
        return None
