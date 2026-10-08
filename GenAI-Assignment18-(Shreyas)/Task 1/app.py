#Task 1 Understanding Raw Text Data
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

text= ['People Love AI','AI includes ML','ML includes DL','AI includes NLP','AI loves NLP']

#------------- Built Vocabulary
vocab = set()

for sentance in text:
    for word in sentance.split():
        vocab.add(word)
vocab = sorted(vocab)
#--------------  One Hot Encoding Matrix
main = []
for sentance in text:
    temp =[]
    for word in vocab:
        if word in sentance.split():
            temp.append(1)
        else:
            temp.append(0)
    main.append(temp)

print(main)

print(vocab)