#Task 3 One-Hot Encoding
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
path = '../online food delivery dataset.csv'
df = pd.read_csv(path)
oh = OneHotEncoder()
df = pd.get_dummies(df,columns=['Gender'],dtype=int)
# display
print(df.iloc[:,2:])