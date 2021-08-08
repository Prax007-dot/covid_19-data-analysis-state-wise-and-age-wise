import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv")
data_1= pd.read_csv("C:/Users/user/Desktop/aoa exp/Book3.csv")
m=data.groupby('State')['Active'].sum().sort_values(ascending=False)
data.groupby('State')['Active'].sum().sort_values(ascending=False)
data.groupby('State')['Active'].sum().drop('Total').drop('State Unassigned').sort_values(ascending=False)
d=data.groupby('State')['Active'].sum().drop('Total').drop('State Unassigned').sort_values(ascending=False)
d.plot.bar(figsize=(15,5))
plt.show()
p=data.groupby('State')['Active'].sum().drop('Total').drop('State Unassigned').sort_values(ascending=False)/403312*100
p.plot.bar(figsize=(15,5))
plt.show()
sns.scatterplot(x="State" , y="Active" ,data=data)
data_1
sns.scatterplot(data=data_1, x="Age Group", y="No. Cases", hue="No. Deaths",palette= "deep")
l=data_1.drop([11])
sns.scatterplot(data=l, x="Age Group", y="No. Cases", hue="No. Deaths",size = "No. Deaths",sizes=(100,150))
age_wise=data_1.groupby('Age Group')['No. Cases'].sum().drop('Total').sort_values(ascending=False)
age_wise.plot.bar(figsize=(15,5))
plt.show()