import tweepy
import configparser
import pandas as pd

from nltk.sentiment import SentimentIntensityAnalyzer


#configration
config = configparser.ConfigParser()
config.read("config.ini")

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret=config['twitter']['access_token_secret']

#authentication
auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


#calling tewwets from specific user

user = 'sehtwiapi'
limit = 5

tweets = api.user_timeline(screen_name=user,count=limit, tweet_mode='extended')



#create data frame

column = ['user_name','tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

dataframe = pd.DataFrame(data, columns=column)



#sentiment analysis ----------------------------------------------------------------------------------------------------

#initialization
analyzer = SentimentIntensityAnalyzer()

#input text
sentiment = analyzer.polarity_scores(tweet.full_text)

print("tweet : ",tweet.full_text)

print(sentiment)







