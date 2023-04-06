import requests
import tweepy
from flask import Flask, jsonify, request
import tensorflow as tf
import configparser
#from flask_cors import CORS
from http import HTTPStatus
import numpy as np
from transformers import BertTokenizer

#twitter configration---------------------------------------------------------------------------------------------------
config = configparser.ConfigParser()
config.read("config.ini")

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret=config['twitter']['access_token_secret']

#twitter authentication
auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#-----------------------------------------------------------------------------------------------------------------------


app = Flask(__name__)
#CORS(app)



data = [{'id': 1, 'name': "senesh", 'book recommendation': "twilight saga"}]
name =""
twitter=""

# api end points

@app.route('/results', methods=['GET'])
def get_results():
#twitter api------------------------------------------------------------------------------------------------------------
    tweets = api.user_timeline(screen_name=twitter, count=5, tweet_mode='extended')

    for tweet in tweets:
        data.append([tweet.user.screen_name, tweet.full_text])
#-----------------------------------------------------------------------------------------------------------------------

#sentiment prediction model---------------------------------------------------------------------------------------------
    sentiment_model = tf.keras.models.load_model('sentiment_model')

    tokenizer = BertTokenizer.from_pretrained('bert-base-cased')

    def prepare_data(input_text, tokenizer):
        token = tokenizer.encode_plus(
            input_text,
            max_length=256,
            truncation=True,
            padding='max_length',
            add_special_tokens=True,
            return_tensors='tf'
        )
        return {
            'input_ids': tf.cast(token.input_ids, tf.float64),
            'attention_mask': tf.cast(token.attention_mask, tf.float64)
        }

    def make_prediction(model, processed_data,
                        classes=['Negative', 'Neutral', 'Positive']):
        probs = model.predict(processed_data)[0]
        return classes[np.argmax(probs)]


    processed_data = prepare_data(tweet.full_text, tokenizer)
    result = make_prediction(sentiment_model, processed_data=processed_data)
    print(f"Predicted Sentiment: {result}")

    return jsonify({'results': data})
#-----------------------------------------------------------------------------------------------------------------------

@app.route('/home', methods=['POST'])
def get():
    print("name "+request.json['name'])
    print("twitter"+ request.json['twitter'])
    global name
    global twitter
    name = request.json['name']
    twitter=request.json['twitter']
    return jsonify({})



if __name__ == '__main__':
    app.run()
