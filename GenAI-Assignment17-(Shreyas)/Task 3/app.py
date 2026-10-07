#Task 3 Remove Noise
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
#-------------------   Advanced Cleaning Techniques
def rem_url(text):
    return re.sub(r'https?://\S+|www\.\S+',"",text)
df['clean_text_basic']=df['clean_text_basic'].apply(rem_url)
#-------------------    Advanced Remove Email Addresses
def rem_email(text):
    return re.sub(r'\S*@\S*\s?',"",text)
df['clean_text_basic']=df['clean_text_basic'].apply(rem_email)
#-------------------    Advanced Remove HTML Tags
def remove_html(text):
    return re.sub(r'<.*?>',"",text)
df['clean_text_basic'] = df['clean_text_basic'].apply(remove_html)
#-------------------    Advanced Remove Emoji and SP char (Same In Punctuation)
def remove_special_emoji(text):
    return re.sub(r'[^\w\s]', '', text)
df['clean_text_basic'] = df['clean_text_basic'].apply(remove_special_emoji)

#Remove Punctuation
def rem_pun(text):
    return re.sub(r'[^\w\s]',"",text)
df['clean_text_basic'] = df['clean_text_basic'].apply(rem_pun)

#Remove Extra Whitespaces
def rem_whitespaces(text):
    return re.sub(r'\s+'," ",text).strip()
df['clean_text_basic'] = df['clean_text_basic'].apply(rem_whitespaces)

df['clean_text_advanced'] = df['clean_text_basic']
print(df['clean_text_advanced'].head())