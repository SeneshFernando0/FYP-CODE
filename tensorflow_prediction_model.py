import pandas as pd
import numpy as np
from tqdm.auto import tqdm
import tensorflow as tf
from transformers import BertTokenizer
from transformers import TFBertModel

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


tokenizerd_input = prepare_data(input_text="Practice Makes Pregnant by Lois Faye Dyer released on Sep 30, 2003 is available now for purchase", tokenizer=tokenizer)
probs = sentiment_model.predict(tokenizerd_input)

print(probs)
val = np.argmax(probs[0])
print(val)

if(val == 0):
    print("the prediction is : negative")
elif(val==1):
    print("the prediction is : neutral")
elif(val==2):
    print("the prediction is : positive")

