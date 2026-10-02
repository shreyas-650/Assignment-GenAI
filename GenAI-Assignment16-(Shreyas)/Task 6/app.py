#Task 6: Random Forest Bagging
from sklearn.ensemble import RandomForestClassifier,BaggingClassifier
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
rf = RandomForestClassifier(n_estimators=100)
model = rf.fit(X_train,Y_train)
#Single Decision Tree and #Bagging Classifier
dt_model = DecisionTreeClassifier(max_depth=5).fit(X_train,Y_train)
bg = BaggingClassifier(estimator=DecisionTreeClassifier(),n_estimators=100,random_state=42).fit(X_train,Y_train)


test_predict = model.predict(X_test)

t_dtmodel = dt_model.predict(X_test)
t_bg = bg.predict(X_test)
print('Random Forest',accuracy_score(Y_test,test_predict)*100)
print('Decision Tree',accuracy_score(Y_test,t_dtmodel)*100)
print('Bagging',accuracy_score(Y_test,t_bg)*100)

# Feature Importance
importance = pd.Series(
    model.feature_importances_,
    index=X.columns
)

print(importance.sort_values(ascending=False)*100)