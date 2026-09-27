#Task 5 Standardization 
import pandas as pd
from sklearn.preprocessing import StandardScaler
path = '../online food delivery dataset.csv'
df = pd.read_csv(path)

numerical = df.select_dtypes('number')

ss = StandardScaler()

result= pd.DataFrame(
    ss.fit_transform(numerical),
    columns= numerical.columns
)
print(result)
#Mean Becomes 0 and STD = 1
print(result.std())
print(result.mean().round(10))