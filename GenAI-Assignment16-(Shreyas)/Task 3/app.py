#Task 3 Train vs Validation Vs Test Split
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
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
X_train,X_temp,Y_train,Y_temp = train_test_split(X,Y,test_size=0.36,random_state=42)

X_val,X_test,Y_val,Y_test = train_test_split(X_temp,Y_temp,test_size=0.5556,random_state=42)

#Model Training
# Train Model on Training Data
m1 = DecisionTreeClassifier(max_depth=3).fit(X_train,Y_train)

#Tune one simple parmeter using validation set

for depth in [1,3,5,10]:
    m = DecisionTreeClassifier(max_depth=depth)
    m.fit(X_train,Y_train)

    val_predict = m.predict(X_val)
    print('Depth Level: ',depth,accuracy_score(Y_val,val_predict)*100,'\n')

#Evaluation final model on test set

test_predict = m1.predict(X_test)
print('Final Model Test',accuracy_score(Y_test,test_predict)*100)