#Task 2 -Decision Tree Algorithm
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
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
# Feature Scaling no need in decision tree

#Model Training

m1 = DecisionTreeClassifier(max_depth=1).fit(X_train,Y_train)
m2 = DecisionTreeClassifier(max_depth=3).fit(X_train,Y_train)
# Visualize the tree structure
plt.figure(figsize=(25,15))
plot_tree(m2, feature_names=X.columns, filled=True)
plt.show()

Y_train1 = m1.predict(X_train)
Y_train2 = m2.predict(X_train)
Y_predict1 = m1.predict(X_test)
Y_predict2 = m2.predict(X_test)

print('TRAIN1',accuracy_score(Y_train,Y_train1)*100,'TEST1',accuracy_score(Y_test,Y_predict1)*100)
print('TRAIN2',accuracy_score(Y_train,Y_train2)*100,'TEST2',accuracy_score(Y_test,Y_predict2)*100)


