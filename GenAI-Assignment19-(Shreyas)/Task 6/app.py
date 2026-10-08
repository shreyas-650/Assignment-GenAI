#Task 6: Train Word2Vec Model

import pandas as pd
import gensim
from nltk.tokenize import word_tokenize,sent_tokenize
df = pd.read_csv('../final_clean_text.csv')
df = df['final_clean'].head(110)
word =[]
for x in df:
    for y in sent_tokenize(x):
        word.append(word_tokenize(y))

model = gensim.models.Word2Vec(window=5,vector_size=100,min_count=1,sg=0)
model.build_vocab(word)
model.train(word,total_examples=model.corpus_count,epochs=model.epochs)
print(model.wv.key_to_index)
print('\n',model.wv['car'])


