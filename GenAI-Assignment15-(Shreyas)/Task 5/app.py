#Task 5 KNN
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
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

#---------------------- Training The Model
for x in [3,5,7]:
    knc = KNeighborsClassifier(n_neighbors=x)
    model = knc.fit(X_train,Y_train)
    #-----------------------  Making Prediction
    Y_predict = model.predict(X_test)
    print(accuracy_score(Y_test,Y_predict)*100)
    #-----------------------  Task 6 Evaluation Metrics for Classification

    from sklearn.metrics import *

    print(precision_score(Y_test,Y_predict))
    print(recall_score(Y_test,Y_predict))
    print(f1_score(Y_test,Y_predict))
    print(confusion_matrix(Y_test,Y_predict),'\n')




