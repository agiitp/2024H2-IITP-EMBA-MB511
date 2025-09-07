import pandas as pd
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import regex as re
path = "/Users/ag/IIT_Patna/Git_Hub/2024H2-IITP-EMBA-MB511/Datasets/001-Sales-Data/" 
#cur_path = os.getcwd()
print(path)
# Read the Excel file into a DataFrame
# By default, it reads the first sheet.
sale_data = pd.read_excel(path + "001-Store-Information.xlsx")

# Print the first 5 rows of the DataFrame
print(sale_data.head())

# print the columns in the given data
print(sale_data.columns)

# print the shape of the given data
print(sale_data.shape)

# print the data types of the given data
print(sale_data.dtypes)

# print the summary statistics of the given data
print(sale_data.describe())

# print the unique values in the given data
print(sale_data.nunique())

# print the missing values in the given data
print(sale_data.isnull().sum())

# print the data in the given data
print(sale_data)

#print the descripting analysis of the data
print(sale_data.describe())

# print the information of the given data
print(sale_data.info())

#Generate the different chart of the data using matplotlib
#sale_data.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)


#Histograms (for numerical data): Show the distribution of a single numerical variable.
plt.hist(sale_data['Cluster'], bins=10) # bins define the number of bars
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Distribution of Column Name')
plt.show()


#Bar Charts (for categorical data): Represent the frequency or count of different categories.
category_counts = sale_data['Store-Manager'].value_counts()
plt.bar(category_counts.index, category_counts.values)
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Counts of Categorical Column')
plt.xticks(rotation=45) # Rotate labels if needed
plt.show()



#Scatter Plots (for relationship between two numerical variables):
plt.scatter(sale_data['Store-ID'], sale_data['Cluster'])
plt.xlabel('Store ID')
plt.ylabel('Cluster')
plt.title('Scatter Plot of Store ID vs Cluster')
plt.show()


#Correlation Analysis
# Select only numerical columns from the DataFrame
sale_data1 = sale_data.select_dtypes(include=[np.number]) # Select only numerical columns
#Correlation matrix
correlation_matrix = sale_data1.corr()
#Displaying Correlation Analysis
plt.figure(figsize=(10, 8)) # Adjust figure size as needed
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix Heatmap')
plt.show()
