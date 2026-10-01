#Task 7 Overfitting and Underfitting
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
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
#---------------------- Training The m1
svm1 = SVC(kernel='rbf',C=0.001) #simple
svm2 = SVC(kernel='rbf',C=1000) #complex
m1 = svm1.fit(X_train,Y_train)
m2 = svm2.fit(X_train,Y_train)

#-----------------------  Making Prediction
Ytrain_predict = m1.predict(X_train)
Y_predict = m1.predict(X_test)

Ytrain_predict2 = m2.predict(X_train)
Y_predict2 = m2.predict(X_test)

print('[Simple]Training Acc',accuracy_score(Y_train,Ytrain_predict)*100,'Testing Acc',accuracy_score(Y_test,Y_predict)*100)
print('[Complex]Training Acc',accuracy_score(Y_train,Ytrain_predict2)*100,'Testing Acc',accuracy_score(Y_test,Y_predict2)*100)

#Observation :-
#In Simple Config(Underfitting)- The Training and Testing Accuracy is Decent
#In Complex Config(Overfitting)- The Training is very good but Testing Accuracy is Very Bade

