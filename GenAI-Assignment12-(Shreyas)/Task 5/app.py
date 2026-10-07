#Task 5 Matrix Plots
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../performance.csv')
df['Parental_Education_Level'] = df['Parental_Education_Level'].astype('category')
df['Parental_Involvement'] = df['Parental_Involvement'].astype('category')
sns.pairplot(data=df)
plt.figure()

temp = df.pivot_table(index='Parental_Involvement',columns='Hours_Studied',values='Attendance',aggfunc='mean')
print(temp)
sns.heatmap(data=temp)
plt.show()
