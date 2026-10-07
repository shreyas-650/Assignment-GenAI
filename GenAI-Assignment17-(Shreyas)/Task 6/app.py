#Task 6: Tokenization
import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
nltk.download('punkt_tab')
df = pd.read_csv('../IMDB Dataset.csv')
df['word_tokens'] = df['review'].apply(word_tokenize)
df['sent_tokens'] = df['review'].apply(sent_tokenize)

print(df.head())
print(df['word_tokens'].head(3))

