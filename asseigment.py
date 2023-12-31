# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oidt7ykX4yNJMqeKZr0VpWLf4LTWKw7a
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind,f_oneway,pearsonr
import statsmodels.api as sm

boston_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/boston_housing.csv'
boston_df=pd.read_csv(boston_url)

plt.figure(figsize=(8, 6))
plt.boxplot(boston_df['MEDV'])
plt.title('Boxplot of Median Value of Owner-Occupied Homes (MEDV)')
plt.ylabel('MEDV ($1000s)')
plt.show()

plt.figure(figsize=(8, 6))
sns.countplot(data=boston_df, x='CHAS')
plt.title('Bar Plot of Houses Bounded by Charles River (0: No, 1: Yes)')
plt.xlabel('CHAS')
plt.ylabel('Count')
plt.show()

boston_df['AGE_Group'] = pd.cut(boston_df['AGE'], bins=[0, 35, 70, max(boston_df['AGE'])], labels=['35 and Younger', 'Between 35 and 70', '70 and Older'])

plt.figure(figsize=(10, 6))
sns.boxplot(data=boston_df, x='AGE_Group', y='MEDV')
plt.title('Boxplot of MEDV by Age Groups')
plt.xlabel('Age Group')
plt.ylabel('MEDV ($1000s)')
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(boston_df['INDUS'], boston_df['NOX'], alpha=0.5)
plt.title('Scatter Plot of NOX vs. INDUS')
plt.xlabel('INDUS (Proportion of Non-Retail Business Acres)')
plt.ylabel('NOX (Nitric Oxide Concentrations)')
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(boston_df['PTRATIO'], bins=15, edgecolor='k', alpha=0.7)
plt.title('Histogram of Pupil to Teacher Ratio (PTRATIO)')
plt.xlabel('PTRATIO')
plt.ylabel('Frequency')
plt.show()

river_houses = boston_df[boston_df['CHAS'] == 1]['MEDV']
no_river_houses = boston_df[boston_df['CHAS'] == 0]['MEDV']

t_stat, p_value = ttest_ind(river_houses, no_river_houses)

# Check if p-value is less than alpha (0.05)
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference.")

age_groups = boston_df['AGE_Group'].unique()
grouped_data = [boston_df[boston_df['AGE_Group'] == group]['MEDV'] for group in age_groups]

f_stat, p_value = f_oneway(*grouped_data)

# Check if p-value is less than alpha (0.05)
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference among age groups.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference among age groups.")

r, p_value = pearsonr(boston_df['NOX'], boston_df['INDUS'])

# Check if p-value is greater than alpha (0.05)
if p_value > alpha:
    print("Fail to reject the null hypothesis. There is no relationship between NOX and INDUS.")
else:
    print("Reject the null hypothesis. There is a relationship between NOX and INDUS.")

import statsmodels.api as sm


X = boston_df['DIS']
X = sm.add_constant(X)
y = boston_df['MEDV']

model = sm.OLS(y, X).fit()
summary = model.summary()


dis_coeff_pvalue = model.pvalues['DIS']


if dis_coeff_pvalue < alpha:
    print("Reject the null hypothesis. There is an impact of DIS on MEDV.")
else:
    print("Fail to reject the null hypothesis. There is no impact of DIS on MEDV.")