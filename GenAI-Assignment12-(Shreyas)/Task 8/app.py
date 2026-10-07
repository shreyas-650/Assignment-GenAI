#Task 8 Multi-Plots & Figure-Level Plots
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('../performance.csv')
df['Gender'] = df['Gender'].astype('category')

g = sns.FacetGrid(data=df,col='Parental_Education_Level')
g.map(sns.scatterplot,'Hours_Studied','Exam_Score')

#2nd
sns.relplot(df,x='Hours_Studied',y='Exam_Score',col='Gender')
sns.catplot(df,x='Gender',y='Exam_Score',kind='box')
sns.displot(df,x='Exam_Score',col='Gender',kind='hist')

plt.show()
