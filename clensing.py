import pandas as pd
data = pd.read_csv('Books.csv',delimiter=",")



data = data.drop(columns=['Image-URL-M'])
data = data.drop(columns=['Image-URL-S'])
data = data.drop(columns=['Image-URL-L'])
data = data.drop(columns=['Year-Of-Publication'])
data = data.drop(columns=['Publisher'])
data = data.drop(columns=['Book-Author'])


print(data)

data.to_csv("new_books.csv")