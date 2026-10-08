#Task 5 Prepare Text for Word2Vec
import pandas as pd
from nltk.tokenize import sent_tokenize,word_tokenize
df = pd.read_csv('../final_clean_text.csv')
df = df['final_clean'].head(20)
sentance = []
for x in df:
    for y in sent_tokenize(x):
        sentance.append(word_tokenize(y))
print(sentance)
