#Task 1 - Linear Regression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

path = '../car data.csv'
df = pd.read_csv(path)

#Data Cleaning and Preprocessing
df['owner'] = df['owner'].replace(['Third Owner','Fourth & Above Owner'],'Third & Above Owner')

df.drop(columns=['name'],inplace=True)
df.drop_duplicates(inplace=True)

# for col in df.select_dtypes(include='object').columns:
#     print(col,df[col].unique())
# for col in df.select_dtypes(include='number').columns:
#     print(col,df[col].describe())

#Encoding
oe = OrdinalEncoder(categories=[['Third & Above Owner','Second Owner','Test Drive Car','First Owner']])
df['owner'] = oe.fit_transform(df[['owner']])
ohe = OneHotEncoder(sparse_output=False)
x = ohe.fit_transform(df[['fuel','seller_type','transmission']])
df[ohe.get_feature_names_out()] = x
df.drop(columns=['fuel','seller_type','transmission'],inplace=True)

temp = df.pop('selling_price')
df.insert(len(df.columns),'selling_price',temp)

X = df.iloc[:,:-1]
Y = df['selling_price']
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
#feature scaling
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

#Model Training
lr = LinearRegression()
model = lr.fit(X_train,Y_train)

Y_predict = model.predict(X_test)

plt.scatter(x=Y_test,y=Y_predict)
plt.xlabel('Actual Value')
plt.ylabel('Y Predict')
plt.title('Actual Vs Predicted Car Price')
plt.show()




