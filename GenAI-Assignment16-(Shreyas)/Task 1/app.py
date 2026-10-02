#Task 1 - Advanced Supervised Learning
import pandas as pd
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
path = '../pet_adoption_data.csv'
df = pd.read_csv(path)

# Data Cleaning
# df.info()
# print(df.duplicated().sum())
# for col in df.select_dtypes(include='string').columns:
#     print(df[col].value_counts(),'\n')
# for col in df.select_dtypes(include='number').columns:
#     print(df[col].describe(),'\n')
# Conclusion: Data is Clean

#Features Selection
df.drop(columns=['PetID'],inplace=True)

# Encoding
X = df.iloc[:,:-1]
Y = df['AdoptionLikelihood']
oh = OneHotEncoder(sparse_output=False)
x = oh.fit_transform(df[df.select_dtypes(include=['str']).columns])
X[oh.get_feature_names_out()] = x
X.drop(columns=X.select_dtypes('str').columns,inplace=True)

# Train Test Split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
# Feature Scaling
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

#Model Training

m1 = SVC(kernel='linear').fit(X_train,Y_train)
m2 = SVC(kernel='rbf').fit(X_train,Y_train)

Y_predict1 = m1.predict(X_test)
Y_predict2 = m2.predict(X_test)

print('Linear Kernel',accuracy_score(Y_test,Y_predict1)*100)
print('RBF Kernel',accuracy_score(Y_test,Y_predict2)*100)




