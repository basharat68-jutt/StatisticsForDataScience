import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import seaborn as sns

"""Finding Mean Manually"""
ar = np.array([4,5,6,2,1,8,5,6,4,7])
sum = np.sum(ar)
print(sum)
length = len(ar)
print(length)
mean = sum/length
print(mean)
"""Formula"""
mean = np.mean(ar)
print(mean)

dataset = pd.read_csv("Titanic-Dataset.csv")
print(dataset.head(3))
mean = dataset["Age"].mean()        #titanic k data set ko use kia
# mn = np.mean(dataset["Age"])
print(mean)
sns.histplot(x="Age",data=dataset,bins=[i for i in range(0,81,10)]) #graph bhi plot kr dia
# sns.histplot(x="Age",data=dataset,bins=[i for i in range(0,81,10)])
plt.plot([mean for i in range(0,300)],[i for i in range(0,300)],c='green',label="Mean")


"""Median"""

dataset["Age"] = dataset["Age"].fillna(dataset["Age"].mean(),inplace=True)
print(dataset.isnull().sum())

median = np.median(dataset["Age"])  #datast["Age"].median()
print(median)
plt.plot([median for i in range(0,300)],[i for i in range(0,300)],c='blue',label="Median")


"""Mode"""
mode = dataset["Fare"].mode()[0]
print(mode)
print(dataset['Fare'].value_counts()) #check frequency of mode
plt.plot([mode for i in range(0,300)],[i for i in range(0,300)],c='red',label="Mode")
# plt.plot([mode for i in range(0,300)],[i for i in range(0,300)],c="red")

plt.show()