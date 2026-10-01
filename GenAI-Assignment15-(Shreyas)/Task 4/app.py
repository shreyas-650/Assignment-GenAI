#Task 4 Naive Bayes Classifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OneHotEncoder,StandardScaler,LabelEncoder
from sklearn.metrics import accuracy_score
path = '../heart_disease.csv'
df = pd.read_csv(path)

#---------------  Data cleaning & Preprocessing
#---------------  Checking -------------
# for col in df.select_dtypes(include=['object']).columns:
#     print(df[col].value_counts(),'\n')
# for col in df.select_dtypes(include=['number']).columns:
#     print(df[col].describe(),'\n')
# df.info()
# print(df.select_dtypes(include=['number']).columns)
# print(df.isnull().sum())

for col in df.select_dtypes(include='number'):
    df[col] = df[col].fillna(df[col].mean())

for col in df.select_dtypes('string'):
    df[col] = df[col].fillna(df[col].max())

#Feature Encoding 
X = df.drop(columns=['Heart Disease Status'])
Y = df['Heart Disease Status']

oh = OneHotEncoder(sparse_output=False)
x = oh.fit_transform(X[X.select_dtypes(include='string').columns])
X[oh.get_feature_names_out()] = x
X.drop(columns=X.select_dtypes('string').columns,inplace=True)


le = LabelEncoder()
Y = pd.Series(le.fit_transform(Y),index = Y.index)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

# Feature Scaling
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

#---------------------- Training The Model (Logistic and GaussianNB)
lr = LogisticRegression(max_iter=1000)
model = lr.fit(X_train,Y_train)
gnb = GaussianNB()
model2 = gnb.fit(X_train,Y_train)

#-----------------------  Making Prediction
Y_predict = model.predict(X_test)
Y_predict2 = model2.predict(X_test)

print((Y_predict == Y_predict2).sum()) # Values that are Same, Predicted by Both of the models
print('Logistic Reg',accuracy_score(Y_test,Y_predict)*100)
print('Gaussian NB',accuracy_score(Y_test,Y_predict2)*100)

#-----------------------  Task 6 Evaluation Metrics for Classification

from sklearn.metrics import *

print(precision_score(Y_test,Y_predict2))
print(recall_score(Y_test,Y_predict2))
print(f1_score(Y_test,Y_predict2))
print(confusion_matrix(Y_test,Y_predict2))
