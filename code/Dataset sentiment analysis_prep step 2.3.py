import pandas as pd
import urllib.request
import numpy as np
import json
from nltk.sentiment import SentimentIntensityAnalyzer

data = pd.read_csv('Output_Dataset final 4.3.2023.csv',delimiter=",")

row, col = data.shape

print("rows : ",row)

analyzer = SentimentIntensityAnalyzer()

#creating data frame and the columns
output_file = pd.DataFrame(columns=["ISBN","Book_Title","Description","sentiment_score_neg","sentiment_score_neu",
                                    "sentiment_score_pos","sentiment_score_compound"])

sample=""


for i in range(2,row):

    temp = analyzer.polarity_scores(data["Description"][i])
    sample = str(temp)

    sample = sample.replace(":", "").replace("{", "").replace("}", "").replace("'neg'", "").replace("'neu'", "") \
        .replace("'pos'", "").replace("'compound'", "")

    sample = sample.split(',')

    output_file.loc[i] = [data["ISBN"][i],data["Book_Title"][i],data["Description"][i],sample[0],sample[1],sample[2],sample[3]]
    print(data["Description"][i],"  ",sample[0],sample[1],sample[2],sample[3])



output_file.to_csv('Output_Dataset final 4.3.2023 ver1.csv', encoding='utf-8')