#Task 8 BoW vs TF-IDF Comparison
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
df = pd.read_csv('../final_clean_text.csv')
clean = df['final_clean'].head(100)
tf = TfidfVectorizer()
encoding = tf.fit_transform(clean).toarray()
features=tf.get_feature_names_out()


#-------------------------------------
max_value = encoding.max()
index = encoding.argmax() #Return the index of maximum
row, col = divmod(index, encoding.shape[1])

print('Word:', features[col])
print('TF-IDF:', max_value)

#---------------- Top 10 High TF-IDF

word_scores = encoding.max(axis=0)
print(word_scores)
top_10 = np.argsort(word_scores)[-10:][::-1]

for i in top_10:
    print(features[i], word_scores[i])

#----------------- Low TF-IDF
word_scores = encoding.min(axis=0)

top_10 = np.argsort(word_scores)[:10]

for i in top_10:
    print(features[i], word_scores[i])


#TF-IDF down-weights common words because a word that appears in many documents doesnt help distinguish one document from another.