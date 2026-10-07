#Task 8 Lemmatization
import pandas as pd
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
nltk.download('wordnet')
df = pd.read_csv('../IMDB Dataset.csv')
def stemmer(text):
    temp =[]
    for x in text.split():
        temp.append(PorterStemmer().stem(x))
    return " ".join(temp)
def lemmer(text):
    temp =[]
    for x in text.split():
        temp.append(WordNetLemmatizer().lemmatize(x,pos='v'))
    return " ".join(temp)
df['stem'] = df['review'].iloc[:5].apply(stemmer)
df['lemm'] = df['review'].iloc[:5].apply(lemmer)

print(df['stem'].head(5))
print(df['lemm'].head(5))