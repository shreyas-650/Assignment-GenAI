#Task 4 Column Transformer(Recommended Way)
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
path = '../online food delivery dataset.csv'
df = pd.read_csv(path)
df.drop(columns=['Unnamed: 13'],inplace=True)
#Separate
numerical = df.select_dtypes('number').columns
categorical = df.select_dtypes('string','category').columns

#Column Transformer
ct = ColumnTransformer(transformers=[('t1',OneHotEncoder(),categorical)],remainder='passthrough')
final = pd.DataFrame(
    ct.fit_transform(df),
    columns=ct.get_feature_names_out()
)
print(final)



