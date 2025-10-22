import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv(r"D:\Power BI Project File\COVID-19.csv")
data.head()
data.describe()
data.tail()
data.columns
data.isnull().sum()
data.columns
sns.relplot(x="Total_Confirmed_cases", y="New_recovered",hue="Latitude",data=data)
sns.relplot(x="Total_Confirmed_cases",y="Discharged",hue="Longitude", data=data)
sns.relplot(x="Latitude",y="Total_Confirmed_cases",data=data)
data.columns
sns.relplot(x="Longitude",y="New_recovered",hue="Date",data=data)
sns.pairplot(data)
sns.relplot(x="Discharged",y="New_cases", kind="line",data=data)
data.columns
sns.catplot(x="Discharged",y="New_cases",data=data)

