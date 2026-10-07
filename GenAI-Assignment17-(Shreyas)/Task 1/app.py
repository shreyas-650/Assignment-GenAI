#Task 1 Understanding Raw Text Data
import pandas as pd
df = pd.read_csv(r'..\IMDB Dataset.csv')

print(df.head(5))
print(df['review'].apply(len))

# Uppercase/lowercase mismatch
print(df['review'].head().to_list())

# Punctuation
import string
print(df['review'].apply(lambda x: any(i in string.punctuation for i in x)))

# Numbers
print(df['review'].str.contains(r'\d+', regex=True))

# Extra spaces
print(df['review'].apply(lambda x: '  ' in x))