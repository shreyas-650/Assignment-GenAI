#Task 2 - Handling Data & Text Features
import pandas as pd
path = '../online food delivery dataset.csv'
df = pd.read_csv(path)

df['Text length'] = df['Educational Qualifications'].str.len()
print(df[df['Text length']==8])
print(df['Educational Qualifications'].unique())
print(df[['Educational Qualifications','Text length']])