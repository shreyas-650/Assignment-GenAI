#Task 8 Imported
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder
from sklearn.compose import ColumnTransformer

path = '../online food delivery dataset.csv'
df = pd.read_csv(path)
#Refining Data
df.drop(columns=['Unnamed: 13','latitude','longitude','Pin code'],inplace=True)

X = df.drop(columns=['Output'])
Y = df['Output']

numeric_col = X.select_dtypes(include=['number']).columns
ordinal_col = ['Occupation']
norminal_col = X.select_dtypes(include=['object','string']).columns
norminal_col = norminal_col.drop('Occupation')

#Creating Seprate Pipelines
Num_pipeline = Pipeline(steps=[('impute',SimpleImputer(strategy='mean')),('scaling',StandardScaler())])
Ordinal_pipeline = Pipeline(steps=[('impute',SimpleImputer(strategy='most_frequent')),('encode',OrdinalEncoder()),('scaling',StandardScaler())])
norminal_pipeline = Pipeline(steps=[('impute',SimpleImputer(strategy='most_frequent')),('encode',OneHotEncoder(handle_unknown='ignore'))])

#Combine Them

features = ColumnTransformer(transformers=[('Numeric Pipeline',Num_pipeline,numeric_col),('Ordinal Pipeline',Ordinal_pipeline,ordinal_col),('Norminal Pipeline',norminal_pipeline,norminal_col)])

#-----------   Task 8 Full Scikit-learn Pipeline
#-----------   Model Creation = Features + Algorithm

from sklearn.linear_model import LogisticRegression

model = Pipeline(steps=[('features',features),('algo',LogisticRegression())])

#-----------   Split Data into train-test sets

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder #for Output column

Y = LabelEncoder().fit_transform(Y)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

#---------------- Model Train and Prediction

model.fit(X_train,Y_train)
Y_predict = model.predict(X_test)

#----------------   Accuracy

from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,Y_predict))


