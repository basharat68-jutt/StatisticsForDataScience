# Percentile & Quartiles Analysis

This project demonstrates basic statistical analysis using **NumPy, Pandas, Matplotlib, and Seaborn**. It focuses on understanding data distribution, skewness, and measures of central tendency using both the Titanic dataset and randomly generated data.

## 📌 Topics Covered

* Percentile and Quartiles
* Mean
* Median
* Mode
* Skewness
* Histogram
* Normal Distribution
* Positive Skewness
* DataFrame creation using Pandas
* Handling missing values

## 🛠️ Libraries Used

* **NumPy** – numerical operations and random data generation
* **Pandas** – data loading and DataFrame manipulation
* **Matplotlib** – data visualization
* **Seaborn** – histogram visualization

## 📂 Dataset

The project uses the **Titanic-Dataset.csv** dataset.

The `Age` column is analyzed to understand its distribution and skewness. Missing values in the `Age` column are intended to be handled using the mean.

## 📊 Analysis Performed

### 1. Titanic Age Distribution

The `Age` column from the Titanic dataset is analyzed using:

* Mean
* Skewness
* Histogram

The histogram helps visualize how the ages are distributed.

### 2. Random Normal Data

Random data is generated using NumPy:

```python
data = np.random.normal(0, 100, 100)
```

The generated data is converted into a Pandas DataFrame and its skewness is calculated. A histogram is then used to visualize the distribution.

### 3. Custom Data Distribution

A manually created dataset is analyzed to calculate:

* Mean
* Median
* Mode
* Skewness

A histogram is also created to understand the shape of the distribution.

## 📈 Visualizations

The project uses Seaborn's `histplot()` to visualize data distributions.

```python
sns.histplot(x="Age", data=dataset)
```

and:

```python
sns.histplot(x="x", data=df)
```

These plots help identify whether the data is approximately normally distributed or skewed.

## 🎯 Purpose

The main purpose of this project is to build a practical understanding of **descriptive statistics and data distributions** before moving toward more advanced data analysis and machine learning concepts.

## 🚀 How to Run

1. Install the required libraries:

```bash
pip install numpy pandas matplotlib seaborn
```

2. Place `Titanic-Dataset.csv` in the project directory.

3. Run the Python file or Jupyter Notebook.

## 👨‍💻 Author

Basharat Jutt
