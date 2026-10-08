#Task 8 Word Similarity & Vector Operations

import pandas as pd
import gensim
from nltk.tokenize import word_tokenize,sent_tokenize

df = pd.read_csv('../final_clean_text.csv')
df = df['final_clean'].head(110)
word =[]
for x in df:
    word.append(word_tokenize(x))

model = gensim.models.Word2Vec(window=5,vector_size=100,min_count=1,sg=0)
model.build_vocab(word)
model.train(word,total_examples=model.corpus_count,epochs=model.epochs)
print(model.wv.most_similar('man'))

vec = model.wv['king'] - model.wv['man'] + model.wv['women']
print('\n',model.wv.most_similar([vec]))

print('\n',model.wv.doesnt_match(['car','man','women']))

print('\n',model.wv.similarity('ball','bat'))
