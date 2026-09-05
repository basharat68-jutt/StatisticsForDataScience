# Mean, Median & Mode using Python

This project demonstrates how to calculate and visualize the three basic measures of central tendency:

* **Mean**
* **Median**
* **Mode**

The concepts are first implemented manually using a NumPy array and then applied to the **Titanic dataset** using Python libraries.

## 📌 Project Overview

Measures of central tendency are used to find a central or representative value in a dataset.

In this project:

* Mean is calculated manually and using NumPy.
* Mean of the Titanic `Age` column is calculated.
* Missing values in the `Age` column are handled using the mean.
* Median of the `Age` column is calculated.
* Mode of the `Fare` column is calculated.
* A histogram is used to visualize the distribution of Age.
* Mean, Median, and Mode are visualized on the graph.

## 🛠️ Libraries Used

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

### NumPy

Used for numerical calculations such as:

```python
np.sum()
np.mean()
np.median()
```

### Pandas

Used for:

* Reading the Titanic CSV dataset
* Data manipulation
* Handling missing values
* Calculating statistical values

### Matplotlib

Used for plotting and visualizing Mean, Median, and Mode.

### Seaborn

Used to create the Age distribution histogram.

## 📊 Mean

Mean is the average value of a dataset.

### Formula

**Mean = Sum of all values / Number of values**

Example:

```python
ar = np.array([4,5,6,2,1,8,5,6,4,7])

sum = np.sum(ar)
length = len(ar)

mean = sum / length
print(mean)
```

Mean can also be calculated directly using NumPy:

```python
mean = np.mean(ar)
```

## 📈 Mean using Titanic Dataset

The Titanic dataset is loaded using Pandas:

```python
dataset = pd.read_csv("Titanic-Dataset.csv")
```

The mean age is calculated using:

```python
mean = dataset["Age"].mean()
```

The Age distribution is visualized using a Seaborn histogram:

```python
sns.histplot(
    x="Age",
    data=dataset,
    bins=[i for i in range(0,81,10)]
)
```

## 📌 Median

Median is the middle value of a sorted dataset.

NumPy can be used to calculate the median:

```python
median = np.median(dataset["Age"])
```

The median is also useful when the data contains extreme values because it is less affected by outliers than the mean.

## 📌 Mode

Mode is the value that occurs most frequently in a dataset.

In this project, the mode of the Titanic `Fare` column is calculated:

```python
mode = dataset["Fare"].mode()[0]
```

The frequency of different fare values can be checked using:

```python
dataset["Fare"].value_counts()
```

## 📉 Visualization

Mean, Median, and Mode are represented on the graph using different lines.

```python
plt.plot(...)
plt.show()
```

The histogram shows the distribution of passenger ages, while the lines represent the calculated central tendency values.

## 📂 Dataset

The project uses the **Titanic-Dataset.csv** dataset.

Important columns used:

* `Age` → Used for Mean and Median
* `Fare` → Used for Mode

## 🎯 Learning Objectives

Through this project, you will understand:

* What Mean, Median, and Mode are
* How to calculate Mean manually
* How NumPy simplifies statistical calculations
* How to calculate statistics from a real-world dataset
* How to handle missing values
* How to visualize statistical values
* How Pandas, NumPy, Matplotlib, and Seaborn work together

## 🚀 Concepts Covered

`Python` • `NumPy` • `Pandas` • `Matplotlib` • `Seaborn` • `Statistics` • `Mean` • `Median` • `Mode` • `Data Visualization` • `Titanic Dataset`
