#Task 4 Cross-Validation
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.tree import DecisionTreeClassifier
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
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.36,random_state=42)

#Model Training
model = DecisionTreeClassifier(max_depth=3).fit(X_test,Y_test)

test_predict = model.predict(X_test)
print('Sinle Train Test Acc',accuracy_score(Y_test,test_predict)*100)

# Apply K=5
score = cross_val_score(model,X_train,Y_train,cv=5)

print('CV Accuracy',score*100)
print('CV Avg',score.mean()*100)