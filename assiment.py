# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ==========================
# Task 1: Load and Explore Data
# ==========================
try:
    # Load Iris dataset from sklearn
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map(
        {0: 'setosa', 1: 'versicolor', 2: 'virginica'})

    print("First 5 rows:")
    display(df.head())

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

    # Clean data (Iris dataset has no missing values, but example shown)
    df = df.dropna()

except FileNotFoundError:
    print("Error: Dataset file not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# ==========================
# Task 2: Basic Data Analysis
# ==========================
print("\nBasic Statistics:")
print(df.describe())

# Grouping by species
species_means = df.groupby('species').mean()
print("\nAverage values by species:")
print(species_means)

# Findings
print("\nObservations:")
print("- Setosa generally has smaller petal length and width compared to other species.")
print("- Virginica tends to have the largest measurements across most features.")
print("- Versicolor is in between Setosa and Virginica.")

# ==========================
# Task 3: Data Visualization
# ==========================
sns.set(style="whitegrid")

# Line chart: Petal length sorted over index (not real time-series, but for illustration)
plt.figure(figsize=(8, 5))
plt.plot(df.index, df['petal length (cm)'], label='Petal Length', color='blue')
plt.title('Petal Length Trend Across Samples')
plt.xlabel('Sample Index')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.show()

# Bar chart: Average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(x='species', y='petal length (cm)',
            data=df, estimator=np.mean, palette='Set2')
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# Histogram: Distribution of sepal length
plt.figure(figsize=(8, 5))
plt.hist(df['sepal length (cm)'], bins=15, color='green', alpha=0.7)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot: Sepal length vs Petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)',
                hue='species', data=df, palette='Set1')
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
