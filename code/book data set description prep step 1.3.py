import pandas as pd
import urllib.request
import numpy as np
import json

base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

data = pd.read_csv('Books.csv', delimiter=",")

row, col = data.shape

print("rows : ", row)

# size of the data set
ran = range(row)

file = open('numbers new 11.txt', 'w')

# creating data frame and the columns
output_file = pd.DataFrame(columns=["ISBN", "Book_Title", "Description"])

for i in range(250000, 270000):
    try:
        user_input = data.at[i, 'ISBN']
        with urllib.request.urlopen(base_api_link + user_input) as f:
            text = f.read()

        decoded_text = text.decode("utf-8")
        obj = json.loads(decoded_text)  # deserializes decoded_text to a Python object
        volume_info = obj["items"][0]
    except:
        # if isbn is invalid skip the record /book
        print("ISBN not found " + str(i))
        continue

    try:
        # save to txt file
        file.write(" id : " + str(i) + " ISBN : " + user_input + "  | name : " + volume_info["volumeInfo"][
            "title"] + "  |  description : " + volume_info["volumeInfo"]["description"] + "\n")
        # save to data frame
        output_file.loc[i] = [user_input, volume_info["volumeInfo"]["title"], volume_info["volumeInfo"]["description"]]
    except:
        # if description is not found skip
        print("description not found " + str(i))
        continue

    print(i)

# save as txt file
file.close()

# save as csv file
output_file.to_csv('Output_Dataset new 11.csv', encoding='utf-8')
