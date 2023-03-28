import pandas as pd
import urllib.request
import numpy as np
import json
from nltk.sentiment import SentimentIntensityAnalyzer



data = pd.read_csv('Finalset.csv',delimiter=",")

row, col = data.shape

print("rows : ",row)


#initialization
analyzer = SentimentIntensityAnalyzer()




#creating data frame and the columns
output_file = pd.DataFrame(columns=["ISBN","Book_Title","Description","sentiment_score_neg","sentiment_score_neu",
                                    "sentiment_score_pos","sentiment_score_compound","sentiment_type"])


for i in range(2,685):
    tempvaluearray =[data["sentiment_score_neg"][i],data["sentiment_score_neu"][i],data["sentiment_score_pos"][i]]
    if (float(data["sentiment_score_neg"][i]) == max(tempvaluearray)):
        output_file.loc[i] = [data["ISBN"][i], data["Book_Title"][i], data["Description"][i],data["sentiment_score_neg"][i],data["sentiment_score_neu"][i]
            ,data["sentiment_score_pos"][i],data["sentiment_score_compound"][i],0]
        continue

    elif(float(data["sentiment_score_neu"][i]) == max(tempvaluearray)):
        output_file.loc[i] = [data["ISBN"][i], data["Book_Title"][i], data["Description"][i],data["sentiment_score_neg"][i], data["sentiment_score_neu"][i]
            ,data["sentiment_score_pos"][i], data["sentiment_score_compound"][i],1]
        continue

    elif(float(data["sentiment_score_pos"][i]) == max(tempvaluearray)):
        output_file.loc[i] = [data["ISBN"][i], data["Book_Title"][i], data["Description"][i],data["sentiment_score_neg"][i], data["sentiment_score_neu"][i]
            ,data["sentiment_score_pos"][i], data["sentiment_score_compound"][i],2]
        continue

    print("count : ",i)



#save as csv file
output_file.to_csv('Output_Dataset_for_tensorflow.csv', encoding='utf-8')