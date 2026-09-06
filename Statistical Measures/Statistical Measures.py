"""Range , Mean absolute division , variance , standard deviation"""

import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("Titanic-Dataset.csv")
print(dataset.head(3))

"""Range"""
minimum_value = np.min(dataset["Age"])
print(minimum_value)
maximun_value = np.max(dataset["Age"])
print(maximun_value)
Range = maximun_value - minimum_value
print(Range)

"""Mean Absolute Deviation""" #isko bht km use krty hain keu iska koe direct formula nhii hai...ziada tr variance or std ko he use krty hain
sec_a = np.array([75,65,73,68,72,67])
sec_b = np.array([90,47,43,96,93,51])
mean = np.mean(sec_b)
print(mean)
no = np.array([1,2,3,4,5,6])
plt.figure(figsize=(10,3))
plt.scatter(sec_a,no,label="Sec A")
plt.scatter(sec_b,no,color="red",label="Sec B")
plt.plot([70,70,70,70,70,70],no,c="blue",label="Mean")
plt.legend()
# plt.show()

print(np.abs(-2)) #abs means modulus agr minus mein value dy gein to positive mein return kryy ga
mad_a = np.sum(np.abs(sec_a-mean))/len(sec_a)
mad_b = np.sum(np.abs(sec_b-mean))/len(sec_b)
print(mad_a,mad_b) #jis ka MAD km hai osi data ko he select krna hai

"""Standard Deviation"""
secA_std = np.std(sec_a)
secB_std = np.std(sec_b)
print(secA_std,secB_std)

"""Variance"""
secA_var = np.var(sec_a)
secB_var = np.var(sec_b)
print(secA_var,secB_var)

"""Graphical Representation"""
sns.histplot(x="Age",data=dataset)
plt.show()
















