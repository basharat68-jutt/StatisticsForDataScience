"""Central Limit Therom"""
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

pop_data = [np.random.randint(10,100) for i in range(10000)]
pop_table = pd.DataFrame({"pop_data":pop_data})
print(pop_table)
plt.figure(figsize=(3,2))
sns.kdeplot(x="pop_data",data=pop_table) #ye non-normal distribution data tha graph mein dekh skty hain

sample_mean = []
for num_sample in range(50):
    sample_data = []
    for data in range(500):
        sample_data.append(np.random.choice(pop_data))
    sample_mean.append(np.mean(sample_data))

sample_n = pd.DataFrame({"Sample_mean":sample_mean})
plt.figure(figsize=(3,2))
sns.kdeplot(x="Sample_mean",data=sample_n)

print(np.mean(pop_data)) #yahan in dono ka mean almost same hai
print(np.mean(sample_mean))
plt.show()

