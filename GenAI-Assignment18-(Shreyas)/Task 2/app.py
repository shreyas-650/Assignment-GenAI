#Task 2 - One Hot Encoding Using SK Learn
from sklearn.feature_extraction.text import CountVectorizer
text= ['People Love AI','AI includes ML','ML includes DL','AI includes NLP','AI loves NLP']

cv = CountVectorizer(binary=True)
text = cv.fit_transform(text)

print(cv.vocabulary_)
print(text.toarray())