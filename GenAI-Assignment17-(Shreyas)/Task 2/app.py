#Task 2 - Basic Text Cleaning
import pandas as pd
import re
df = pd.read_csv('../IMDB Dataset.csv')

#Convert Text to lowercase
def clean_text(text):
    temp = []
    for x in text.split():
        temp.append(x.lower())
    return " ".join(temp)

df['clean_text_basic'] = df['review'].apply(clean_text)
print(df.head(),'\n')

#Remove Punctuation
def rem_pun(text):
    return re.sub(r'[^\w\s]',"",text)
df['clean_text_basic'] = df['clean_text_basic'].apply(rem_pun)

print(df['clean_text_basic'].tail(),'\n')

#Remove Extra Whitespaces
def rem_whitespaces(text):
    return re.sub(r'\s+'," ",text).strip()
df['clean_text_basic'] = df['clean_text_basic'].apply(rem_whitespaces)
print(df['clean_text_basic'].head())