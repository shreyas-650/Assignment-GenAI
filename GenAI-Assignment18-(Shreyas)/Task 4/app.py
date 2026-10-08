#Task 4 Understanding Word Frequency
# from sklearn.feature_extraction.text import CountVectorizer
text= ['People Love AI','AI includes ML','ML includes DL','AI includes NLP','AI loves NLP']
freq = {}
# cv = CountVectorizer(max_features=None)
# text = cv.fit_transform(text)
# text = text.toarray()
# features = cv.get_feature_names_out()

for sentance in text:
    for word in sentance.split():
        freq[word] = freq.get(word,0) + 1
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print(sorted_freq)
print(sorted_freq[:-5:-1])

# BoW captures frequency information by representing each document as a vector where each value indicates the number of times a particular word occurs.
