#Task 5 Handlin Repeated Character & Slang
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

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
#-------------------    Advanced Remove Emoji and SP char
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

#---------------- Handling Stop Words
# nltk.download('stopwords') load 1 Time
english = stopwords.words('english')

def rem_stopword(text):
    temp =[]
    for x in text.split():
        if(x not in english):
            temp.append(x)
    return " ".join(temp)

df['clean_text_advanced'] = df['clean_text_advanced'].apply(rem_stopword)
print(df['clean_text_advanced'].head())
#--------------- Repeated Character Fix like soooo---> so
def normalize_repeated(text):
    return re.sub(r'(.)\1+', r'\1\1', text)
df['clean_text_advanced'] = df['clean_text_advanced'].apply(normalize_repeated)
#--------------- Slang Dictonary
slang_dict={
    'u':'you',
    'gr8':'great'
}

def slang_expand(text,slang_dict):
    words = text.split()
    return " ".join(slang_dict(word,word) for word in words)
    
df['clean_text_advanced'] = df['clean_text_advanced'].apply(slang_expand,slang_dict=slang_dict)
print(df['clean_text_advanced'].head())