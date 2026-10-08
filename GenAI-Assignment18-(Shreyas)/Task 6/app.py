#Task 6: Tokenization
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

df = pd.read_csv('../final_clean_text.csv')
clean = df['final_clean'].head(100)



cv = CountVectorizer(ngram_range=(1,2))
text = cv.fit_transform(clean)
print('\nFor Ngram_range(1,2)')
print(len(cv.vocabulary_))
print(cv.get_feature_names_out())
print(text.toarray())
print(text.toarray().shape) 
#observation:- ngram range 1,1 + 2,2 = 4266 + 11372 = 15638 

