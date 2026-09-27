#Task 1 - Creating New Features
import pandas as pd
path = '../online food delivery dataset.csv'
df = pd.read_csv(path)

def grp(val):
    if val>=18 and val<=25:
        return 'Adult'
    elif val>25:
        return 'MidAge'
    else:
        return 'Child'
def sus(x):
    a='Customer Type'
    b='Feedback'
    if x[a]=='Regular' and x[b]=='Negative':
        return 'Priority'
    elif x[a]=='Frequent' and x[b]=='Negative':
        return 'Mid Priority'
    else:
        return 'Low Priority'

df.drop(['Unnamed: 13','latitude','longitude'],axis=1,inplace=True)
df[['Customer Type','Feedback']] = df[['Customer Type','Feedback']].astype('category')

df['Age_grp'] = df['Age'].apply(grp)
df['Feedback'] = df['Feedback'].str.strip()
df['Priority'] = df[['Customer Type','Feedback']].apply(sus,axis=1)
print(df.sample(5))
print(df['Feedback'].unique())
print(df[['Customer Type','Feedback','Priority']].sample(20))