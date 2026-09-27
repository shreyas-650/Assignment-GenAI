#Task 6: Normalization (MinMaxScaler)
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
path = '../online food delivery dataset.csv'
df = pd.read_csv(path)

mms = MinMaxScaler()

numerical = df.select_dtypes(include=['number'])

result = pd.DataFrame(
    mms.fit_transform(numerical),
    columns=numerical.columns
)
print(result)

#Values are scaled between 0 and 1
result.plot()
plt.show()