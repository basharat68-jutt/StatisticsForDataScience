# Covariance & Correlation Analysis

This project demonstrates how to calculate and visualize **Correlation** and **Covariance** using Python, Pandas, Matplotlib, and Seaborn.

## 📌 Project Overview

In this project, the `tips.csv` dataset is used to understand the relationship between numerical variables.

Two important statistical concepts are covered:

* **Correlation**
* **Covariance**

The numerical columns are selected from the dataset using `select_dtypes()`, and then correlation and covariance matrices are calculated using Pandas.

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn

## 📂 Dataset

The project uses the **Tips Dataset (`tips.csv`)**.

The dataset contains information such as:

* Total Bill
* Tip
* Size
* Sex
* Smoker
* Day
* Time

## 📊 Correlation

Correlation measures the **strength and direction of the linear relationship** between two numerical variables.

Correlation values range from:

* **+1** → Strong positive correlation
* **0** → No linear correlation
* **-1** → Strong negative correlation

Correlation is calculated using:

```python
data_corr = dataset.select_dtypes(["float64", "int64"]).corr()
```

## 📈 Covariance

Covariance shows the **direction of the relationship** between two variables.

Unlike correlation, covariance does **not have a fixed range of -1 to +1**. Its value depends on the scale of the variables.

Covariance is calculated using:

```python
data_cov = dataset.select_dtypes(["float64", "int64"]).cov()
```

## 🔥 Covariance Heatmap

A Seaborn heatmap is used to visualize the covariance matrix:

```python
plt.figure(figsize=(4,3))
sns.heatmap(data_cov, annot=True)
plt.show()
```

The heatmap makes it easier to understand how numerical variables vary together.

## 🎯 Learning Objectives

Through this project, I learned:

* How to calculate correlation using Pandas
* How to calculate covariance using Pandas
* Difference between covariance and correlation
* How to select numerical columns using `select_dtypes()`
* How to create a heatmap using Seaborn
* How statistical relationships can be visualized

## 🚀 How to Run

1. Clone this repository.
2. Make sure Python is installed.
3. Install the required libraries:

```bash
pip install pandas matplotlib seaborn
```

4. Keep `tips.csv` in the same directory as the Python file.
5. Run the Python program.

## 📌 Key Difference

| Correlation                                     | Covariance                                 |
| ----------------------------------------------- | ------------------------------------------ |
| Measures strength and direction of relationship | Measures how two variables change together |
| Range is -1 to +1                               | No fixed range                             |
| Unitless                                        | Depends on the units of variables          |
| Easier to compare between variables             | More affected by scale                     |

## 👨‍💻 Author

This project is part of my journey of learning **Python, Data Science, Statistics, and Machine Learning**.
