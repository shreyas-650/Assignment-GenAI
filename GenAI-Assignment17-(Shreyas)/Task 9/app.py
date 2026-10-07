#Task 9 NLP Pipeline Creation
import pandas as pd
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('wordnet')
nltk.download('stopwords')
english = stopwords.words('english')

def nlp_preprocess(text):
    #Convert Text to lowercase
    temp = []
    for x in text.split():
        temp.append(x.lower())
    text =  " ".join(temp)
#---------------------------Noise Removal
    #URL Removal
    text= re.sub(r'https?://\S+|www\.\S+',"",text)
    #Email
    text= re.sub(r'\S*@\S*\s?',"",text)
    #Html
    text = re.sub(r'<.*?>',"",text)
    #Remove Punchuation/Special Char / Emoji
    text = re.sub(r'[^\w\s]',"",text)
    #Remove Extra WhiteSpaces
    text = re.sub(r'\s+'," ",text).strip()
#----------------  StopWord Removal
    temp = []
    for x in text.split():
        if x not in english:
            temp.append(x)
    text = " ".join(temp)
#----------------  Tokenization
    token = word_tokenize(text)
#----------------  Lemmatization
    temp =[]
    for x in token:
        temp.append(WordNetLemmatizer().lemmatize(x,pos='v'))
    return " ".join(temp)

df = pd.read_csv('../IMDB Dataset.csv')

with open('final_clean_text','w',encoding='utf-8') as file:
    temp =[]
    for x in df['review'].apply(nlp_preprocess):
        temp.append(x)
    text = "\n".join(temp)
    file.write(text)
    
