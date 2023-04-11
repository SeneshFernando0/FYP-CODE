
import pandas as pd
import random as rand
import urllib.request
import json

import tensorflow as tf
from transformers import BertTokenizer

import numpy as np




#seniment finding system -----------------------------------------------------------------------------------------------

data = pd.read_csv('Output_Dataset final 4.3.2023 tensorflow ready.csv',delimiter=",") #getting books from dataset


sentiment_model = tf.keras.models.load_model('sentiment_model new')

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

def make_prediction(model, processed_data):
    probs = model.predict(processed_data)[0]
    return np.argmax(probs)


input_text = input('today is a very happy day')

processed_data = prepare_data(input_text, tokenizer)
result = make_prediction(sentiment_model, processed_data=processed_data)
print(f"Predicted Sentiment: {result}")




#book reco system-------------------------------------------------------------------------------------------------------

base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"


if (result==0):
    count=0
    for i in range(rand.randint(1, 50), 600):
        if count > 5:
            break
        if (float(data["sentiment_type"][i]) >= result):
            def isbn_count(temp):
                while (len(temp) != 10):
                    temp = "0" + temp
                return str(temp)

            with urllib.request.urlopen(base_api_link + isbn_count(str(data["ISBN"][i]))) as f:
                text = f.read()

            decoded_text = text.decode("utf-8")
            obj = json.loads(decoded_text)  # deserializes decoded_text to a Python object
            volume_info = obj["items"][0]

            ToFrontend = {"book_name": str(data["Book_Title"][i]), "book_description": str(data["Description"][i]),
                          "sentiment": int(data["sentiment_type"][i]),
                          "image_url": str(volume_info["volumeInfo"]["imageLinks"]["thumbnail"])}

            #print("name :" + volume_info["volumeInfo"]["imageLinks"]["thumbnail"] + "\n")

            print(json.dumps(ToFrontend))

            print("book recommendations : " + data["Book_Title"][i]+data["ISBN"][i])
            count= count+1



if (result==1):
    count = 0
    for i in range(rand.randint(1, 50), 600):
        if count > 5:
            break
        if (float(data["sentiment_type"][i]) >= result):

            def isbn_count(temp):
                while (len(temp) != 10):
                    temp = "0" + temp
                return str(temp)


            with urllib.request.urlopen(base_api_link + isbn_count(str(data["ISBN"][i]))) as f:
                text = f.read()

            decoded_text = text.decode("utf-8")
            obj = json.loads(decoded_text)  # deserializes decoded_text to a Python object
            volume_info = obj["items"][0]

            ToFrontend = {"book_name": str(data["Book_Title"][i]),"book_description": str(data["Description"][i]), "sentiment":int(data["sentiment_type"][i]),
                          "image_url":str(volume_info["volumeInfo"]["imageLinks"]["thumbnail"])}

            #print("name :" + volume_info["volumeInfo"]["imageLinks"]["thumbnail"] + "\n")

            print(json.dumps(ToFrontend))

            print("book recommendations : " + data["Book_Title"][i]+data["ISBN"][i])
            count = count + 1


if (result==2):
    count = 0
    for i in range(rand.randint(1, 50), 600):
        if count > 5:
            break
        if (float(data["sentiment_type"][i]) >= result):
            def isbn_count(temp):
                while (len(temp) != 10):
                    temp = "0" + temp
                return str(temp)


            with urllib.request.urlopen(base_api_link + isbn_count(str(data["ISBN"][i]))) as f:
                text = f.read()

            decoded_text = text.decode("utf-8")
            obj = json.loads(decoded_text)  # deserializes decoded_text to a Python object
            volume_info = obj["items"][0]

            ToFrontend = {"book_name": str(data["Book_Title"][i]), "book_description": str(data["Description"][i]),
                          "sentiment": int(data["sentiment_type"][i]),
                          "image_url": str(volume_info["volumeInfo"]["imageLinks"]["thumbnail"])}

            #print("name :" + volume_info["volumeInfo"]["imageLinks"]["thumbnail"] + "\n")

            print(json.dumps(ToFrontend))

            print("book recommendations : " + data["Book_Title"][i]+data["ISBN"][i])
            count = count + 1

else:
    print("No recommendations found")

#return jsonify({'results': ToFrontend})




