#Task 5 Unigrams,Bigrams & Trigrams
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

df = pd.read_csv('../final_clean_text.csv')
clean = df['final_clean'].head(100)

for x in range(1,4):

    cv = CountVectorizer(ngram_range=(x,x))
    text = cv.fit_transform(clean)
    print('\nFor Ngram_range',x)
    print(len(cv.vocabulary_))
    print(cv.get_feature_names_out())
    print(text.toarray())
    print(text.toarray().shape)