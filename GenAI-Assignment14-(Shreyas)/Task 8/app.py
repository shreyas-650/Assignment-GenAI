#Task 8 Univariate Analysis

# Data Cleaning:
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../performance.csv')
df = df[['Hours_Studied', 'Attendance', 'Parental_Involvement',
       'Access_to_Resources', 'Sleep_Hours', 'Motivation_Level', 'Internet_Access',
        'Family_Income', 'Teacher_Quality', 'Gender',
       'Exam_Score']]
#handling missing values
df['Teacher_Quality'] = df['Teacher_Quality'].astype('category')
df['Teacher_Quality'] = df['Teacher_Quality'].fillna(df['Teacher_Quality'].mode()[0])
#No duplicated row if it had I had used df['Name']= df['Name'].drop_duplicates()

#rename col to lowercase and snake_case

df.columns = df.columns.str.lower()

#fixing incorrect dtypes
df['parental_involvement']=df['parental_involvement'].astype('category')
df['access_to_resources']=df['access_to_resources'].astype('category')

#Univariate Analysis

sns.histplot(data=df,x='sleep_hours',kde=True)
plt.figure()
sns.countplot(data=df,x='access_to_resources')
plt.figure()
sns.boxplot(data=df,x='sleep_hours')
sns.boxplot(data=df,x='sleep_hours')
plt.figure()
#4
sns.heatmap(pd.crosstab(df['gender'],df['teacher_quality'],normalize=True)*100)
plt.show()