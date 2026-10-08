#Task 3 Bag of Words Representation
from sklearn.feature_extraction.text import CountVectorizer
text= ['People Love AI','AI includes ML','ML includes DL','AI includes NLP','AI loves NLP']

cv = CountVectorizer()
text = cv.fit_transform(text)

print(len(cv.vocabulary_))
print(cv.get_feature_names_out())
print(text.toarray())