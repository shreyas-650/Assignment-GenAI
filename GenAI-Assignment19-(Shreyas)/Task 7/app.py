#Task 7 Skip Gram Word2Vec Model
import pandas as pd
import gensim
from nltk.tokenize import word_tokenize,sent_tokenize
import time

df = pd.read_csv('../final_clean_text.csv')
df = df['final_clean'].head(110)
word =[]
for x in df:
    for y in sent_tokenize(x):
        word.append(word_tokenize(y))
#------------------- CBOW Time Calculation
start = time.time()

model = gensim.models.Word2Vec(window=5,vector_size=100,min_count=1,sg=0)
model.build_vocab(word)
model.train(word,total_examples=model.corpus_count,epochs=model.epochs)
print(len(model.wv.key_to_index))
print('\n',model.wv['car'])

cbow_time = time.time() - start

#------------------------- Skip Gram Time Calculation
start = time.time()

gm_model = gensim.models.Word2Vec(window=5,vector_size=100,min_count=1,sg=0)
gm_model.build_vocab(word)
gm_model.train(word,total_examples=gm_model.corpus_count,epochs=gm_model.epochs)
print(len(gm_model.wv.key_to_index))
print('\n',model.wv['car'])

gm_time = time.time() - start

#------------
print(f'\nCbow Time : {cbow_time}\nSkipGram Time: {gm_time}')

#Compair Similar Word
print("CBOW:")
print(model.wv.most_similar('movie'))

print("\nSkip-Gram:")
print(gm_model.wv.most_similar('movie'))