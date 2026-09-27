#Task 9 Bivariate Analysis

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

#Bivariate Analysis
#numerical vs numerical
sns.scatterplot(data=df,x='sleep_hours',y='hours_studied')
plt.figure()
sns.heatmap(pd.crosstab(df['sleep_hours'],df['hours_studied'],normalize=True)*100)
plt.figure()
#categorical vs numerical
sns.barplot(data=df,x='gender',y='hours_studied')
plt.figure()
sns.boxplot(data=df,x='gender',y='hours_studied')
plt.figure()
sns.violinplot(data=df,x='gender',y='hours_studied')

plt.show()