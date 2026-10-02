#Task 5 Bagging vs Boosting (conceptual+practice)
'''
Bagging:- Bagging is a supervised learning technique used to train data from multiple models by spliting it in random order, The out is predicted by Max Value in Classification and Average Value in Regression
Boosting:- It is a supervised learning technique used to provive the output of weak learner to the input of the weak leaners until we get the generalized model
'''
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


path = '../pet_adoption_data.csv'
df = pd.read_csv(path)

# Data Cleaning
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
bc = BaggingClassifier(estimator=DecisionTreeClassifier(),n_estimators=100,random_state=42)
m1 = bc.fit(X_test,Y_test)
abc = AdaBoostClassifier(estimator=DecisionTreeClassifier(max_depth=1),n_estimators=100,random_state=42)
m2 = abc.fit(X_test,Y_test)

test_predict1 = m1.predict(X_test)
test_predict2 = m2.predict(X_test)
print('Bagging Classifier',accuracy_score(Y_test,test_predict1)*100)
print('AdaBoost Classifier',accuracy_score(Y_test,test_predict2)*100)

