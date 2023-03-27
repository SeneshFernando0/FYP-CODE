
import random as rand
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
print(dataframe)





data = pd.read_csv('Finalset.csv',delimiter=",") #getting books from dataset

row, col = data.shape

#print("rows : ",row)

analyzer = SentimentIntensityAnalyzer()



#initialization
analyzer = SentimentIntensityAnalyzer()

#input text
scores  = analyzer.polarity_scores(tweet.full_text)

sentiment = str(scores)

#clear the input data
sentiment = sentiment.replace(":", "").replace("{", "").replace("}", "").replace("'neg'", "").replace("'neu'", "") \
        .replace("'pos'", "").replace("'compound'", "")

sentiment = sentiment.split(',')

print("users emotion : ",scores)


#print("test  : ",float(data["sentiment_score_neg"][7]),"   ",float(data["sentiment_score_neu"][7]),"   ",float(data["sentiment_score_pos"][7]))


"""""
#find book recommendation
for i in range(rand.randint(1,50),600):

    if(float(data["sentiment_score_neg"][i])>=float(sentiment[0])) or (float(data["sentiment_score_neu"][i]) >= float(sentiment[1])) and (float(data["sentiment_score_pos"][i]) == float(sentiment[2])):
        print("book recommendations : "+data["Book_Title"][i])
        break

    else:
        print("No recommendations found")

"""""





if float(sentiment[0]) >float(sentiment[1]) and float(sentiment[0]) >float(sentiment[2]):
    for i in range(rand.randint(1, 50), 600):
        if (float(data["sentiment_score_neg"][i]) >= float(sentiment[0])):
            print("book recommendations : "+data["Book_Title"][i])


if float(sentiment[1]) > float(sentiment[0]) and float(sentiment[1]) > float(sentiment[2]):
    for i in range(rand.randint(1, 50), 600):
        if (float(data["sentiment_score_neu"][i]) >= float(sentiment[1])):
            print("book recommendations : " + data["Book_Title"][i])



if (float(sentiment[2]) > float(sentiment[0])) and (float(sentiment[2]) > float(sentiment[1])):

    for i in range(rand.randint(1, 50), 600):
        if (float(data["sentiment_score_pos"][i]) >= float(sentiment[2])):
            print("book recommendations : " + data["Book_Title"][i])


else:
    print("No recommendations found")













