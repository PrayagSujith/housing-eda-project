import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Housing.csv')

print("--- Data Overview ---")
print(df.head())
print("\n--- Data Info ---")
print(df.info())

print("\n--- Identifying Missing Values ---")
print(df.isnull().sum())

df['sqft_living'] = df['sqft_living'].fillna(df['sqft_living'].mean())
df['sqft_lot'] = df['sqft_lot'].fillna(df['sqft_lot'].mean())
df['yr_built'] = df['yr_built'].fillna(df['yr_built'].mean())

most_frequent_city = df['city'].mode()[0]
df['city'] = df['city'].fillna(most_frequent_city)

print("Verification: Missing values after cleaning:")
print(df.isnull().sum())

df = df[(df['price'] > 0) & (df['bedrooms'] > 0)]
df = df[df['price'] <= 5000000]

df['house_age'] = 2014 - df['yr_built']
df['price_per_sqft'] = df['price'] / df['sqft_living']

print("\n--- Data Cleaning & Feature Engineering Complete ---")
print(f"Final Clean Rows: {df.shape[0]}")

print("\n--- Final Descriptive Statistics ---")
print(df.describe())

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = df[numeric_cols].corr()

print("\n--- Key Price Drivers ---")
print(correlation_matrix['price'].sort_values(ascending=False))

plt.figure(figsize=(10, 6))
sns.histplot(df['price'], kde=True, color='blue')
plt.title('Distribution of House Prices (Univariate)')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.savefig('price_distribution.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='sqft_living', y='price', data=df, color='green')
plt.title('House Price vs. Square Footage (Bivariate)')
plt.xlabel('Square Footage (Living)')
plt.ylabel('Price ($)')
plt.savefig('price_vs_sqft.png')
plt.close()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap (Multivariate)')
plt.savefig('correlation_heatmap.png')
plt.close()

print("\nAll visualizations generated successfully.")