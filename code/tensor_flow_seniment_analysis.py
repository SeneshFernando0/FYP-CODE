import pandas as pd
import numpy as np
from tqdm.auto import tqdm
import tensorflow as tf
from transformers import BertTokenizer
from transformers import TFBertModel




df = pd.read_csv('Output_Dataset final 4.3.2023 tensorflow ready.csv', delimiter=",")



print(df.head())
print(df.info())
print(df['sentiment_type'].value_counts())

tokenizer = BertTokenizer.from_pretrained('bert-base-cased')

X_input_ids = np.zeros((len(df), 256))
X_attn_masks = np.zeros((len(df), 256))


def generate_training_data(df, ids, masks, tokenizer):
    for i, text in tqdm(enumerate(df['Description'])):
        tokenized_text = tokenizer.encode_plus(
            text,
            max_length=256,
            truncation=True,
            padding='max_length',
            add_special_tokens=True,
            return_tensors='tf'
        )
        ids[i, :] = tokenized_text.input_ids
        masks[i, :] = tokenized_text.attention_mask
    return ids, masks


X_input_ids, X_attn_masks = generate_training_data(df, X_input_ids, X_attn_masks, tokenizer)

labels = np.zeros((len(df), 5))

dataset = tf.data.Dataset.from_tensor_slices((X_input_ids, X_attn_masks, labels))


def SentimentDatasetMapFunction(input_ids, attn_masks, labels):
    return {
        'input_ids': input_ids,
        'attention_mask': attn_masks
    }, labels


dataset = dataset.map(SentimentDatasetMapFunction)  # converting to required format for tensorflow dataset

dataset = dataset.shuffle(10000).batch(16, drop_remainder=True)  # batch size, drop any left out tensor

train_size = int(
    (len(df) // 16) * 0.8)  # for each 16 batch of data we will have len(df)//16 samples, take 80% of that for train.

train_dataset = dataset.take(train_size)
val_dataset = dataset.skip(train_size)

# model------------------------------------------------------------------------------------------------------------------

model = TFBertModel.from_pretrained('bert-base-cased')  # bert base model with pretrained weights


# defining 2 input layers for input_ids and attn_masks
input_ids = tf.keras.layers.Input(shape=(256,), name='input_ids', dtype='int32')
attn_masks = tf.keras.layers.Input(shape=(256,), name='attention_mask', dtype='int32')

bert_embds = model.bert(input_ids, attention_mask=attn_masks)[1] # 0 -> activation layer (3D), 1 -> pooled output layer (2D)
intermediate_layer = tf.keras.layers.Dense(512, activation='relu', name='intermediate_layer')(bert_embds)
output_layer = tf.keras.layers.Dense(5, activation='softmax', name='output_layer')(intermediate_layer) # softmax -> calcs probs of classes

sentiment_model = tf.keras.Model(inputs=[input_ids, attn_masks], outputs=output_layer)
print(sentiment_model.summary())

optim = tf.keras.optimizers.Adam(
    learning_rate=0.0001,
    beta_1=0.9,
    beta_2=0.999,
    epsilon=1e-07,
    amsgrad=False,
    weight_decay=None,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    jit_compile=True,
    name="Adam",
)

loss_func = tf.keras.losses.CategoricalCrossentropy()
acc = tf.keras.metrics.CategoricalAccuracy('accuracy')

sentiment_model.compile(optimizer=optim, loss=loss_func, metrics=[acc])


hist = sentiment_model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=25)

sentiment_model.save('sentiment_model new')




