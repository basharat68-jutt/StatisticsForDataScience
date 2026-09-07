"""Percentile & Quartiles"""
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("Titanic-Dataset.csv")
print(dataset.head(3))
dataset["Age"] = dataset["Age"].fillna(dataset["Age"].mean(),inplace=True)
#also check skewed of  a data like this
print(dataset["Age"].skew())
sns.histplot(x="Age",data=dataset) #this is a positive skewed

data = np.random.normal(0,100,100)
print(data)
df = pd.DataFrame({"x":data})
print(df["x"].skew())
sns.histplot(x="x",data=df)

data = [2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,9,9,9,9,10,10,10,11,11,12]
print(data)
df = pd.DataFrame({"x":data}) #normal skewed
print(df["x"].skew())
sns.histplot(x="x",data=df,bins=[2,3,4,5,6,7,8,9,10,11,12,13])
#mean
print(df["x"].mean())
print(df["x"].median())
print(df["x"].mode())
plt.show()