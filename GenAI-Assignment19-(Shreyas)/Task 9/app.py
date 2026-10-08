#Task 9 Visualization Word Embedding
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

#----------------- Reduce Dimensions
from sklearn.decomposition import PCA
pca = PCA(n_components=3)
X=pca.fit_transform(model.wv.get_normed_vectors())
y = model.wv.index_to_key

import plotly.io as pio
pio.renderers.default = 'browser'

import plotly.express as px
fig = px.scatter_3d(X[:100],x=0,y=1,z=2,color=y[:100])
fig.show()