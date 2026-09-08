"""Coveriance & Correlation"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset =  pd.read_csv("tips.csv")
print(dataset.head())
dataset.info()
data_corr = dataset.select_dtypes(["float64","int64"]).corr() #correlation sirf 1 or -1 k dermyyan he aye ga
data_cov = dataset.select_dtypes(["float64","int64"]).cov() #jb k coveriance 1 or -1 k dermyyan nhii aye g

plt.figure(figsize=(4,3))
sns.heatmap(data_cov,annot=True)
plt.show()