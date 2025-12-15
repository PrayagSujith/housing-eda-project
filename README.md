# Exploratory Data Analysis of Housing Dataset

## Project Overview
This project performs an Exploratory Data Analysis (EDA) on a housing dataset
containing 4,600 residential property records. The objective is to identify
the key factors that influence house prices using statistical analysis and
visualization techniques in Python.

## Dataset
- Source: Housing.csv
- Records: 4,600
- Features: Price, Bedrooms, Bathrooms, Sqft Living, Sqft Lot, Floors,
  Waterfront, View, Condition, Year Built, Renovation Year, etc.

## Tools & Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Analysis Performed
### 1. Data Cleaning
- Missing value imputation (Mean/Mode)
- Removal of invalid values (Price = 0, Bedrooms = 0)
- Outlier treatment (Price > $5M removed)

### 2. Feature Engineering
- House Age
- Price per Square Foot

### 3. Exploratory Data Analysis
- **Univariate Analysis**: Price distribution (right-skewed)
- **Bivariate Analysis**: Price vs Sqft Living (strong positive relationship)
- **Multivariate Analysis**: Correlation heatmap

## Key Insights
- Sqft Living is the strongest price driver (Correlation ≈ 0.69)
- Bathrooms have more impact than bedrooms
- Year Built has negligible impact on price
- Median price is more representative than mean

## Visualizations
All plots are available in the `Images/` folder.

## Author
**Prayag Sujith**  
