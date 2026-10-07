#Task 7 Stemming
import pandas as pd
from nltk.stem import PorterStemmer
df = pd.read_csv('../IMDB Dataset.csv')
def stemmer(text):
    temp =[]
    for x in text.split():
        temp.append(PorterStemmer().stem(x))
    return " ".join(temp)
df['stem'] = df['review'].iloc[:5].apply(stemmer)
print(df['review'].head())
print(df['stem'].head(5))