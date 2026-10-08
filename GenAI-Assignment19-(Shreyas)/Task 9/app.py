#Task 9 Vectorizer Parameter Exploration
from sklearn.feature_extraction.text import CountVectorizer
text= ['People Love AI','AI includes ML','ML includes DL','AI includes NLP','AI loves NLP']
#-------------- MAX Freatures
cv = CountVectorizer(max_features=2)
text1 = cv.fit_transform(text)
print(text1.toarray())
print(len(cv.vocabulary_))
#-------------------------- min_df
min_df = CountVectorizer(min_df=4)
text2 = min_df.fit_transform(text)
print('\n',text2.toarray())
print(len(min_df.vocabulary_))
#-------------------------- max_df
max_df = CountVectorizer(max_df=1)
text3 = max_df.fit_transform(text)
print('\n',text3.toarray())
print(len(max_df.vocabulary_))