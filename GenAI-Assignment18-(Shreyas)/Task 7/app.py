#Task 7 TF-IDF Implementation
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

df = pd.read_csv('../final_clean_text.csv')
clean = df['final_clean'].head(100)
tf = TfidfVectorizer()
encoding = tf.fit_transform(clean)

print(tf.get_feature_names_out())
print(encoding.shape) #4266
