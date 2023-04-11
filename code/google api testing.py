import pandas as pd
import urllib.request
import numpy as np
import json

base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

user_input="0393045218"

with urllib.request.urlopen(base_api_link + user_input) as f:
    text = f.read()

decoded_text = text.decode("utf-8")
obj = json.loads(decoded_text)  # deserializes decoded_text to a Python object
volume_info = obj["items"][0]

# displays title, summary, author, domain, page count and language

print("name :" + volume_info["volumeInfo"]["description"] + "\n")
print("name :" + volume_info["volumeInfo"]["imageLinks"]["thumbnail"] + "\n")