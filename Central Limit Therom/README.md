# Central Limit Theorem

This project demonstrates the **Central Limit Theorem (CLT)** using Python, NumPy, Pandas, Matplotlib, and Seaborn.

## 📌 About the Project

The **Central Limit Theorem** states that when we take sufficiently large random samples from a population, the distribution of the **sample means** tends to become approximately normally distributed, even if the original population data is not normally distributed.

In this project:

* A population of **10,000 random values** is generated.
* The population distribution is visualized using a KDE plot.
* **50 random samples** are taken from the population.
* Each sample contains **500 observations**.
* The mean of each sample is calculated.
* The distribution of these sample means is visualized.
* Finally, the population mean and the mean of the sample means are compared.

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn

## 🔄 Project Workflow

```text
Generate Population Data
        ↓
Visualize Population Distribution
        ↓
Take Random Samples
        ↓
Calculate Mean of Each Sample
        ↓
Create Distribution of Sample Means
        ↓
Compare Population Mean
with
Mean of Sample Means
```

## 📊 Implementation

### 1. Generate Population

```python
pop_data = [np.random.randint(10,100) for i in range(10000)]
```

A population containing 10,000 random values between 10 and 99 is generated.

### 2. Visualize Population

```python
sns.kdeplot(x="pop_data", data=pop_table)
```

The KDE plot shows the distribution of the original population.

### 3. Generate Samples

```python
for num_sample in range(50):

    sample_data = []

    for data in range(500):
        sample_data.append(np.random.choice(pop_data))

    sample_mean.append(np.mean(sample_data))
```

Here, 50 samples are generated, with **500 observations in each sample**.

The mean of every sample is stored in `sample_mean`.

### 4. Visualize Sample Means

```python
sns.kdeplot(x="Sample_mean", data=sample_n)
```

This plot shows the distribution of the sample means.

According to the Central Limit Theorem, the distribution of sample means tends to become approximately **normal** when the sample size is sufficiently large.

### 5. Compare Means

```python
print(np.mean(pop_data))
print(np.mean(sample_mean))
```

The population mean and the mean of the sample means are expected to be approximately equal.

## 📈 Key Learning

This project demonstrates that:

* The original population does not necessarily need to be normally distributed.
* Taking sufficiently large random samples produces a distribution of sample means that tends toward a normal distribution.
* The mean of the sample means is generally close to the population mean.
* Increasing the sample size generally makes the sampling distribution more stable and closer to normal.

## 🎯 Purpose

The purpose of this project is to understand the practical working of the **Central Limit Theorem** through simulation and visualization using Python.

## 👨‍💻 Author

**Basharat Jutt**
