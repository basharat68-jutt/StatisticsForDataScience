# Statistical Hypothesis Testing

This project contains practical examples of **Statistical Hypothesis Testing** using Python. It covers **Z-Test, T-Test, and Chi-Square Testing** with real-world style scenarios and numerical calculations.

## Topics Covered

### 1. Z-Test

The Z-Test is used to determine whether there is a significant difference between a sample result and a population value when the population standard deviation is known or the sample size is sufficiently large.

Examples included:

* Testing a teacher's claim about the average student score.
* Comparing the average purchase amount between an old and a new website design.

Important concepts used:

* Sample Mean
* Population Mean
* Population Standard Deviation
* Sample Size
* Significance Level (α)
* Calculated Z-Value
* Critical/Table Z-Value
* Null Hypothesis (H₀)
* Alternative Hypothesis (Hₐ)

Python libraries used:

```python
import scipy.stats as st
import numpy as np
```

The critical Z-value is calculated using:

```python
st.norm.ppf()
```

---

### 2. T-Test

The T-Test is used to determine whether there is a statistically significant difference between means, especially when the population standard deviation is unknown and the sample size is relatively small.

Examples included:

* Testing a manufacturer's claim about the average weight of potato chips.
* Comparing productivity between two different teams.
* Comparing typing speed before and after a training program.

Important concepts used:

* Sample Mean
* Sample Standard Deviation
* Sample Size
* Degree of Freedom (df)
* Significance Level (α)
* Calculated T-Value
* Critical T-Value
* One-Tailed Test
* Two-Tailed Test
* Paired Comparison

The critical T-value is calculated using:

```python
st.t.ppf()
```

Degree of freedom for a one-sample test:

```text
df = n - 1
```

---

### 3. Chi-Square Testing

Chi-Square Testing is used for categorical data to determine whether observed frequencies differ significantly from expected frequencies or whether two categorical variables are associated.

Examples included:

* Testing whether a dice is fair using observed and expected frequencies.
* Investigating the relationship between gender and preferred music genre.

Important concepts used:

* Observed Frequency
* Expected Frequency
* Chi-Square Statistic
* Significance Level
* Categorical Data
* Association between Variables

The Chi-Square statistic is calculated using:

```text
χ² = Σ (Observed - Expected)² / Expected
```

In Python:

```python
np.sum(np.square(ob-ex)/ex)
```

---

## Hypothesis Testing Process

The general process followed in these examples is:

1. Define the **Null Hypothesis (H₀)**.
2. Define the **Alternative Hypothesis (Hₐ)**.
3. Select the significance level (α).
4. Calculate the test statistic.
5. Find the critical/table value.
6. Compare the calculated value with the critical value.
7. Make a decision about H₀.
8. Interpret the result in the context of the problem.

## Libraries Used

* **NumPy** – numerical calculations and arrays
* **SciPy** – statistical distributions and critical values

## Key Learning

Through this project, I practiced how statistical tests can be used to make decisions about population claims using sample data. I also learned the difference between **Z-Test, T-Test, and Chi-Square Testing** and how significance levels, critical values, and hypothesis decisions are used in statistical analysis.
